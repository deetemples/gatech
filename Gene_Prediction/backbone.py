#!/usr/bin/env python
import argparse
import os
import subprocess
import shutil
from coding.genemarks2_wrapper import genemarks2_script
from coding.prodigal_wrapper import prodigal_script
from coding.union_outputs import merge_predict
from coding.blastn import blastn_script
from coding.rename_faa_fna import rename
from coding.rename_gff import rename_gff
from noncoding.infernal_wrapper import infernal_script
from noncoding.aragorn_wrapper import aragorn_script
from noncoding.rnammer_wrapper import rnammer_script
from noncoding.ncRNA_merge import ncRNA_merge_output

#############################################################################################################################################################################################
############################### https://stackoverflow.com/questions/3853722/python-argparse-how-to-insert-newline-in-the-help-text/22157136#22157136 ########################################

# Helps to format the argparse options
class SmartFormatter(argparse.HelpFormatter):

    def _split_lines(self, text, width):
        if text.startswith('R|'):
            return text[2:].splitlines()
        # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(self, text, width)


#############################################################################################################################################################################################

#Check if the tool which needs to be run is present or not
def check_tools(run_tool):
    tools_to_run=[]
    if(run_tool==1):
        tools_to_run.append("gms2.pl")
    elif(run_tool==2):
        tools_to_run.append("prodigal")
    else:
        #bedtools, samtools and transeq are the tools needed to merge the results hence are needed to be called
        tools_to_run.extend(["gms2.pl","prodigal","bedtools"])
    #print(tools_to_run)
    for tools in tools_to_run:

        try:
            #Calling the genemarks2,prodigal or both by name.
            bash_output = subprocess.check_output([tools])
        except (FileNotFoundError, subprocess.CalledProcessError) as error:
            print("The tool {}, was not present on the system. Please check again".format(tools))
            return False
        print("{} is present".format(tools))
    return True


#################################################################################################################################################################################################

#check whether input files folder is present and not empty or not
def check_input(folder_name):
    if os.path.isdir(folder_name):
        if len(os.listdir(folder_name))!=0:
            print("The folder {} is not empty".format(folder_name))
            return True
        else:
            print("The folder {} is empty".format(folder_name))
            return False
    else:
        print("The folder {} is not present".format(folder_name))
        return False


##############################################################################################################################################################################################

# Running GeneMarkS-2 and/or Prodigal based on the options given by the user, it takes in the input path to the files, output path, type of the species( either bacteria or auto for genemarks-2) and which tool to run or both to run
def running_tools(input_path,output_path,type_species,run_tool,name="contigs.fasta"):
    list_of_files=[]
    #List all the directories present in the input path, where the wrapper goes into those directories and runs the contigs files
    #print(os.listdir(input_path))
    for folder in sorted(os.listdir(input_path)):
       list_of_files.append(folder)
       #print(folder)
       if (run_tool==1 or run_tool==3):
           genemarks2_output=genemarks2_script(input_path,folder,output_path,type_species,name)
           if genemarks2_output == False:
                return False
       if(run_tool==2 or run_tool==3):
            prodigal_output=prodigal_script(input_path,folder,output_path,name)
            if prodigal_output == False:
                return False
    return True,list_of_files


############################################################################################################################################################################################

# Blast validation function
def blast_results(run_tool,out):

    #Checks if gene_marks2 is called or prodigal or the union of both
    if run_tool==1:
        #Sets the genemarks2 generated output to be the input to be given to the blast script
        genemarks2_output=out+"/genemarks2/"
        #Lists all the files in the genemarks2 output directory
        for folder_file in os.listdir(genemarks2_output):
            #Runs the blast script
            blast_out_genemarks2=blastn_script(genemarks2_output, folder_file, out,run_tool)
            if blast_out_genemarks2 == False:
                return False

    #Same if only prodigal is called
    elif run_tool==2:
        prodigal_output=out+"/prodigal/"
        for folder_file in os.listdir(prodigal_output):
            blast_out_prodigal=blastn_script(prodigal_output,folder_file, out,run_tool)
            if blast_out_prodigal == False:
                return False

    #Same if both the tools are called and the merge results are obtained
    else:
        union_input_path=out+"/merge_out/union_fna"
        for folder_file in os.listdir(union_input_path):
            blast_out=blastn_script(union_input_path ,folder_file, out,run_tool)
            if blast_out == False:
                return False
    return True


#################################################################################################################################################################################################

# Run the rename script to generate output files with known and unknown genes 
def rename_scripts(list_of_files,out,run_tool):
    blast_input_path=out+"blast"

    #Checks if gene_marks2 is called or prodigal or the union of both
    if run_tool==1:
        for files in list_of_files:

            genemarks2_output=out+"/genemarks2/"+files
            condition=rename(genemarks2_output,blast_input_path,files, out,"fna",run_tool)
            if condition == False:
                return False
            condition=rename(genemarks2_output, blast_input_path, files, out,"faa",run_tool)
            if not condition:
                return False
            condition=rename_gff(genemarks2_output,blast_input_path,files,out,run_tool)
            if not condition:
                return False

        genemarks2_output=out+"/genemarks2/"
        shutil.rmtree(genemarks2_output)

    #Same if only prodigal is called
    elif run_tool==2:
        for files in list_of_files:

            prodigal_output=out+"/prodigal/"+files
            condition=rename(prodigal_output,blast_input_path,files, out,"fna",run_tool)
            if condition == False:
                return False
            condition=rename(prodigal_output, blast_input_path, files, out,"faa",run_tool)
            if not condition:
                return False
            condition=rename_gff(prodigal_output,blast_input_path,files,out,run_tool)
            if not condition:
                return False

        prodigal_output=out+"/prodigal/"
        shutil.rmtree(prodigal_output)
            
    #Same if both the tools are called and the merge results are obtained
    else:
        union_path_fna=out+"/merge_out/union_fna"
        union_path_faa=out+"/merge_out/union_faa"
        union_path_gff=out+"/merge_out/union_gff"

        for files in list_of_files:
            condition=rename(union_path_fna, blast_input_path, files, out, "fna",run_tool)
            if not condition:
                return False
            condition=rename(union_path_faa, blast_input_path, files, out,"faa",run_tool)
            if not condition:
                return False
            condition=rename_gff(union_path_gff,blast_input_path,files,out,run_tool)
            if not condition:
                return False

        shutil.rmtree(union_path_fna)
        shutil.rmtree(union_path_faa)
        shutil.rmtree(union_path_gff)


    shutil.rmtree(blast_input_path)
    return True


#################################################################################################################################################################################################

# Running Infernal or Inferal, Aragon and Rnammer based on the options given by the user, it takes in the input path to the files, output path
def noncoding_run(input_path,output_path,run_tool,flag,name="contigs.fasta"):
    #List all the directories present in the input path, where the wrapper goes into those directories and runs the contigs files
    for folder in sorted(os.listdir(input_path)):
       #print(folder)
        if (run_tool==1 or run_tool==2):
            infernal_output=infernal_script(input_path,folder,output_path,type_species,name)
            if infernal_output == False:
                return False
        if(run_tool==2):
            rnammer_output=rnammer_script(input_path,folder,output_path,name)
            aragon_output=aragon_script(input_path,folder,output_path,name)
            if rnammer_output == False or aragon_output == False:
                return False
    return True
#################################################################################################################################################################################################

######## main of the script which takes in the input ###################################### 

def main():


    ################################# User Input ######################################################################
    parser = argparse.ArgumentParser(description="Backbone script",formatter_class=SmartFormatter)

    parser.add_argument("-io","--input-option",default=1,help="R|Default Option is 1, options available\n"
    "1 Take input from the genome assembly results \n"
    "2 Input your own assembly files")
    parser.add_argument("-nc", "--name-contigs", default="contigs.fasta" ,help="Name of the contig files,called when option 2 for input-option is selected, default considered is contigs.fasta",required=False)
    parser.add_argument("-ia", "--input-assembly", help="Path to the directory that contains input file manually,called when option 2 for input-option is selected",required=False)
    parser.add_argument("-if77", "--input-files77", help="Path to the directory that contains input file for spades output of 21,33,55,77, called when default option for input-option is selected",required=False)
    parser.add_argument("-if99", "--input-files99", help="Path to the directory that contains input file for spades output of 21,33,55,77,99,127,called when default option for input-option is selected",required=False)
    parser.add_argument("-go", "--gene-output", help="Path to a directory that will store the output gff files, fna files and faa files.", required=True)
    parser.add_argument("-tr","--coding-tools",default=3,help="R|Default Option is 3, options available to run are\n"
    "1 Only GeneMarkS-2 \n"
    "2 Only Prodigal \n"
    "3 Both and getting a union of the genes")
    parser.add_argument("-ts", "--type-species", help="if running Gene_MarkS-2, mention species to be either bacteria or auto")
    parser.add_argument("-nctr","--noncoding-tools",default=2,help="R|Default Option is 2, options available to run are\n"
    "1 Only Infernal \n"
    "2 Aragon, Infernal and Rnammer (and merge results")
    
    
    args = vars(parser.parse_args())
    ##################################### User input ends and variables are assigned #############################################################


    output_path=args['gene_output']
    run_tool=args['coding_tools']
    type_species=args['type_species']
    flag=args['input_option']
    nc_tool=args['noncoding_tools']
    #print(output_path,run_tool,type_species,flag)


    ##############################################################################################################################################
    #checks whether genemarks2 and prodigal tools, if either or both are called are present or not.
    if not check_tools(run_tool):
        return False

    ##### If the user wants to take in his own input###############################################################################################
    if flag == 2:
        input_path=args['input_assembly']
        name=args['name_contigs']
        
        
        if check_input(input_path):
            # checks the input folder for manual input, and then runs the tools. Considers input folder to contain specific sequence folder which in turn contains the name variable (name of the contigs)
            # Runs prodigal or genemarks2 or both depending on the user's choice calls the function run_out 
            run_out,list_of_files=running_tools(input_path,output_path,type_species,run_tool,name)
            #If run out is false, it just returns false and the function returns the appropriate error message
            if not run_out:
                return False
            

            #If the user has chosen to run both gene marks2 and prodigal, we get the merge results of it by calling the script function merge_predict from the union script
            if run_tool==3:
                genemarks2_output=output_path+"/genemarks2/"
                prodigal_output=output_path+"/prodigal/"
                merge_output=output_path+"/merge_out"
                #### If the merge output directory doesnt exist, it makes a directory called merge out where the output files will be located, 
                # or just deletes the folder if it is present 
                if os.path.exists(merge_output) == False:
                    os.mkdir(merge_output)
                else:
                    shutil.rmtree(merge_output)
                    os.mkdir(merge_output)
                # Runs the function merge_predict
                merge=merge_predict(genemarks2_output,prodigal_output,input_path)
                #If merge is false, it just returns false and the function returns the appropriate error message
                if not merge:
                    return False


            blast_output=blast_results(run_tool,output_path)
            if not blast_output:
                return False
            rename_output=rename_scripts(list_of_files,output_path,run_tool)
            if not rename_output:
                return False
            

            ###########################################################################################################
            ######Non coding tools, runs infernal or aragon,rnammer or infernal tools and calls the function nc_run_out
            nc_run_out=noncoding_run(input_path,output_path,nc_tool,name)
            #If nc_run_out is false, it just returns false and the function returns the appropriate error message
            if not nc_run_out:
                return False

            if nc_tool==2:
                infernal_output=output_path+"/infernal/"
                aragon_output=output_path+"/aragon/"
                rnammer_output=output_path+"/rnammer/"
                # Runs the function ncRNA_merge_output
                ncmerge=ncRNA_merge_output(aragon_output,rnammer_output,infernal_output,output_path)
                #If ncmerge is false, it just returns false and the function returns the appropriate error message
                if not ncmerge:
                    return False    
            ###########################################################################################################

        else:
            return False
    ##################################################################################################################################################


    else:
        input_folder77=args['input_files77']
        input_folder99=args['input_files99']
        
        
        if check_input(input_folder77) and check_input(input_folder99):
            ###########################Coding tools, GeneMarkS2 and Prodigal, merge the results or keep them seperate blast out the results and 
            # there are two input paths as there are two folders given to us by the genome assembly group according to the kmer count
            # Runs prodigal or genemarks2 or both depending on the user's choice calls the function run_out 
            run_out,list_of_files=running_tools(input_folder77,output_path,type_species,run_tool,flag)
            #If run_out is false, it just returns false and the function returns the appropriate error message
            if not run_out:
                return False
            run_out,list_of_files=running_tools(input_folder99,output_path,type_species,run_tool,flag)
            if not run_out:
                return False

            #If the user has chosen to run both gene marks2 and prodigal, we get the merge results of it by calling the script function merge_predict from the union script    
            if run_tool==3:
                genemarks2_output=output_path+"/genemarks2/"
                prodigal_output=output_path+"/prodigal/"
                merge_output=output_path+"/merge_out"
                #### If the merge output directory doesnt exist, it makes a directory called merge out where the output files will be located, 
                # or just deletes the folder if it is present 
                if os.path.exists(merge_output) == False:
                    subprocess.call(["mkdir",merge_output])
                else:
                    shutil.rmtree(merge_output)
                    os.mkdir(merge_output)
                # Runs the function merge_predict
                merge=merge_predict(genemarks2_output,prodigal_output,input_folder77,merge_output,input_folder99)
                #If merge is false, it just returns false and the function returns the appropriate error message
                if not merge:
                    return False

            # Running the individual results or 
            blast_output=blast_results(run_tool,output_path)
            if not blast_output:
                return False
            rename_output=rename_scripts(list_of_files,output_path,run_tool)
            if not rename_output:
                return False
            
            ###########################################################################################################
            ######Non coding tools, runs infernal or aragon,rnammer or infernal tools and calls the function nc_run_out
            nc_run_out=noncoding_run(input_folder77,output_path,nc_tool,name)
            #If nc_run_out is false, it just returns false and the function returns the appropriate error message
            if not nc_run_out:
                return False

            nc_run_out=noncoding_run(input_folder99,output_path,nc_tool,name)
            if not nc_run_out:
                return False

            if nc_tool==2:
                infernal_output=output_path+"/infernal/"
                aragon_output=output_path+"/aragon/"
                rnammer_output=output_path+"/rnammer/"
                # Runs the function ncRNA_merge_output
                ncmerge=ncRNA_merge_output(aragon_output,rnammer_output,infernal_output,output_path)
                #If ncmerge is false, it just returns false and the function returns the appropriate error message
                if not ncmerge:
                    return False    
            ###########################################################################################################
 
        else:
            return False
################################################################################################################################################################################################################


if __name__=="__main__":
    main()
