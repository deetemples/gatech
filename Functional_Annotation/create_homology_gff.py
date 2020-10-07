'''
Script for creating .gff files from homology results incorporating the clustering data

'''

#!/usr/bin/env python

import subprocess,os,sys

'''
Function reads in the VFDB results

'''
def vfdb(input_file_path):
	
	vfdic={}
	
	#Parsing the VFDB results:
	with open(input_file_path,"r") as vfin:
		for line in vfin:
			col=line.split("\t")
			node=col[0].split()
			vir=col[1]
			if node[0] not in vfdic.keys():
				vfdic[node[0]]=[vir]
	return(vfdic)

'''
Function reads in the CARD results
'''
def card(input_file_path):
	
	cardic={}
	
	#Parsing the CARD results:
	with open(input_file_path,"r") as cardin:
		
		#Skipping the first line
		cardin.readline()
		for line in cardin:
			col=line.split("\t")
			node=col[0].split()
			antbio=col[14]
			mech=col[15]
			amr_gene_family=col[16]
			if node[0] not in cardic.keys():
				cardic[node[0]]=[antbio,mech,amr_gene_family]
	return cardic


'''
Function reads in the Eggnog results

'''
def eggnog(input_file_path):
	
	eggdic={}
	
	#Parsing the Eggnog results:
	with open(input_file_path,"r") as eggin:
		for line in eggin:
			if line.startswith("#")==False:
				line=line.rstrip()
				col=line.split("\t")
				node=col[0]
				function=col[-1]
				if node not in eggdic.keys():
					eggdic[node]=[function]
	return eggdic
				 
'''
Function reads in the Operon results
'''
def operon(input_file_path):
	
	operondic={}

	#Parsing Operon results:
	with open(input_file_path,"r") as opin:
		for line in opin:
			col=line.split("\t")
			node=col[0]
			function="Operon member"
			if node not in operondic.keys():
				operondic[node]=[function]
	return operondic





'''
This function relates homology results to their clusters
'''
def cluster(cluster_input):
	
	#Reading the centroids of each cluster
	centroid=[]
	clustdic={}
	with open(cluster_input,"r") as clustin:
		clust=clustin.readlines()
		line=0
		while(line<len(clust)-1):
			if clust[line].startswith(".")==False:
				line=line+1
				while(clust[line].startswith(".")==True and line<len(clust)-1):
					clust[line]=clust[line].rstrip()
					col=clust[line].split("/")
					node=col[4]
					if node.endswith("...*") ==True:
						name=node.replace("...*","")
						centroid.append(name)
						clustdic[name]=[clust[line]]
					else:
						text=node.split("...")
						clustdic[centroid[-1]].append(clust[line])
					line=line+1
	return clustdic

'''
This function creates gff files for each output

'''
def gff(clustdic,dictionary,retype):
	for key in dictionary.keys():
		if key in clustdic.keys():
			mem=clustdic[key]
			for item in mem:
				node=item.split("/")
				file_name="./tmp/"+node[3]
				out_ext="_"+retype+".gff"
				output_file=file_name.replace(".faa",out_ext)
				col=node[4].split(":")
				name=col[0]
				pos=col[1].split("-")
				start=int(pos[0])-1
				stop=pos[1].split("...")
				list1=dictionary[key]
				details=",".join(list1)
				with open(output_file,"a+") as ot:
					ot.write(name+"\t"+"."+"\t"+"."+"\t"+str(start)+"\t"+stop[0]+"\t"+"."+"\t"+"."+"\t"+"."+"\t"+details+"\n")
					
				
def main():
	vfdb_input=sys.argv[1]
	card_input=sys.argv[2]
	eggnog_input=sys.argv[3]
#	operon_input=sys.argv[4]
	cluster_input=sys.argv[4]
	cluster_membership=sys.argv[5]
	
	vf_name="vf"
	card_name="card"
	eggnog_name="eg"
	operon_name="op"

	#Merging the cluster files
	paste_com="paste "+cluster_membership+" "+cluster_input+" > Clust1"
	os.system(paste_com)
	awk_com="cat Clust1 | cut -d'\t' -f1,3 > Clust2"
	os.system(awk_com)
	rm_com="rm Clust1"
	os.system(rm_com)
	sed1_com="sed -i 's/>//g' Clust2"
	os.system(sed1_com)
	sed2_com="sed -i 's/Cluster //g' Clust2"
	os.system(sed2_com)
	sed3_com="sed -i -E 's/\s+[0-9]+[a]{2},\s+/\//g' Clust2"
	os.system(sed3_com)

	#Parsing the outputs	
	vfdic=vfdb(vfdb_input)
	clustdic=cluster(Clust2)
	cardic=card(card_input)
	eggdic=eggnog(eggnog_input)
	#operondic=operon(operon_input)
	
	#Creating gffs
	gff(clustdic,vfdic,vf_name)
	gff(clustdic,cardic,card_name)
	gff(clustdic,eggdic,eggnog_name)
	#gff(clustdic,operondic,operon_name)
	
if __name__ == "__main__":
	main()

