'''
Script for creating .gff files from ab-initio results

'''

#!/usr/bin/env python

import subprocess,os,sys

'''
Function reads in the CRISPR results

'''
def pilercr_merger(input_directory_path,pilercr_file):

	#Creating input file path
	input_file=input_directory_path + pilercr_file
	
	#Creating output file path
	mod_pilercr_file_name=pilercr_file.replace("_crispr","_crispr.gff")
	output_file="./tmp/"+mod_pilercr_file_name
	dict1={}        #Dictionary stores the crispr array details for each contig tested.
	
	#Parsing the CRISPR input file
	with open(input_file,"r") as inp:
		in_file=inp.readlines()
		line_count=0    #Counter for the lines in input file.
		count=0 #Counter for number of crispr arrays predicted.
		while(line_count<len(in_file)):
			if in_file[line_count].startswith(">")==True:
				in_file[line_count]=in_file[line_count].rstrip()
				header=in_file[line_count].replace(">","")
				count=count+1
				if count not in dict1.keys():
					dict1[count]=header
			if in_file[line_count].startswith("SUMMARY BY SIMILARITY")==True:
				line_count=line_count+6
				count1=0        #Counter to match the number of arrays found to the ones reported in the "Summary by similarity"
				while in_file[line_count].startswith("SUMMARY BY POSITION")!=True:
					if count1<count:
						count1=count1+1
						crisp_array=in_file[line_count].split()
						arr_num=int(crisp_array[0])
						start_pos=crisp_array[2]
						end_pos=int(start_pos)+int(crisp_array[3])+1
						head=dict1[arr_num]
						dict1[arr_num]=head+"\t"+start_pos+"\t"+str(end_pos)+"\t"+"Copies:"+crisp_array[4]+";Repeat_length:"+crisp_array[5]+";Spacer_Length:"+crisp_array[6]+";Repeat_Consensus:"+crisp_array[8]+"\n"
					line_count=line_count+2
			if in_file[line_count].startswith("SUMMARY BY POSITION")==True:
				break
			line_count=line_count+1


	#Writing to the .gff output files
	with open(output_file,"a+") as op:
		for keys in dict1.keys():
			line_split=dict1[keys].split("\t")
			op.write(line_split[0]+"\t"+"pilercr"+"\t"+"CRISPR array"+"\t"+line_split[1]+"\t"+line_split[2]+"\t"+"."+"\t"+"."+"\t"+"."+"\t"+line_split[3])


'''
This function merges the predicted Transmembrane proteins to the .faa and .gff files produced by the Gene Prediction group.

'''
def tmhmm_merger(input_directory_path,tmhmm_file):

	#Creating input file path
	input_file=input_directory_path + tmhmm_file
	#Creating output file path for .gff file
	mod_tmhmm_file_name=tmhmm_file.replace("tmhmm","tmhmm.gff")
	output_file="./tmp/"+mod_tmhmm_file_name
	dict_faa={}
	#Parsing the TM protein input file
	with open(input_file,"r") as inp:
		for line in inp:
			line=line.rstrip()
			col=line.split("\t")
			header=col[0]
			pred_hel_split=col[4].split("=")
			pred_hel=pred_hel_split[1]
			top=col[5]
			if int(pred_hel)!=0:    #Rejecting the proteins with zero predicted alpha-helices
				dict_faa[header]= "Transmembrane Protein: Predicted Helices="+pred_hel+", Topology:"+top
	#Writing to the .gff output files
	with open(output_file,"a+") as op:
		for keys in dict_faa.keys():
			name=keys.split(":")
			node=name[0]
			number=name[1].split("-")
			start=int(number[0])-1
			if start <0:
				start=0
			stop=number[1]
			op.write(node+"\t"+"."+"\t"+"."+"\t"+str(start)+"\t"+stop+"\t"+"."+"\t"+"."+"\t"+"."+"\t"+dict_faa[keys]+"\n")


'''
This function merges the predicted Transmembrane proteins to the .faa and .gff files produced by the Gene Prediction group.

'''
def signalp_merger(input_directory_path,signalp_file):
	
	#Creating input file path
	input_file=input_directory_path + signalp_file
	#Creating output file path for .gff file
	mod_signalp_file_name=signalp_file.replace(".gff3","_signalp.gff")
	output_file="./tmp/"+mod_signalp_file_name
	signalp_dict={}
	#Parsing the SignalP input file
	with open(input_file,"r") as inp:
		first=inp.readline()	#Removing the first line
		for line in inp:
			col=line.split("\t")
			name=col[0]
			funct=col[2]
			signalp_dict[name]=funct
	#Writing to the .gff output files
	with open(output_file,"a+") as op:
		for keys in signalp_dict.keys():
                        name=keys.split(":")
                        node=name[0]
                        number=name[1].split("-")
                        start=int(number[0])-1
                        if start <0:
                                start=0
                        stop=number[1]
                        op.write(node+"\t"+"."+"\t"+"."+"\t"+str(start)+"\t"+stop+"\t"+"."+"\t"+"."+"\t"+"."+"\t"+signalp_dict[keys]+"\n")

	
			 
def main():
	inputpath_pilercr=sys.argv[1]
	inputpath_tmhmm=sys.argv[2]
	inputpath_signalp=sys.argv[3]
	files_pilercr=os.listdir(inputpath_pilercr)
	file_tmhmm=os.listdir(inputpath_tmhmm)
	file_signalp=os.listdir(inputpath_signalp)
	
	#Checking if pilercr input files exist in the directory
	if len(files_pilercr) == 0:
		print("No files present in the directory.")
	for name in files_pilercr:
		print("Writing file for "+name+"\n")
		#Writing gff of  PilerCr results.
		pilercr=pilercr_merger(inputpath_pilercr,name)
	
	#Checking if tmhmm input files exist in the directory
	if len(files_tmhmm) == 0:
		print("No files present in the directory.")
	for name in files_tmhmm:
		print("Writing file for "+name+"\n")
		#Writing gff of tmhmm results
		tmhmm=tmhmm_merger(inputpath_tmhmm,name)
	
	#Checking if signalp input files exist in the directory
	if len(files_signalp) == 0:
		print("No files present in the directory.")
	for name in files_signalp:
		print("Writing file for "+name+"\n")
		#Writing gff of signalp results
		signalp=signalp_merger(inputpath_signalp,name)

if __name__ == "__main__":
        main()

