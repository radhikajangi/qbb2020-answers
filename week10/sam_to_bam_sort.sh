#/!/bin/bash

for SAMPLE in 83 86 88 89 90 93 94 97
do

samtools view -S -b ${SAMPLE}.sam | samtools sort -o ${SAMPLE}.sorted.bam

done