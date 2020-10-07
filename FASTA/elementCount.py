#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="This is the input file.")
arg = parser.parse_args()
if arg.i :
	file = arg.i

infile = open(file, "r")
l = infile.readlines()
inp = []
for line in l:
    elements = line.split('\t')		#split items by tab
    elements[-1] = elements[-1].replace('\n','')
    elements[1] = int(elements[1])	#convert strings to ints
    elements[2] = int(elements[2])
    inp.append(elements)

def self_overlap(l):
    coords_by_chrom = {}
    for line in l:
        chrom = line[0]		#title of chrom
        coordinates = line[1:3]		#start & stop coordinates
        if chrom not in coords_by_chrom:
            coords_by_chrom[chrom] = []
        coords_by_chrom[chrom].append(coordinates)

    overlaps_by_chrom = {}
    for chrom in coords_by_chrom:
        coords = coords_by_chrom[chrom]
        overlaps = calculate_overlaps_for_chrom(coords)
        overlaps_by_chrom[chrom] = overlaps

    out = []
    for chrom in overlaps_by_chrom:
        overlaps = overlaps_by_chrom[chrom]
        for overlap in overlaps:
            start, end, count = overlap
            out.append([ chrom, start, end, count ])
    return out

def calculate_overlaps_for_chrom(coords):
    low = min(coords, key=lambda interval: interval[0])[0]		#find min; anonymous fxn
    high = max(coords, key=lambda interval: interval[1])[1]		#find max; anonymous fxn
    mask = [0] * (high - low)
    for interval in coords:
        start, end = interval[0], interval[1]
        for i in range(start-low, end-low):
            mask[i] += 1

    overlaps = []
    i = 0
    prev_count = None
    while i < len(mask):
        if mask[i] == 0:
            prev_count = 0
            i += 1
            continue
        count = mask[i]		#get counter
        start = i + low		#get new start

        while i < len(mask) and mask[i] == count:
            i += 1
        end = i + low		#get new end
        prev_count = count
        overlaps.append([start, end, count])
    return overlaps

out = self_overlap(inp)
for line in out:
    chrom, start, end, count = line
    print('{0}\t{1}\t{2}\t{3}'.format(chrom, start, end, count))
