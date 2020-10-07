#/usr/bin/env python3
import sys

knownGene = sys.argv[1]
kgxRef = sys.argv[2]
infection = sys.argv[3]

startStops = {}		#key is ID; value is tuple of chr, start, stop
with open(knownGene, "r") as fh:
	fh.readline()
	for thisLine in fh:
		cols = thisLine.split("\t")
		startStops[cols[0]] = (cols[1], cols[3], cols[4])	#chr, start, stop
fh.close()

names = {}		#key is ID; value is gene name
genesFound = set()	#identifies duplicate genes
with open(kgxRef, "r") as fh:
	fh.readline()
	for thisLine in fh:
		cols = thisLine.split("\t")
		gene = cols[4]
		if not gene in genesFound:		#check if Gene Name is duplicate
			key = cols[0]		
			names[key] = gene		#key is ID;  value is gene name
			genesFound.add(gene)		#add Gene Name if not duplicate
		else:
			startStops.pop(cols[0], None)	#pops Gene Name if duplicate
fh.close()

infGenes = set()
with open(infection, "r") as file:
	contents = file.readlines()		#a list of lines
	contents = contents[1:]			#removes header
	for c in contents:
		infGenes.add(c.strip())
file.close()

results = []
for theID in names.keys():		#iterates through the dictionaries
	theGene = names[theID]
	if theGene in infGenes:
		theChr = startStops[theID][0]
		theStart = startStops[theID][1]
		theStop = startStops[theID][2]
		row = [theGene, theChr, theStart, theStop]
		results += [row]
results.sort(key = lambda x: x[0])	#sorts alphabetically by gene name

print("Gene\tChr\tStart\tStop")
for r in results:
	print("\t".join(r))


