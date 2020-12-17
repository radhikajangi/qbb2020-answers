#!/bin/bash
for SAMPLE in 83 86 88 89 90 93 94 97
do

#bwa mem -R "@RG\tID:${SAMPLE}\tSM:{SAMPLE}" sacCer3.fa A01_${SAMPLE}.fastq > A01_${SAMPLE}.sam
bwa mem week13_data/assembly.fasta week13_data/READS/SRR4921${SAMPLE}_1.fastq week13_data/READS/SRR4921${SAMPLE}_2.fastq > ${SAMPLE}.sam

done