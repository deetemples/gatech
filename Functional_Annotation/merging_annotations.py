'''
This script merges the individual .gff results from all tools into one
'''

#!/usr/bin/env python

import subprocess,os,sys

'''
Function to merge the .gffs
'''
def merge_gff(input_directory_path,output_directory_path):
	
	files=os.listdir(input_directory_path)
	
	#Getting a list od unique sample names
	sample_list=[]
	for item in files:
		sample_name=item.split("_")
		if sample_name[0] not in sample_list:
			sample_list.append(sample_name[0])
	
	#Merging the .gffs of each sample
	for sample in sample_list:
		sample_dict={}
		#Reading crispr results
		sample_crispr=input_directory_path+"/"+sample+"_crispr.gff"
		if os.path.isfile(sample_crispr)==True:
			with open(sample_crispr,"r") as crisp:
				for line in crisp:
					line=line.rstrip()
					col=line.split("\t")
					crisp_key=col[0]+","+col[3]+","+col[4]
					crisp_def="CRISPR array:"+col[-1]
					if crisp_key not in sample_dict.keys():
						sample_dict[crisp_key]=[crisp_def]
					else:
						sample_dict[crisp_key].append(crisp_def)
		#Reading TM results
		sample_tm=input_directory_path+"/"+sample+"_tmhmm.gff"
		if os.path.isfile(sample_tm)==True:
			with open(sample_tm,"r") as tm:
				for line in tm:
					line=line.rstrip()
					col=line.split("\t")
					tm_key=col[0]+","+col[3]+","+col[4]
					tm_def=col[-1]
					if tm_key not in sample_dict.keys():
						sample_dict[tm_key]=[tm_def]
					else:
						sample_dict[tm_key].append(tm_def)
		
		#Reading SignalP results
		sample_sp=input_directory_path+"/"+sample+"_union_signalp.gff"
		if os.path.isfile(sample_sp)==True:
			with open(sample_sp,"r") as sp:
				for line in sp:
					line=line.rstrip()
					col=line.split("\t")
					sp_key=col[0]+","+col[3]+","+col[4]
					sp_def=col[-1]
					if sp_key not in sample_dict.keys():
						sample_dict[sp_key]=[sp_def]
					else:
						sample_dict[sp_key].append(sp_def)
		
		#Reading VFDB results
		sample_vf=input_directory_path+"/"+sample+"_union_vf.gff"
		if os.path.isfile(sample_vf)==True:
			with open(sample_vf,"r") as vf:
				for line in vf:
					line=line.rstrip()
					col=line.split("\t")
					vf_key=col[0]+","+col[3]+","+col[4]
					vf_def="Virulence Factor:"+col[-1]
					if vf_key not in sample_dict.keys():
						sample_dict[vf_key]=[vf_def]
					else:
						sample_dict[vf_key].append(vf_def)

		#Reading CARD results
		sample_ca=input_directory_path+"/"+sample+"_union_card.gff"
		if os.path.isfile(sample_ca)==True:
			with open(sample_ca,"r") as ca:
				for line in ca:
					line=line.rstrip()
					col=line.split("\t")
					ca_key=col[0]+","+col[3]+","+col[4]
					ca_def="AMR profile:"+col[-1]
					if ca_key not in sample_dict.keys():
						sample_dict[ca_key]=[ca_def]
					else:
						sample_dict[ca_key].append(ca_def)

		#Reading Eggnog resulst
		sample_eg=input_directory_path+"/"+sample+"_union_eg.gff"
		if os.path.isfile(sample_eg)==True:
			with open(sample_eg,"r") as eg:
				for line in eg:
					line=line.rstrip()
					col=line.split("\t")
					eg_key=col[0]+","+col[3]+","+col[4]
					eg_def="Eggnog:"+col[-1]
					if eg_key not in sample_dict.keys():
						sample_dict[eg_key]=[eg_def]
					else:
						sample_dict[eg_key].append(eg_def)
		'''
		#Reading Operon results
		sample_op=input_directory_path+"/"+sample+"_union_op.gff"
		if os.path.isfile(sample_op)==True:
			with open(sample_op,"r") as op:
				for line in op:
					line=line.rstrip()
					col=line.split("\t")
					op_key=col[0]+","+col[3]+","+col[4]
					op_def=col[-1]
					if op_key not in sample_dict.keys():
						sample_dict[op_key]=[op_def]
					else:
						sample_dict[op_key].append(op_def)
		'''
		
		#Writing final merged .gff
		output_file=output_directory_path+"/"+sample+".gff"
		for keys in sample_dict.keys():
			col=keys.split(",")
			node=col[0]
			start=col[1]
			stop=col[2]
			funct_list=sample_dict[keys]
			function=";".join(funct_list)
			with open(output_file,"a+") as out:
				out.write(node+"\t"+"."+"\t"+"."+"\t"+start+"\t"+stop+"\t"+"."+"\t"+"."+"\t"+"."+"\t"+function+"\n")


def main():
	input_path=sys.argv[1]
	output_path=sys.argv[2]
	merge_gff(input_path,output_path)

if __name__ == "__main__":
	main()
		
