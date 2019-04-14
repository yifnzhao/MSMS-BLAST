#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 18:21:00 2019

@author: yifan
"""

#peptide_seq_length_counter

''' 
this module counts the length of peptide sequences in a input csv file 

(usage: to explain the choice of evalue 100)
'''

import pandas as pd

def read_lee2017(lee_dir):
    df=pd.read_csv(lee_dir, usecols=['ENSG', 'Gene Name', 'ENST', 
                                     'Subcellular Location', 'Query Sequence',
                                     'Alignment Length', 'E Value'])
    lee_list = df.values.tolist()
    seq_list=[]
    #only keep sequences
    for entry in lee_list:
       seq_list.append(entry[4])
      
    return seq_list 

def read_shekari2017():
    dirs=[
            '/Users/yifan/BIOC396/MSMS_BLAST/data_summary/Shekari2017/output_C1_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/data_summary/Shekari2017/output_C23_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/data_summary/Shekari2017/output_CM1_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/data_summary/Shekari2017/output_CM23_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/data_summary/Shekari2017/output_H1_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/data_summary/Shekari2017/output_H23_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/data_summary/Shekari2017/output_L1_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/data_summary/Shekari2017/output_L23_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/data_summary/Shekari2017/output_M1_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/data_summary/Shekari2017/output_M23_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/data_summary/Shekari2017/output_N1_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/data_summary/Shekari2017/output_N23_Shekari2017_parsed.csv']
    
    shekari_list=[]
    for dir in dirs:      
        df=pd.read_csv(dir, usecols=['ENSG', 'Gene Name', 'ENST', 
                                     'Subcellular Location', 'Query Sequence',
                                     'Alignment Length', 'E Value'])
        sublist = df.values.tolist()
        shekari_list=shekari_list +sublist
    seq_list=[]
    for entry in shekari_list:
       seq_list.append(entry[4])
      
    return seq_list 

def count_seq_len(seq_list):
    # generate a dictionary: len - count
    len_count_dic = {}
    for seq in seq_list:
        key = len(seq)
        if key in len_count_dic:
            len_count_dic[key]+=1
        else:
            len_count_dic[key]=1
    return len_count_dic

        
def calculate_percentage(dic):
    #find the total count
    total=0
    for k,v in dic.items():
        total +=v
    newdic={}
    for k,v in dic.items():
        newdic[k] = [v, round(100*(v/total),3)]
    #print(newdic)
    return newdic
    
def printdic(len_count_dic):              
    #print the formatted dic
    print ("{:<30} {:<15} {:<15}".format('PeptideLength','Count', 'Percentage(%)'))

    for k, v in len_count_dic.items():
        count, p = v
        print ("{:<30} {:<15} {:<15}".format(k, count, p) )

if __name__ == "__main__":
    lee_list=read_lee2017('/Users/yifan/BIOC396/MSMS_BLAST/data_summary/Lee2017/output_Lee2017_fig2a_parsed.csv')
    print("Lee2017 \n")
    printdic(calculate_percentage(count_seq_len(lee_list)))
    print("\n\n\n\n")
    read_shekari2017
    s_list=read_shekari2017()
    print("Shekari2017 \n")
    printdic(calculate_percentage(count_seq_len(s_list)))
    
    

