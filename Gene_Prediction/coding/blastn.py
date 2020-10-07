"""
Run BLASTn for each union_fna file against
custom BLAST database.
   
    created by: Danielle Temples
    edited by: Paarth Parekh
    last edited: 03/19/2020
    
"""

#!/usr/bin/python3
import os, subprocess

def blastn_script(input_path, input_file_folder, output_path,run_tool):
    #input_path = the folder that the fna files (ex: union_fna,genemarks2)
    #input_file = the specific file number in the folders (ex: CGT2049, CGT2211)
    #output_path = path where the blast output folder will be
    if run_tool==3:
        #input_file = the specific file that correlates to the input file (ex: CGT2049_union.fna)
        input_file = input_path+"/"+input_file_folder
    else:
        input_file=input_path+"/"+input_file_folder+"/"+input_file_folder+"__nucleotide.fnn"
    #output_folder= the folder that the known/unknown files will be placed in (folder in input_path named kn_union_fna/faa)
    output_folder = output_path+"/blast/"
    output_file = output_folder+input_file_folder+"_blast"

    if "totaldb.fna.nhr" not in os.listdir("./total_campylobacter/"):       #if no database exists in blast database directory
        print("BLAST database does not exists in specified directory, Making a new blast database")
        subprocess.call(["makeblastdb", "-in","./total_campylobacter/totaldb.fna ","-dbtype nucl"])
        #blast_db = the location of the blast custom database
        blast_db ="./total_campylobacter/totaldb.fna"
    else:
        #blast_db = the location of the blast custom database
        blast_db ="./total_campylobacter/totaldb.fna "
    
    if "blast" in os.listdir(output_path):    #if blast folder already exists in output path
        if output_file in os.listdir(output_folder):  #if CGT2049_union.fna_blast already exists in blast output folder
            print("Output Directory {} contains file. Please delete it before running BLASTn for the same file".format(output_folder))
            return False
        else:
            try:
                print("Running blast for {} to seperate known and unknown genes".format(input_file))
                subprocess.call(["blastn", "-db", blast_db, "-query", input_file, "-out", output_file, "-max_hsps", "1", "-max_target_seqs", "1", "-outfmt", "6", "-perc_identity", "100", "-num_threads", "5"])
            except subprocess.CalledProcessError:
                print("Error running Blast for {}".format(input_file))
                return False
    else:
        os.mkdir(output_folder)
        try:
            print("Running blast for {} to seperate known and unknown genes".format(input_file))
            subprocess.call(["blastn", "-db", blast_db, "-query", input_file, "-out", output_file, "-max_hsps", "1", "-max_target_seqs", "1", "-outfmt", "6", "-perc_identity", "100", "-num_threads", "5"])
        except subprocess.CalledProcessError:
            print("Error running Blast for {}".format(input_file))
            return False
if __name__=="__main__":
    pass
