#!/bin/bash
#this script outputs blastp result as xml file
#$1: E-value //set to 500 for now
#$2: query file name
#$3: output file name 
#change your direcoty as needed
cd /Users/yifan/BIOC396/tryblast/
#to make blast database
makeblastdb -in Homo_sapiens.GRCh38.pep.all.fa -dbtype prot
echo database created
#run blastp
echo start to run blastp
blastp -evalue $1 -query $2 -db Homo_sapiens.GRCh38.pep.all.fa -out $3 -outfmt 5
echo blastp result created
