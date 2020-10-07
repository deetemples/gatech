"""
Mark union_fna/faa files with KNOWN (K) or UNKNOWN (U) according to hits in
its corresponding blast file.
    created by: Danielle Temples
    edited by: Paarth Parekh
    last edited: 03/19/2020
    
"""

#!/usr/bin/python
import os, subprocess

def rename(union_input_path, blast_input_path, input_file, output_path,type_of_file):
    #blast_input_path = the folder that the formatted blast files are in (ex: blast/formatted_)
    #union_input_path = the folder that the union files are in (ex: union_faa, union_fna)
    #input_file = the specific file number in the folders (ex: CGT2049, CGT2211)
    #type = faa or fna
    #blast_input_file = the specific blast file that correlates to the input file (ex: CGT2049_union.fna_blast)
    blast_input_file = blast_input_path+"/"+input_file+"_union.fna_blast"
    #union_input_file = the specific union file that correlates to the input file (ex: CGT2049_union.fna/faa)
    union_input_file = union_input_path+"/"+input_file+"_union."+type_of_file
    #output_folder= the folder that the known/unknown files will be placed in (folder in input_path named kn_union_fna/faa)
    output_folder = output_path+"known_unknown_"+type_of_file+"/"
    #output_file = the ku file in the ku folder under the union folders (ex: known_unknown_faa/CGT2049_union.faa)
    #output_file = output_folder+"/"+input_file+"_union."+type

    if input_file+"_union."+type_of_file not in os.listdir(union_input_path):       #if CGT2049_union.fna/faa does not exist in union_fna/faa
        print("Union Directory does not contain inputted union file {}. Please check before running tool for same file").format(union_input_file)
        return False
    if input_file+"_union.fna_blast" not in os.listdir(blast_input_path):       #if CGT2049_union.fna_blast does not exist in blast directory
        print("Blast Directory does not contain corresponding file to union file {}. Please check before running tool for same file").format(blast_input_file)
        return False

    if "known_unknown_"+type_of_file in os.listdir(output_path):    #if known_unknown_(faa or fna) already exists in output_folder/fna folder
        if input_file+"_union."+type_of_file in os.listdir(output_folder):  #if CGT2049_union.faa/fna already exists in output_folder/fna folder
            print("Output Directory {} contains file. Please delete it before running the tool for the same file").format(output_folder)
            return False
        else:
            output_file = output_folder+input_file+"_union."+type_of_file   #make file in known_unknown_fna/faa folder called CGT2049_union.faa/fna
            subprocess.call("cp "+union_input_file+" "+ output_file,shell=True)  #copy contents from input file to output file (union_faa/CGT2049_union.faa -> output_folder/known_unknown_faa/CGT_union_faa)
    else:
        os.mkdir(output_folder)     #make ku_union_fna/faa folder if it does not exist
        output_file = output_folder+input_file+"_union."+type_of_file   #make file in known_unknown_fna/faa folder called CGT2049_union.faa/fna
        subprocess.call("cp "+union_input_file+" "+output_file,shell=True)  #copy contents from input file to output file (union_faa/CGT2049_union.faa -> output_folder/known_unknown_faa/CGT_union_faa)

    original = open(output_file, 'r').readlines()
    hits = open(blast_input_file, 'r').readlines()
    data = []
    for line in hits:
            data.append(line.split('\t')[0])
    write_output=open(output_file,"w")
    for l in original:
            if l.startswith(">"):
                    #print("header")
                    match = l.split(">")[1]
                    match=match.strip("\n")
                    #print(match)
                    if match in data:
                            l=l.strip("\n")
                            write_output.write(l + " K".format(1)+"\n")
                            #print("known")
                    else:
                            l=l.strip("\n")
                            write_output.write(l + " U".format(1)+"\n")
                            #print("unknown")a
            else:
                    write_output.write(l)
    write_output.close()
    return True

if __name__=="__main__":
    pass


