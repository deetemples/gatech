"""
Merge GM-S2 and Prodigal gene prediction gff (union) and create subsequent 
union .fna and .faa files
    
    created by: Kara Keun Lee
    edited by: Paarth Parekh
    last edited: 03/17/2020
"""

#!/usr/bin/python3
import os
import subprocess as sp
import shutil


def merge_predict(input_gms2_path,input_prod_path,input_contig_path1,output_folder,input_contig_path2=None):
    # check the paths to directories provided contain prediction files and contig files:
    if not os.listdir(input_gms2_path) :
        print("There are no Genemark-S2 gff files in the given directory path. Please check and try again.")
        return False
    if not os.listdir(input_prod_path) :
        print("There are no Prodigal gff files in the given directory path. Please check and try again.")
        return False
    if not os.listdir(input_contig_path1) :
        print("There are no assembled contig fasta files in the given directory path. Please check and try again.")
        return False
    if input_contig_path2!= None:
        if not os.listdir(input_contig_path2) :
            print("There are no assembled contig fasta files in the given directory path. Please check and try again.")
            return False
    
    # check if output directories exist:
        # Yes --> empty the output directories for the new run
        # No --> make 3 new union output directories 
    
    # union gff
    u_gff_folder=output_folder+"/union_gff"    
    if os.path.exists(u_gff_folder) == False:
        os.mkdir(u_gff_folder)
    else:
        if os.listdir(u_gff_folder):
            print("Output gff folder exists please delete the files before continuing")
            return False
    
    # union fna
    u_fna_folder=output_folder+"/union_fna"    
    if os.path.exists(u_fna_folder) == False:
        os.mkdir(u_fna_folder)
    else:
        if os.listdir(u_fna_folder):
            print("Output fna folder exists please delete the files before continuing")
            return False
    
    # union faa 
    u_faa_folder=output_folder+"/union_faa"    
    if os.path.exists(u_faa_folder) == False:
        os.mkdir(u_faa_folder)
    else:
        if os.listdir(u_faa_folder):
            print("Output faa folder exists please delete the files before continuing")
            return False
    
    # Temporary folder to store merge files in and delete them later on
    temp_folder=output_folder+"/temp/"
    if os.path.exists(temp_folder) == False:
        os.mkdir(temp_folder)
    else:
        shutil.rmtree(temp_folder)
        os.mkdir(temp_folder)
    
    # Contig copy path
    contig_copied=output_folder+"/contigs_copied/"
    
    # if contig folder exists then delete it. 
    if os.path.exists(contig_copied) == True:
        shutil.rmtree(contig_copied)

    shutil.copytree(input_contig_path1,contig_copied)
    if input_contig_path2!=None:
        shutil.copytree(input_contig_path2,contig_copied)
    
    for sample in os.listdir(input_gms2_path):
        # specify paths & formats:
        gms2_gff=input_gms2_path+sample+"/"+sample+"_output.gff"
        prod_gff=input_prod_path+sample+"/"+sample+"_output.gff"
        if sample in os.listdir(contig_copied):
            contig_file=contig_copied+sample+"/contigs.fasta"
        else:
            print("{} not present in either of the directories mentioned".format(sample))
            continue

        intersect1_gff=temp_folder+sample+"_1.txt"
        intersect2_gff=temp_folder+sample+"_2.txt"
        intersect3_gff=temp_folder+sample+"_3.txt"
        union_gff=output_folder+"/union_gff/"+sample+"_union.gff"
        union_fna=output_folder+"/union_fna/"+sample+"_union.fna"
        union_faa=output_folder+"/union_faa/"+sample+"_union.faa"


        # generate 3 parts of the union using bedtools intersect:
        sp.call("bedtools intersect -a "+gms2_gff+" -b "+prod_gff+" -wa -v -f 1.0 -r >> " +intersect1_gff,shell=True)
        sp.call("bedtools intersect -b "+gms2_gff+" -a "+prod_gff+" -wa -v -f 1.0 -r >> "+intersect2_gff,shell=True)
        sp.call("bedtools intersect -a "+gms2_gff+" -b "+prod_gff+" -f 1.0 -r >> "+intersect3_gff,shell=True)
        # combine all resulting intersections for union gff:
        sp.call("cat "+intersect1_gff+" "+intersect2_gff+" "+intersect3_gff+" >> "+union_gff,shell=True)
        # remove temporary directory with intersect files:
        # generate union fna files for blasting using union gff:
        sp.call(["samtools","faidx",contig_file])
        sp.call(["bedtools","getfasta","-fi",contig_file,"-bed",union_gff,"-fo",union_fna])
        # generate union faa files, maintain header format:
        print("Running transeq for {} to convert into protein sequence".format(union_fna))
        sp.call("transeq "+union_fna+" -sformat pearson -trim -clean -outseq "+union_faa,shell=True)
        sub = sp.call(["sed", "-i" ,'s/_[^_]*$//',union_faa])

        
    shutil.rmtree(temp_folder)
    shutil.rmtree(contig_copied)
    shutil.rmtree(input_gms2_path)
    shutil.rmtree(input_prod_path)
    return True
if __name__=="__main__":
    pass
