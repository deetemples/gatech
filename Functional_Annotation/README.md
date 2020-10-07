# Functional Annotation Tools 


## Objective
Perform a full functional annotation on the genes and proteins determined by the Gene Prediction group that is relevant to C. jejuni
We will be dividing functional annotation tools into clustering, homology-based and ab-initio-based tools.

## Pipeline
We will be analyzing our DNA and protein sequences (in faa, fna, and gff files) using homology and ab-initio based techniques. We will be narrowing down the following categories to one tool based on efficiency and performance.e
## Clustering
### Clustering Sequences: CDHit 
	./cd-hit -i <input_file> -o <output_file_name>
## Homology
### Antibiotic Resistance: CARD
	wget https://card.mcmaster.ca/latest/data
	tar -xvf data ./card.json
	rgi load --card_json <path to card.json> --local
	rgi main -i <path to cluster.faa> -o <output_file_name> -t protein –local
	rgi tab -i <path to output_file_name.json>
### Virulence: VFDB
	makeblastdb -in VFDB_db -dbtype 'nucl' -out <db_name>
	blastn -db <db_name> -query <cluster> -out <result> -max_hsps 1 -max_target_seqs 1 -outfmt "6 qseqid length qstart qend sstart send evalue bitscore stitle" -perc_identity 100 -num_threads 5
### Operons: MicrobesOnline
	makeblastdb -in <fasta file > -dbtype prot -out <database>
	blastp -query cdhit/faa_rep_seq.faa -db tmp/db_operon -evalue 0.01 -max_target_seqs 1 -max_hsps 1 -outfmt 6 -out tmp/hits_0.01.txt -num_threads 5
### Fully Automated Functional Annotation: eggNOG Mapper
	./emapper.py  -i <cluster> --output <result> -d bact -m diamond
## Ab-initio
### Trans Membrane Protein: TMHMM2
	tmhmm <input multifasta file> > <output_file> 
### Signal Peptide: SignalP v5.0
	signalp –fasta <input_sequence_file> -org gram- -format short –gff3
### CRSIPR: PilerCR
	pilercr –in <input multifasta file> -out <output file> -noinfo –quiet
