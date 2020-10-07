# This is Gene Prediction (Team 2, Group 2)
**Paarth Parekh, Danielle Temples, Kara Keun Lee, Shuting Lin**

## Required Software
**Conda is recommended way of installing tools** <br/>
**Python and Perl is needed to run this pipeline**
1. GeneMarkS-2 (Locally in the path)
2. Prodigal
3. Blast+
4. bedtools
5. samtools
6. transeq
7. aragon
8. Infernal
9. rnammer

## To Run
Please Run the backbone script. It takes in the following inputs:
1. INPUT_OPTION:	Default Option is 1, options available
                		1 Take input from the genome assembly results 
                		2 Input your own assembly files
2. NAME_CONTIGS:	Name of the contig files,called when option 2 for input-option is selected, default considered is contigs.fasta
3. INPUT_ASSEMBLY:	Path to the directory that contains input file manually,called when option 2 for input-option is selected
4. INPUT_FILES77:	Path to the directory that contains input file for genome assembly output of 21,33,55,77, called when default option for input-option is selected
5. INPUT_FILES99:	Path to the directory that contains input file for genome assembly output of 21,33,55,77,99,127,called when default option for input-option is selected
6. GENE_OUTPUTS:	Path to a directory that will store the output gff files, fna files and faa files.
7. CODING_TOOLS:	Default Option is 3, options available to run are
                        	1 Only GeneMarkS-2 
                        	2 Only Prodigal 
                        	3 Both and getting a union of the genes
8. TYPE_SPECIES:	if running Gene_MarkS-2, mention species to be either bacteria or auto
9. NONCODING_TOOLS:	Default Option is 2, options available to run are
                        	1 Only Infernal 
                        	2 Aragon, Infernal and Rnammer (and merge results

## Description:
This Gene Prediction Pipeline runs GeneMarkS-2 and/or Prodigal to predict the coding genes in the assembled fasta files and blasts it against the reference database to validate the results and gives output as Known gene or Unknown Gene. If both GeneMarkS-2 and Prodigal are called then it merges the results and then blasts the results to give renamed .fna, .faa and .gff files. 

For Noncoding Prediction it uses Infernal and/or Infernal,Aragon and Rnammer to predict the ncRNA. If all three tools are called it merges the results and gives the merged gff files.
