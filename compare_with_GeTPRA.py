#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:11:13 2019

@author: yifan
"""

#compare_with_GeTPRA

import pandas as pd
import re


def read_getpra(getpra_dir):
    df=pd.read_csv(getpra_dir,delimiter="\t",        
                   usecols=['Entrez gene ID', 'Ensembl gene ID',
                            'Ensembl transcript ID', 'Transcript type',
                            'Predicted SL', 'Experimental evidences on SLs'])
    getpra_list=df.values.tolist()
    #print(getpra_list[0])
    return getpra_list

def read_lee2017(lee_dir):
    df=pd.read_csv(lee_dir, usecols=['ENSG', 'Gene Name', 'ENST', 
                                     'Subcellular Location', 'Query Sequence',
                                     'Alignment Length', 'E Value'])
    lee_list = df.values.tolist()
    #ENST, ENSG without version number
    for entry in lee_list:
        entry[0]= re.search('ENSG\d+[^\.]',entry[0]).group(0)
        entry[2]= re.search('ENST\d+[^\.]',entry[2]).group(0)
        #print(entry)
    return lee_list 

def read_shekari2017():
    dirs=[
            '/Users/yifan/BIOC396/MSMS_BLAST/Shekari2017/output_C1_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/Shekari2017/output_C23_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/Shekari2017/output_CM1_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/Shekari2017/output_CM23_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/Shekari2017/output_H1_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/Shekari2017/output_H23_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/Shekari2017/output_L1_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/Shekari2017/output_L23_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/Shekari2017/output_M1_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/Shekari2017/output_M23_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/Shekari2017/output_N1_Shekari2017_parsed.csv',
            '/Users/yifan/BIOC396/MSMS_BLAST/Shekari2017/output_N23_Shekari2017_parsed.csv']
    shekari_list=[]
    for dir in dirs:      
        df=pd.read_csv(dir, usecols=['ENSG', 'Gene Name', 'ENST', 
                                     'Subcellular Location', 'Query Sequence',
                                     'Alignment Length', 'E Value'])
        sublist = df.values.tolist()
        shekari_list=shekari_list +sublist
        
    #ENST, ENSG without version number
    for entry in shekari_list:
        entry[0]= re.search('ENSG\d+[^\.]',entry[0]).group(0)
        entry[2]= re.search('ENST\d+[^\.]',entry[2]).group(0)
        #print(entry)
    return shekari_list 


def compare_getpra_lee(getpra_list,lee_list):
    coverage_count=0 #getpra entry coverage count, not transcript
    for g_entry in getpra_list:
        inlee=False
        for l_entry in lee_list:
            #compare transcript ID ENST
            if l_entry[2] == g_entry[2]:
                inlee=True
                g_entry.append(l_entry[3]) #subcellular location in lee2017, IMM
                coverage_count+=1
                break
        if inlee==False:
            g_entry.append("N/A")       
    #coverage = (coverage_count / len(getpra_list))    
    return getpra_list, coverage_count

    
def compare_getpra_shekari(getpra_list,shekari_list):
    coverage_count=0 #getpra entry coverage count, not transcript
    for g_entry in getpra_list:
        inshekari=False
        for s_entry in shekari_list:
            #compare transcript ID ENST
            if s_entry[2] == g_entry[2]:
                inshekari=True
                g_entry.append(s_entry[3]) #subcellular location in Shekari2017
                coverage_count+=1
                break
        if inshekari==False:
            g_entry.append("N/A")       
    #coverage = (coverage_count / len(getpra_list))    
    return getpra_list, coverage_count 

def csv_generator(getpra_list, csv_dir):
    
    df=pd.DataFrame(getpra_list, columns=[
            'Entrez gene ID', 'Ensembl gene ID',
            'Ensembl transcript ID', 'Transcript type',
            'Predicted SL', 'Experimental evidences on SLs', 
            'Lee2017 Evidence','Shekari2017 Evidence'])
    df.to_csv(csv_dir, sep=',')
    print('A csv file is generated.')
    
def transcript_coverage_count(csv_dir):
    df=pd.read_csv(csv_dir, usecols=['Entrez gene ID', 'Ensembl gene ID',
            'Ensembl transcript ID', 'Transcript type',
            'Predicted SL', 'Experimental evidences on SLs', 
            'Lee2017 Evidence','Shekari2017 Evidence'])
    mylist = df.values.tolist()
    
    unique_list=[]
    
    for entry in mylist:
        notunique = False
        for unique_entry in unique_list:
            if entry[2] == unique_entry[2]:
                notunique=True
                break
        if notunique==False:
            unique_list.append(entry)
    count=0
    for unique_entry in unique_list:
        if type(unique_entry[6]) is str:
            count+=1
        elif type(unique_entry[7]) is str:
            count+=1
    csv_generator(unique_list, './getpra_comparison_unique.csv')
        
    return count
        

   
if __name__=="__main__":
#    print("Reading from getpra...")
#    getpra_list = read_getpra('/Users/yifan/BIOC396/getpra/getpra_results_publication_version/draft_GeTPRA.txt')
#    print("Reading from Lee2017...")
#    lee_list = read_lee2017('/Users/yifan/BIOC396/MSMS_BLAST/Lee2017/output_Lee2017_fig2a_parsed.csv')
#    print("Comparing getpra with lee...")
#    getpra_lee, gl_coverage_count = compare_getpra_lee(getpra_list,lee_list)
#    print("Reading from Shekari...")
#    shekari_list = read_shekari2017()
#    print("Comparing the three...")
#    getpra_lee_and_shekari, gls_coverage_count=compare_getpra_shekari(getpra_lee, shekari_list)
#    print("Coverage count of getpra entries is "+ str(gls_coverage_count))
#    print("Total number entries in getpra is "+ str(len(getpra_list)))
#    print("Writing a csv output...")
#    csv_generator(getpra_lee_and_shekari,'./getpra_comparison.csv')
#    
    enst_coverage_count=transcript_coverage_count('./getpra_comparison.csv')
    