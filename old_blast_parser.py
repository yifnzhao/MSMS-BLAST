#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:17:57 2019

@author: yifan
"""
#blast_parser

from Bio.Blast import NCBIXML
import re
import csv
import sys
import pandas


def hit_ensg_gene_id(blast_record_title):
    title_info = blast_record_title.split()
    return title_info[4].split(':')[1] #ensg based on title formatting



def parse_BLAST_Output(blast_records): 
    
    
    
    blast_parsed_output = open("/Users/yifan/BIOC396/tryblast/blast_output_parse.csv", 'w')
    file_writer = csv.writer(blast_parsed_output, quoting = csv.QUOTE_ALL)
    #print('Protein_ID Gene_ID Transcript_ID Gene_Symbol E_Value Query_length Alignment_Length Gaps Positives Percentage_Positives \n')
    file_writer.writerow(['Subcellular Location', 'Protein ID', 'Gene ID', 'Transcript ID', 'Gene Name', 'E Value', 'Query Length', 'Alignment Length', 'Gaps', 'Positives', '% Positives (Alignment length)', '% Positives (Query length)'])
    
    
    
    
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                
                
                
                
                title_info = [str(blast_record.query)] #indicates subcellular locations
                #title_info.append(str(blast_record.query.split()[1]))
                #title_info.append(str(blast_record.query.split()[2]))
                hit_info = blast_record_alignment.title.split() 
                title_info.append(hit_info[1]) #ensp 
                title_info.append(hit_info[4].split(':')[1]) #ensg
                title_info.append(hit_info[5].split(':')[1]) #enst
                title_info.append(hit_info[8].split(':')[1]) #hit gene name
                title_info.append(str(hsp.expect)) # e value
                title_info.append(str(blast_record.query_length)) # pepide sequence query length
                title_info.append(str(hsp.align_length))
                title_info.append(str(hsp.gaps))
                title_info.append(str(hsp.positives))
                title_info.append(str((hsp.positives / hsp.align_length) * 100) + '%')
                title_info.append(str((hsp.positives / blast_record.query_length) * 100) + '%')
                file_writer.writerow(title_info)
                for unit in title_info:
                    sys.stdout.write(unit + " ")
                print('\n')
        file_writer.writerow('END OF ENTRY')
        print('-----------------------------------------------------------------------------------------------------------\n')
                
    blast_parsed_output.close()
    return


if __name__ == '__main__':
    
    result_handle = open("/Users/yifan/BIOC396/tryblast/test_output.xml")

    blast_records = NCBIXML.parse(result_handle)

    parse_BLAST_Output(blast_records)