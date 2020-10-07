import os
from Bio import Entrez
import urllib3
import subprocess

def operon_blast(input_file, input_cluster):

	subprocess.call("makeblastdb -in "+input_file+" -dbtype prot -out tmp/db_operon1", shell=True)
	subprocess.call("blastp -query "+input_cluster+" -db tmp/db_operon1 -max_target_seqs 1 -max_hsps 1 -outfmt 6 -out tmp/hits.txt -num_threads 5", shell=True)
	return True


def operon_db_creation(ref, op_dir):

	#Creating a list of operon IDs 
	locus=[]
	files = os.listdir(ref)
	for i in files:
		with open(ref+'/'+i, 'r') as f:
			first = f.readline()
			for line in f:
				line = line.strip('\n')
				line = line.split('\t')
				if line[6]=='TRUE':
					if line[7] != 'NA':
						if float(line[7])>0.9:
							locus.append(line[0])
							locus.append(line[1])
			
		f.close()	

	#Removing duplicate operon IDs
	locus = list(dict.fromkeys(locus))

	#Creating a dictionary containg GID for each operon ID
	dic={}
	files1 = os.listdir(op_dir)
	for j in files1:
		f1 = open(op_dir+'/'+j, 'r')
		for line in f1:
			line = line.strip('\n')
			line = line.split('\t')
			if line[2] != '':
				key = line[0]
				value = line[2]
				if key not in dic.keys():
					dic[key]=value
		f1.close()

	#Creating a list of GID for each operon
	gi=[]
	for l in locus:
		if l in dic.keys():
			gi.append(dic[l])

	#Download protein sequences based on GID and create fasta file
	fasta_file = 'operon_database.fasta'
	x = 0
	n = 0
	for i in gi:
		with open(fasta_file,'a') as file2:
			n+=1
			Entrez.email="jhgmjyf%f@gmail.com"%x
			handle = Entrez.efetch(db="protein", id=i, rettype="fasta", retmode="text")
			seq = handle.read()
			print(n)
			file2.write(seq)
			x += 1

	return(fasta_file)


def main():
	'''
	# Argparse
	parser = argparse.ArgumentParser(description='Predicting Operons')
	parser.add_argument('--input_file', '-f1', type=str, help='Cluster input file path')
	parser.add_argument('--input_file', '-f1', type=str, help='Cluster input file path')
	parser.add_argument('--output_file', '-o', type=str, help='Output file name')
	#parser.add_argument('--input_sequence_type', '-t', type=str, help='Sequence type - n/p')

	args = parser.parse_args()
	'''

	input_cluster = '../output/cdhit/faa_rep_seq.faa' 

	reference = 'ref_CJ/'
	predicted_operons = 'MO_operons/'


	input_fasta = operon_db_creation(reference, predicted_operons)
	run_blast = operon_blast(input_fasta, input_cluster)


	# makeblastdb -in operon_db.fasta -dbtype prot -out tmp/db_operon
	# blastp -query cdhit/faa_rep_seq.faa -db tmp/db_operon -max_target_seqs 1 -max_hsps 1 -outfmt 6 -out tmp/hits2.txt -num_threads 5

if __name__ == "__main__":
	main()
