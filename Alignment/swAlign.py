#!/usr/bin/env python3
import sys

open_seq1 = open(sys.argv[1]).read()
seq2 = open_seq1.strip().split("\n",1)[1]
open_seq2 = open(sys.argv[2]).read()
seq1 = open_seq2.strip().split("\n",1)[1]
gap = -1	#set gap penalty to -1
match = 1	#set match penalty to +1 
mismatch = -1	#set mismatch penalty to -1

def zero_matrix(rows, cols) :	#make a matrix of all zeros
	empty = []
	for x in range(rows) :
		empty.append([])	#add empty list to each row
		for y in range(cols) :
			empty[-1].append(0)	#add 0 to each column in each row
	return empty

def penalty(base1, base2):	#determines penalty when bases are compared
    if base1 == base2:	#if bases are the same, return match penalty
        return match
    elif base1 == '-' or base2 == '-':	#if a base contains a -, return gap penalty
        return gap
    else:	#if bases are different, return mismatch penalty
        return mismatch

def smith(seq1, seq2) :
	len1 = len(seq2)	#get length of seq1
	len2 = len(seq1)	#get length of seq2
	max_value = 0
	score = zero_matrix(len2 + 1, len1 + 1)	#make matrix of zeros based on lengths of sequences
	
	for i in range(0, len2 + 1):	#iterates through length of seq2
		score[i][0] = gap * i	#fills first column (0, -1 * index of len2)
		if score[i][0] < 0 :	#replace negatives with 0
			score[i][0] = 0 
	for j in range(0, len1 + 1):	#iterates through length of seq1
		score[0][j] = gap * j	#fills first row (0, -1 * index of len1)
		if score[0][j] < 0 :	#replace negatives with 0
			score[0][j] = 0 
	for i in range(1, len2 + 1):	#fill out rest of matrix
		for j in range(1, len1 + 1):
			check_top = score[i - 1][j - 1] + penalty(seq2[j-1], seq1[i-1])	#checks cell at top & adds appropriate penalty
			check_left = score[i - 1][j] + gap	#checks cell at left & adds gap penalty
			check_diagonal = score[i][j - 1] + gap	#checks cell at diagonal & adds gap penalty
			score[i][j] = max(check_top, check_left, check_diagonal)	#takes max score from above possible scores
			if score[i][j] > max_value:	#find max score
				max_value = score[i][j]
				max_i = i	#find starting location
				max_j = j
			if score[i][j] < 0 :	#replace negatives with 0
				score[i][j] = 0 	

	#BEGIN BACKTRACK

	align1 = ""	#make empty align1 string
	align2 = ""	#make empty align2 string
	while score[max_i][max_j] != 0:	#loops while the value doesn't equal 0
		current_score = score[max_i][max_j]	#sets current score
		top = score[max_i][max_j-1]	#sets top score
		left = score[max_i-1][max_j]	#sets left score
		diagonal = score[max_i-1][max_j-1]	#sets diagonal score
	
		if current_score == diagonal + penalty(seq2[max_j-1], seq1[max_i-1]): #find which score the current score was calculated from
			align1 += seq2[max_j-1]	#add base to align1
			align2 += seq1[max_i-1]	#add base to align2
			max_i -= 1	#update position in score matrix
			max_j -= 1
		elif current_score == top + gap: #find which score the current score was calculated from
			align1 += seq2[lmax_j-1]	#add base to align1
			align2 += "-"	#add - to align2 to represent gap
			max_j -= 1	#update position in score matrix
		elif current_score == left + gap:	#find which score the current score was calculated from
			align1 += "-"	#add - to align1 to represent gap
			align2 += seq1[max_i-1]	#add base to align2
			max_i -= 1	#update position in score matrix
		else:
			break

	align1 = align1[::-1]	#reverse sequence
	align2 = align2[::-1]	#reverse sequence
	
	counter = 0	#counter for alignment score
	symbols = ""	#empty string for match (|), mismatch (*), gap (" ")
	u = zip(align1, align2)
	for a,b in u:
		if a==b:	#if letters in each alignment match
			counter += 1	#increase counter by 1
			symbols += "|"	#add match symbol to symbols
		elif a == '-' or b == '-':	#if letter in alignment equals "-"
			symbols += " "	#add gap symbol to symbols
			counter -= 1	#decrease counter by 1
		else :
			counter -= 1	#decrease counter by 1
			symbols += "*"	#add mismatch symbol to symbols
	return (align2, symbols, align1, str(counter))

output1, output2, output3, output4 = smith(seq1, seq2)
print(output3 + "\n" + output2 + "\n" + output1 +"\nAlignment score: " + output4)