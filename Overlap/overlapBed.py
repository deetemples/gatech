#!/usr/bin/env python3

import sys
import re
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i1", help="This is input file #1.")
parser.add_argument("-i2", help="This is input file #2.")
parser.add_argument("-m", help="This is the min overlap (MUST BE INT).")
parser.add_argument("-j", action='store_true', help="This joins the two entries.")
parser.add_argument("-o", help="This is the output file.")
arg = parser.parse_args()

if arg.m:
    m = float(arg.m)/100    #make m a decimal
output = ""
with open(arg.i1) as file1:
    with open(arg.i2) as file2:
        l1 = file1.readlines()
        l2 = file2.readlines()

        matchLine = 0   #starting range for inner file
        startLine = 0   #starting range for outer file
        for i in range(startLine, len(l1), 1):  #iterate through whole TE.bed
            set1 = l1[i].rstrip('\n').split('\t')   #split by tab & remove new line
            start_one, stop_one = set1[1:3] #get start and stop position
            start_one, stop_one = int(start_one), int(stop_one) #convert start & stop to int
            #print('###LINE: ' + str(i))
            for j in range(matchLine, len(l2), 1):  #iterate through line of last match and length of Intron.bed
                set2 = l2[j].rstrip('\n').split('\t')   #split by tab & remove new line
                start_two, stop_two = set2[1:3] #get start & stop position
                start_two, stop_two = int(start_two), int(stop_two) #convert start & stop to int
                total_num = (stop_two) - (start_two)    #total length of segment2
                chr1, chr2 = str(set1[0]), str(set2[0]) #get chr name of each file
                if (chr1 != chr2):
                    matchLine += 1  #if chr name not the same, move one line in Intron
                    break
                min_num = min(stop_one, stop_two) #get min stop
                max_num = max(start_one, start_two)   #get max stop
                num_of_overlap = int(min_num - max_num) #number of overlap between two lines
                if (start_one < start_two) and (stop_one < stop_two) and (num_of_overlap < 0):
                    break
                if num_of_overlap > 0:
                    matchLine = j-5 #provide a buffer
                if total_num != 0:
                    percentage = num_of_overlap / total_num #get percentage overlap
                if percentage >= m:  #if percentage is greater than or equal to set min overlap
                        matchLine = j-10 #provide a buffer
                        if arg.j:
                            output += ' '.join(map(str, set1)) + '\t' + ' '.join(map(str, set2)) + '\n' #join option
                        else:
                            output += ' '.join(map(str, set1)) + '\n'
                            break
        with open(arg.o, 'w') as final_out:
            final_out.write(output[:-1])    #get rid of extra newline
