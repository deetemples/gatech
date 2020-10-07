"""
Mark union_gff files with KNOWN (K) or UNKNOWN (U) according to hits in
its corresponding blast file.
    created by: Danielle Temples
    edited by: Paarth Parekh
    last edited: 03/19/2020
    
"""

#!/usr/bin/python
import os, subprocess

def rename_gff(union_input_path, blast_input_path, input_file, output_path):
    #blast_input_path = the folder that the formatted blast files are in (ex: blast/formatted_)
    #union_input_path = the folder that the union gff files are in (ex: union_gff)
    #input_file = the specific file number in the folders (ex: CGT2049, CGT2211)
    #blast_input_file = the specific blast file that correlates to the input file (ex: CGT2049_union.fna_blast)
    blast_input_file = blast_input_path+"/"+input_file+"_union.fna_blast"
    #union_input_file = the specific union file that correlates to the input file (ex: CGT2049_union.fna/faa)
    union_input_file = union_input_path+"/"+input_file+"_union.gff"
    #output_folder= the folder that the known/unknown files will be placed in (folder in input_path named kn_union_fna/faa)
    output_folder = output_path+"known_unknown_gff/"

    if input_file+"_union.gff" not in os.listdir(union_input_path):     #if CGT2049_union.gff does not exist in union_gff
        print("Union Directory does not contain inputted union gff file {}. Please check before running tool for same file").format(input_file+"_union.gff")
        return False
    if input_file+"_union.fna_blast" not in os.listdir(blast_input_path):     #if CGT2049_union.fna_blast does not exist in blast directory
        print("Blast Directory does not contain corresponding file to union file {}. Please check before running tool for same file").format(input_file+"_union.gff")
        return False

    if "known_unknown_gff" in os.listdir(output_path):    #if ku_union_gff already exists in union_gff
        if input_file+"_union.gff" in os.listdir(output_folder):  #if CGT2049_union.gff already exists in ku_union_gff
            print("Output Directory {} contains file. Please delete it before running the tool for the same file").format(output_folder)
            return False
        else:
            output_file = output_folder+input_file+"_union.gff"   #make file in known_unknown_gff folder called CGT2049_union.gff
            subprocess.call("cp "+union_input_file+" "+ output_file,shell=True)      #copy contents from input file to output file (union_gff/CGT2049_union.gff -> output_folder/known_unknown_gff/CGT_union_gff)
    else:
        os.mkdir(output_folder)     #make known_unknown_gff folder if it does not exist
        output_file = output_folder+input_file+"_union.gff"   #make file in known_unknown_gff folder called CGT2049_union.gff
        subprocess.call("cp "+union_input_file+" "+ output_file,shell=True)      #copy contents from input file to output file (union_gff/CGT2049_union.gff -> output_folder/known_unknown_gff/CGT_union_gff)

    original = open(output_file, 'r').readlines()
    hits = open(blast_input_file, 'r').readlines()
    match = []
    start = []
    stop = []
    write_output=open(output_file,"w")
    for l in hits:
            tabbed_line = l.split('\t')
            before = tabbed_line[0]
            match.append(before.partition(":")[0])
            start.append(before[before.find(":")+1:before.find("-")])
            stop.append(before[before.find("-")+1:])
    for line in original:
            data = line.split('\t')[0]
            num1 = line.split('\t')[3]
            num2 = line.split('\t')[4]
            if data in match and num1 in start and num2 in stop:
                    write_output.write(line.replace("\t", " K" + "\t", 1))
            else:
                    write_output.write(line.replace("\t", " U" + "\t", 1))
    write_output.close()
    return True
if __name__=="__main__":
    pass
