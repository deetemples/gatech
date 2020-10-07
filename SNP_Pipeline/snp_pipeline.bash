#!/bin/bash

# Place your gatech username in the below export
export NAME="dtemples3"

get_input () {
	# Function for doing your getopts
	# Inout for all the flags
	# Input: Getopts array
while getopts ":a:b:r:eo:f:zvih" option; do
case $option in
a) reads1=$OPTARG;;	# first reads file
b) reads2=$OPTARG;;	# second reads file
r) ref=$OPTARG;;	# ref genome
e) realign=1;;		# realignment turned on
o) output=$OPTARG;;	# output file name
f) millsFile=$OPTARG;;	# Mills File name
z) gunzip=1;;		# gunzip turned on
v) v=1;;		# verbose mode on
i) index=1;;		# index turned on
h) echo "how to run script: ./snp_pipeline_bash -a <first reads file>, -b <second reads file>, -r <ref genome>, -e (realign status), -o <output file name>, 
-f <Mills File name>, -z (gunzip status), -v (verbose mode), -i (index status), -h (help)"
exit 0;;
esac
done
}

check_files () {
	# Function for checking for presence of input files, reference genome,
	# and the output VCF file
	#
	# Input: File locations (string)
	# Output: True, if checks pass; False, if checks fail (bool)
	# Checks if reads1, reads2, ref genome, output, and millsFile exist
if [ $v -eq 1 ]; then
echo "Beginning check files."
fi

if [ ! -f $reads1 ]; then
echo "False. Missing first reads file."
exit 1

elif [ ! -f $reads2 ]; then
echo "False. Missing second reads file."
exit 1

elif [ ! -f $ref ]; then
echo "False. Missing ref genome."
exit 1

elif [ -f $output ]; then
echo "Would you like to overwrite existing VCF file (o) or exit (e)?"
read answer
if [ $answer == 'o' ]; then
echo "Overwritting excisting VCF file."
elif [ $answer == 'e' ]; then
echo "Exiting"
exit 1
else 
echo "Improper input. Exiting"
exit 1
fi

elif [ ! -f $millsFile ]; then
echo "Missing Mills File."
exit 1
fi
}

prepare_temp () {
	# Preparing your temporary directory
	# holds all files made in temp directory
	# 

if [ $v -eq 1 ]; then
echo "Preparing temporary directory."
fi
tmp=$(mktemp -d)
}


mapping () {
	# Function for the mapping step of the SNP-calling pipeline
	# Maps reads1 & reads2 onto ref genome then sorts
	# Input: File locations (string), Verbose flag (bool)
	# Output: File locations (string)
if [ $v -eq 1 ]; then
echo "Beginning mapping step"
fi
bwa index $ref
bwa mem -R '@RG\tID:foo\tSM:bar\tLB:library1' "$ref" "$reads1" "$reads2" > $tmp/lane.bam

samtools fixmate -O bam $tmp/lane.bam $tmp/lane_fixmate.bam

samtools sort -O bam -o $tmp/lane_sorted.bam -T $tmp/lane_temp $tmp/lane_fixmate.bam
}

improvement () {
	# Function for improving the number of miscalls
	# Realigns twice then indexes
	# Input: File locations (string)
	# Output: File locations (string)
samtools faidx ./data/chr17.fa
samtools dict ./data/chr17.fa
samtools index $tmp/lane_sorted.bam  
if [ $realign -eq 1 ]; then
if [ $v -eq 1 ]; then
echo "First step of realignment improvement"	# reduces the number of miscalls of INDELs by realigning raw gapped alignment
fi
java -Xmx2g -jar ./lib/GenomeAnalysisTK.jar -log ./output/dtemples3.log -T RealignerTargetCreator -R $1 -I $tmp/lane_sorted.bam -o $tmp/lane.intervals --known $2
if [ $v -eq 1 ]; then
echo "Second step of realignment improvement"
fi
java -Xmx4g -jar ./lib/GenomeAnalysisTK.jar -log file -T IndelRealigner -R $1 -I $tmp/lane_sorted.bam -targetIntervals $tmp/lane.intervals -known $2 -o $tmp/lane_sorted.bam
cat file >> ./output/dtemples3.log	# saves log to dtemples3.log
fi

if [ ! -z "$index" ]; then	# if index is set, then index lane_sorted
if [ $v -eq 1 ]; then
echo "Index bam step of improvement"
fi
samtools index $tmp/lane_sorted.bam
fi
}

call_variants () {
	# Function to call variants
	# Filters varients then makes either a zipped or nonzipped file
	# Input: File locations (string)
	# Ouput: None
if [ $v -eq 1 ]; then
echo "First step of variants"	# produce a BCF file that contains all of the locations in the genome
fi
bcftools mpileup -Ou -f $ref $tmp/lane_sorted.bam | bcftools call -vmO z -o $output.vcf.gz

if [ $v -eq 1 ]; then
echo "Second step of variants"	# indexes files
fi
tabix -p vcf $output.vcf.gz	# requires a zipped file

if [ -z "$gunzip" ]; then	# if gunzip is not set, decompress the vcf file
gunzip -d $output.vcf.gz
fi
}

main() {
	# Function that defines the order in which functions will be called
	# You will see this construct and convention in a lot of structured code.
	
	# Add flow control as you see appropriate
	get_input "$@"
	check_files
	prepare_temp
	mapping "$ref" "$reads1" "$reads2"
	improvement "$ref" "$millsFile" "$index" "$realign"
	call_variants "$ref" "$output" "$gunzip"
}

# Calling the main function
main "$@"


# DO NOT EDIT THE BELOW FUNCTION
bats_test (){
    command -v bats
}
# DO NOT EDIT THE ABOVE FUNCTION
