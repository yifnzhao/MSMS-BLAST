#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:17:57 2019

@author: yifan
"""
#blast_parser

from Bio.Blast import NCBIXML
#import re
import pandas


def parse_BLAST_Output(blast_records): 
    # note that the sequence will not be recorded if no hits are found
    ensp=[]
    ensg=[]
    enst=[]
    gene_name=[]
    queryseq=[]
    querylen=[]
    matchseq=[]
    e_value=[]
    #blast_score=[]
    #num_alignments=[]
    alignment_len=[]
    #gaps=[]
    #positives=[]
    #percent_pos_align_len=[]
    #percent_pos_query_len=[]
    identities_over_querylen=[]
    sbjctseq=[]
    subcellular_loc=[]
    
    for blast_record in blast_records:
        # reference: http://biopython.org/DIST/docs/api/Bio.Blast.Record-module.html
        for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    if hsp.identities < blast_record.query_length:
                        continue

                    querylen.append(blast_record.query_length)
                    alignment_title=alignment.title.split()
                    ensp.append(alignment_title[1])
                    ensg.append(alignment_title[4].split(":")[1])
                    enst.append(alignment_title[5].split(":")[1])
                    gene_name.append(alignment_title[8].split(":")[1])
                    subcellular_loc.append(blast_record.query)
                    #print(alignment_title)
                   
                    # reference: http://biopython.org/DIST/docs/api/Bio.Blast.Record.HSP-class.html
                    queryseq.append(hsp.query) # query seq (IPAMTIAK)
                    
                    matchseq.append(hsp.match) # match sequence
                    e_value.append(hsp.expect) # expect value
                    #blast_score.append(hsp.score) # BLAST score of hit
                    #num_alignments.append(hsp.num_alignments) # number of alignments for same subject
                    alignment_len.append(hsp.align_length)
                    #gaps.append(hsp.gaps)
                    #positives.append(hsp.positives)
                    #percent_pos_align_len.append(str((hsp.positives / hsp.align_length) * 100) + '%')
                    #percent_pos_query_len.append(str((hsp.positives / blast_record.query_length) * 100) + '%')           
                    identities_over_querylen.append(hsp.identities/blast_record.query_length)
                    sbjctseq.append(hsp.sbjct)
                    
    df_dic={"ENSG": ensg, "Gene Name": gene_name,
                                "ENST": enst,
                                "ENSP": ensp, 
                                "Gene Name": gene_name,
                                "Subcellular Location":subcellular_loc,
                                "Query Sequence":queryseq,
                                "Match Sequence":matchseq,
                                "Subject Sequence:":sbjctseq,
                                "Query Length": querylen,   
                                "Alignment Length":alignment_len,
                                "Identitiies/Query Length": identities_over_querylen,                               
                                "E Value":e_value
                                }     


    df = pandas.DataFrame(data=df_dic)
    df.to_csv('./output_N23_Shekari2017_parsed.csv', sep=',')  
        

if __name__ == '__main__':
    
    result_handle = open("./N23.xml")

    blast_records = NCBIXML.parse(result_handle)

    parse_BLAST_Output(blast_records)
    print("A parsed output file is generated.")