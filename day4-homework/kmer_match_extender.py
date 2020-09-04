#!/usr/bin/env python3

# Run from command line as "./kmer_match_extender.py subset.fa droYak2_seq.fa 11 > matches.txt
import sys
from fasta_iterator_class import FASTAReader
target_fname = sys.argv[1]
droyak_fname = sys.argv[2]
k = int(sys.argv[3])

# Creates target seq id + seq for target and query files
target_seqs = FASTAReader(open(target_fname))
droyak_seqs = FASTAReader(open(droyak_fname))

# Will hold all kmers from target file    
kmers = {}

for seq_id, sequence in target_seqs:
    for i in range(0, len(sequence) - k+1): # i = start position of kmer
        kmer = sequence[i:i + k] # Store kmer at current position
        if kmer in kmers:
                kmers[kmer].append(i) # If identical kmer stored,
                                        # append to val list 
        else:
            kmers[kmer] = [seq_id, i] # Unique kmer added to dict
    
count = 0
for seq_id, sequence in droyak_seqs:
    for i in range(0, len(sequence) - k+1):
        kmer_q = sequence[i:i + k] # Pull q kmer
        if kmer_q in kmers: # Search target dict for query kmer
            print("target sequence names and starts {},\t query start: {},\t kmer: {}".format(str(kmers[kmer_q]), i, kmer_q))
            count+=1
        if count > 1000: # Print 1000 lines to file
            break

            
                                                     
            

    
    
    
    
    
    
    
    
    
    
    