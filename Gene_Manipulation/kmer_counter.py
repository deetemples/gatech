#/usr/bin/env python3

import sys

dict = {}
k = int(sys.argv[1])
fasta = open(sys.argv[2]).read()
post_fasta = fasta.split("\n",1)[1];
f = post_fasta.replace('\n', '')

for i in range(len(f) - k + 1):
   kmer = f[i:i+k]
   if kmer in dict:
      dict[kmer] += 1
   else:
      dict[kmer] = 1

for kmer, count in sorted(dict.items()):
	print(kmer + "\t" + str(count))

