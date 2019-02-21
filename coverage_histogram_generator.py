#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:41:25 2019

@author: yifan
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#coverage_histogram_generator

def gene_transcript_dic(csv_dir):
    df=pd.read_csv(csv_dir, usecols=['Ensembl gene ID',
            'Ensembl transcript ID'])
    mylist = df.values.tolist()
    gene_dic={}
    # {ensg:[[ensts], count]}
    for gene, transcript in mylist:
        if gene in gene_dic.keys():
            if transcript not in gene_dic[gene]:
                gene_dic[gene].append(transcript)
        else:
            gene_dic[gene]=[transcript]
    return gene_dic



def enst_count_histogram(gene_dic):
    enst_count_list=[]
    for key, value in gene_dic.items():
        enst_count_list.append(len(value))
    
  
    data= pd.Series(enst_count_list)

    data.plot.hist(grid=True, color = 'grey', rwidth=1,
                   bins=np.arange(min(data), max(data)))
    plt.xticks(range(min(data), max(data)))
    
    plt.title("Transcripts Per Gene in GeTPRA" )
    plt.xlabel("Number of transcripts per gene")
    plt.ylabel("Counts")
    plt.grid(axis='y', alpha=0.5)
    
    plt.savefig("./transcripts_per_gene_counts.png", dpi=1000)
    plt.show()
    return enst_count_list

def gene_dic_with_MS(gene_dic, unique_csv_dir):
    df=pd.read_csv(unique_csv_dir, usecols=['Ensembl gene ID',
            'Ensembl transcript ID', 'Lee2017 Evidence','Shekari2017 Evidence'])
    mylist = df.values.tolist()
    
    gene_dic_with_MS={}
    for key, value in gene_dic.items():
        newvalue=[value,[]]
        gene_dic_with_MS[key]=newvalue
    for entry in mylist:
        g,t,l,s=entry
        if (type(l) is str) or (type(s) is str):
            gene_dic_with_MS[g][1].append(t)
            
        #gene_dic_with_MS = {ensg:[
        #                       [all enst in getpra for this gene],
        #                       [enst with MSMS evidence for this gene that are covered in getpra]
        #                   ]}
   
    return gene_dic_with_MS
    
def coverage_histogram(gene_dic):
    coverage_count_list=[]
    for key, value in gene_dic.items():
        #print(value[1])
        #print(len(value[1]))
        coverage=float(len(value[1]))/float(len(value[0]))
#        if coverage !=0.0:
#            print(coverage)
        coverage_count_list.append(coverage)
  
    data=pd.Series(coverage_count_list)

    data.plot.hist(grid=True, color = 'grey', rwidth=1, bins=30)    
    plt.title("Transcript Coverage Per Gene by MSMS Evidence" )
    plt.xlabel("Percent Transcript Coverage Per Gene (%)")
    plt.ylabel("Counts")
    plt.grid(axis='y', alpha=1)
    bins=np.arange(0, 1.05, 0.05)
    plt.xticks(bins,rotation='vertical')
    plt.tight_layout()
    
    plt.savefig("./MS_transcript_coverage.png", dpi=1000)
    plt.show()
    return coverage_count_list


if __name__=="__main__":
    gene_count_dic=gene_transcript_dic('./getpra_comparison.csv')
    enst_count_list=enst_count_histogram(gene_count_dic)
    gene_count_dic_with_MS=gene_dic_with_MS(gene_count_dic, './getpra_comparison_unique.csv')
    coverage_count_list=coverage_histogram(gene_count_dic_with_MS)
