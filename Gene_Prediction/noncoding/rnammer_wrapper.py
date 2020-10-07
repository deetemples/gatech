#!/usr/bin/python3
import os,subprocess

def rnammer_script(input_path,assembly_file,output_folder_path,name):
    #Get the contigs file from all the different assemblies generated
    #input= input_path is the folder in which different contigs are kept example:21,33,55,77 and assembly_file is the actual folder i.e CGT2049. name just takes those contigs files 
    assembly_input=input_path+assembly_file+"/"+name
    #output_tool is the folder it will create in the output_folder_path based on the tool which is running
    output_tool=output_folder_path+"/rnammer/"
    #output_folder_path is the folder in which the output folders will be generated in. It will check whether those folders are present or will generate them. 
    output_folder=output_tool+assembly_file
    if "rnammer" in os.listdir(output_folder_path):
        if assembly_file in os.listdir(output_tool):
            if not len(os.listdir(output_folder)) == 0:
                print("Output Directory {} contains files,please delete them before running the tool for the same file".format(output_folder))
                return False
        else:
            os.mkdir(output_folder)
    else:
        os.mkdir(output_tool)
        os.mkdir(output_folder)
    #each output folder generated will have three sequences which will be produced.
    output_gff=output_folder+"/"+assembly_file+"_output.gff"
    try:
        print("Running RNAmmer for:" ,assembly_file)
            #RNAmmer running with genome-type bacteria
        bash_output=subprocess.check_output(["rnammer", "-S", "bac", "-m", "lsu,ssu,tsu", "-multi", "-gff", "rRNA.gff ", assembly_input])
        bash_output=subprocess.check_output(["perl","./convert_codes/convert_RNAmmer_to_gff3.pl", "--input", "rRNA.gff >", output_gff])


    except subprocess.CalledProcessError:
        print("Error running RNAmmer please check the installation and files ")
        return False
    print("Completed running RNAmmer for",assembly_file)
    return True

if __name__=="__main__":
    pass
    #rnammer_script  
