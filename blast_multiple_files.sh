#!/bin/bash
#blast_multiple_files
cd /Users/yifan/BIOC396/tryblast/Shekari_fasta/
for i in $( ls )
do
    inname="\\./$i"
    outname="\\./$i.xml"
    echo "running blast on: $inname"
    ./runblast.sh 500 $inname $outname
done
echo "blast finished for Shekari"