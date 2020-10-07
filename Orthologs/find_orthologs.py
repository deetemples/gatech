#!/usr/bin/env python3
import os
import subprocess
import argparse
'''
Script for finding orthologs using reciprocal BLAST hits.

You may choose to import any of the other allowed modules.

You have to write an argparse for getting command line arguments. The usage for
this script is:
    ./find_orthologs.py -i1 <Input file 1> -i2 <Input file 2> -o <Output file name> –t <Sequence type – n/p>

where "n" specifies a nucleotide sequence and "p" specifies a protein sequence.
'''

def main():
    '''
    This is the main function.
    '''

    '''
    Insert argparse code that populates the following variables
     - file_one
     - file_two
     - output_file
     - input_sequence_type
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-i1", help="This is the first input file.")		#sets first input file to flag -i1
    parser.add_argument("-i2", help="This is the second input file.")		#sets second input file to flag -i2
    parser.add_argument("-o", help="This is the output file name.")		#sets output file name to flag -o
    parser.add_argument("-t", help="This is the input sequence type.")		#sets input sequence type to flag -t
    arg = parser.parse_args()
    if arg.i1 :
        file_one = arg.i1		#sets -i1 arg to variable file_one
    if arg.i2 :
        file_two = arg.i2		#sets -i2 arg to variable file_two
    if arg.o :
        output_file = arg.o		#sets -o arg to variable output_file
    if arg.t :
        input_sequence_type = arg.t	#sets -t arg to variable input_sequence_type

	
    '''
    output_list is a list of reciprocal BLAST hits. Each element is a tab
    separated pair of gene names. Eg:
    ["lcl|AM421808.1_cds_CAM09336.1_10  lcl|AE002098.2_cds_NMB0033_33", "lcl|AM421808.1_cds_CAM09337.1_11       lcl|AE002098.2_cds_NMB0034_34", "lcl|AM421808.1_cds_CAM09338.1_12       lcl|AE002098.2_cds_NMB0035_35", "lcl|AM421808.1_cds_CAM09339.1_13       lcl|AE002098.2_cds_NMB0036_36", ...]
    '''
    output_list = get_reciprocal_hits(file_one, file_two, input_sequence_type)
    with open(output_file, 'w') as output_fh:
        for ortholog_pair in output_list:
            output_fh.write(ortholog_pair +"\n")

    os.remove("./file_one_db.nhr")		#removes temporary files
    os.remove("./file_one_db.nin")
    os.remove("./file_one_db.nsq")
    os.remove("./file_two_db.nhr")
    os.remove("./file_two_db.nin")
    os.remove("./file_two_db.nsq")
    os.remove("./f1_f2db.tab")
    os.remove("./f2_f1db.tab")

def get_reciprocal_hits(file_one, file_two, input_sequence_type):
    if input_sequence_type == "n" :		
        input_sequence_type = "nucl"		#changes "n" input to "nucl" for makeblastdb to understand
    if input_sequence_type == "p" :
        input_sequence_type = "prot"		#changes "p" input to "prot" for makeblastdb to understand
    if input_sequence_type == "nucl" :
        blast_type = "blastn"			#calls blastn if input sequence type is "nucl"
    if input_sequence_type == "prot" :
        blast_type = "blastp"			#calls blastp if input sequence type is "prot"

    subprocess.call(["makeblastdb", "-in", file_one, "-dbtype", input_sequence_type, "-out", "file_one_db"])		#makes db for file one
    subprocess.call(["makeblastdb", "-in", file_two, "-dbtype", input_sequence_type, "-out", "file_two_db"])		#makes db for file two
    subprocess.call([blast_type, "-query", file_one, "-db", "file_two_db", "-outfmt", "6", "-out", "f1_f2db.tab", "-num_alignments", "1"])  #blast for file one on file 2 db
    subprocess.call([blast_type, "-query", file_two, "-db", "file_one_db", "-outfmt", "6", "-out", "f2_f1db.tab", "-num_alignments", "1"])  #blast for file 2 on file one db
        
    orthologs = {}				#create empty orthologs dict
    f1 = open("f1_f2db.tab", "r")		#open & read file
    f1_dict={}					#create empty f1 dict
    for line in f1:
        columns = line.strip().split("\t")	#strip whitespace and split with tab for each line
        query = columns[0]			#query ID = first column
        subject = columns[1]			#subject ID = second column
        f1_dict[query] = subject		#query = keys; subject = values

    f2 = open("f2_f1db.tab", "r")		#open & read file
    f2_dict={}					#create empty f2 dict
    for line in f2:
        columns = line.strip().split("\t")	#strip whitespace and split with tab for each line
        query = columns[0]			#query ID = first column
        subject = columns[1]			#subject ID = second column
        f2_dict[query] = subject 		#query = keys; subject = values
       
    for id in f2_dict.keys():			#iterate through the keys in f2_dict
        v = f2_dict[id]				#v = values of f2_dict
        if ( v in f1_dict.keys() ):		#if values in f2_dict is in keys in f1_dict
            if ( id == f1_dict[v] ):		#if values in f1_dict = keys in f2_dict
                orthologs[id] = v		

    pairs = []					#create empty list
    for k in orthologs.keys():			#iterate through the keys in orthologs
        pairs.append(k + '\t'+ orthologs[k])	#append key and value from orthologs to list and separate with tab
    pairs = [x.strip(' ') for x in pairs]	#strip whitespace
    return pairs



if __name__ == "__main__":
    main()