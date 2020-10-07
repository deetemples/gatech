#!/usr/bin/python3
import os,subprocess

def genemarks2_script(input_path,assembly_file,output_folder_path,type_species,name):
    #Get the contigs file from all the different assemblies generated
    #input= input_path is the folder in which different contigs are kept example:21,33,55,77 and assembly_file is the actual folder i.e CGT2049. name just takes those contigs files 
    assembly_input=input_path+assembly_file+"/"+name
    #output_tool is the folder it will create in the output_folder_path based on the tool which is running
    output_tool=output_folder_path+"/genemarks2/"
    #output_folder_path is the folder in which the output folders will be generated in. It will check whether those folders are present or will generate them. 
    output_folder=output_tool+assembly_file
    if "genemarks2" in os.listdir(output_folder_path):
        if assembly_file in os.listdir(output_tool):
            if not len(os.listdir(output_folder)) == 0:
                print("Output Directory {} contains files,please delete them before running the tool for the same file".format(output_folder))
                return False
        else:
            os.mkdir(output_folder)
    else:
        os.mkdir(output_tool)
        os.mkdir(output_folder)
    #each output folder generated will have three sequences which will be produced, example file generate: output_folder_path/CGT2149/CGT2149_nucleotide.fnn
    output_nucleotide=output_folder+"/"+assembly_file+"_nucleotide.fnn"
    output_protein=output_folder+"/"+assembly_file+"_protein.faa"
    output_gff=output_folder+"/"+assembly_file+"_output.gff"
    try:
        print("Running GeneMarkS2 for:" ,assembly_file)
        if type_species=="bacteria":
            #GeneMarkS2 running with genome-type bacteria
            bash_output=subprocess.check_output(["gms2.pl", "--seq", assembly_input, "--genome-type", "bacteria", "--output", output_gff, "--format", "gff", "--fnn", output_nucleotide, "--faa", output_protein])
        else:
            bash_output=subprocess.check_output(["gms2.pl", "--seq", assembly_input, "--genome-type", "auto", "--output", output_gff, "--format", "gff", "--fnn", output_nucleotide, "--faa", output_protein])
    except subprocess.CalledProcessError:
        print("Error running GeneMarkS-2 please check the installation and files ")
        return False
    print("Completed running GeneMarkS-2 for",assembly_file)
    return True
if __name__=="__main__":
    pass
    #genemarks2_script  
