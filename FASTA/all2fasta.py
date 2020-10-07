#!/usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="This is the input file.")
parser.add_argument("-f", help="This is the fold length.")
arg = parser.parse_args()
if arg.i :
	file = arg.i
if arg.f :
	fold = int(arg.f)
else:
	fold = 70	#default fold length is 70
infile = open(file, "r")
## list of lines in the file
lines = infile.readlines()
firstLine = lines[0]

## initialize FASTA vars
id = []
desc = []
seq = []

## EMBL
if firstLine.startswith("ID"):
	for i in range(len(lines)):
		if (re.match('AC',lines[i])):
			contents = lines[i].split(" ")
			id += [contents[3].strip()]		#removes AC & add to id variable
		elif (re.match('DE', lines[i])):
			contents = lines[i].strip()
			desc += [contents[5:]]			#removes DE & add to desc variable
		elif lines[i].startswith('SQ'):
			stuff = lines[i + 1: len(lines) - 1]	#stops before "//" at the end
			plain = ""
			for s in stuff:
				theStuff = s.split(" ")		#split contents by space
				for thing in theStuff:
					if (len(thing.strip()) > 0 and thing.strip().isalpha()):	#actually contains alphabetical material
						plain += thing.strip().upper()	#strip spaces & make all uppercase
			seq += [plain]	#add to seq variable
	infile.close()

## GB
elif firstLine.startswith("LOCUS"):
	for i in range(len(lines)):
		if (re.match('ACCESSION',lines[i])):
			contents = lines[i].split(" ")
			id += [contents[3].strip()]		#removes ACCESSION & add to id variable
		elif (re.match('DEFINITION', lines[i])):
			contents = lines[i].strip()
			desc += [contents[12:]]			#removes DEFINITION & add to id variable
		elif lines[i].startswith('ORIGIN'):
			stuff = lines[i + 1: len(lines) - 1]	#stops before "//" at the end
			plain = ""
			for s in stuff:
				theStuff = s.split(" ")
				for thing in theStuff:
					if (len(thing.strip()) > 0 and thing.strip().isalpha()):	#actually contains alphabetical material
						plain += thing.strip().upper()	#strip spaces & make all uppercase
			seq += [plain]	#add to seq variable
	infile.close()

## FASTQ
elif firstLine.startswith("@"):
	for i in range(len(lines)):
		if (re.match('@', lines[i])):
			contents = lines[i]
			id += [contents[1:].strip()]	#removes @ & add to id variable
			desc = " "	#empty description
			plain = ""
			stuff = lines[i: i+3]	#seq for each file ID
			for s in stuff:
				if (len(s.strip()) > 0 and s.strip().isalpha()):	#actually contains alphabetical material
					plain += s.strip().upper()	#strip spaces & make all uppercase
			seq += [plain]

	infile.close()

## MEGA
elif firstLine.startswith("#"):
	for i in range(1, len(lines)):
		if (re.match("#", lines[i])):
			contents = lines[i]
			id += [contents[1:].strip()]	#removes # & add to id variable
			desc = " "
			stuff = lines[i: len(lines)]	#seq for file ID
			plain = ""
			for s in stuff:
				if (len(s.strip()) > 0 and s.strip().isalpha()):	#actually contains alphabetical material
					plain += s.strip().upper()	strip spaces & make all uppercase
			seq += [plain]
	infile.close()

## EXTENSION fna OR faa
for i in range(len(id)):
	theSeq = str(seq[i])
	regex = re.compile('[ACGTNacgtn]')
	if regex.findall(theSeq):	#if seq contains only those letters
		outfile = open(file + ".fna", "w")
	else :	#if seq contains chars outside those
		outfile = open(file + ".faa", "w")

## SET FOLD
for i in range(len(id)):
	outfile.write(">" + id[i] + " ")	#header line
	outfile.write(desc[0] + "\n")	#header line
	theSeq = str(seq[i])
	counter = 0
	for j in range(len(theSeq)):
		if counter == fold :
			counter = 0
			outfile.write("\n")		#print newline if fold is reached
		outfile.write(theSeq[j])
		counter +=1		#increment to fold value
	outfile.write("\n")
outfile.close()
