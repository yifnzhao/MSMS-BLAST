#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 10:23:43 2019

@author: yifan
"""

#inputFastaGenerator

''' 
this module extracts all peptide sequences with SL info 
then generates an input fasta file for blast
'''

import pandas as pd



def get_peptides_from_Lee2017_fig2a(file_path):

    ''' returns a list
    list_pep[0] = peptide
    list_pep[1] = subcellular location
    '''
    mylist=[]
    fig2a_df = pd.read_excel(file_path, sheet_name = 'Summary (Fig.2a)')
    for index, row in fig2a_df.iterrows():
        peptides_list=(index, row['Peptide'])
        pep_seq=peptides_list[1]
        mylist.append([pep_seq,'Inner Mitochondrial Membrane'])
    return mylist


def get_peptides_from_Shekari2017_supp2(file_path, sheetname):
    ''' returns a list
    list_pep[0] = peptide
    list_pep[1] = subcellular location (sheet_name)
    '''
    mylist=[]
    mydf= pd.read_excel(file_path, sheet_name=sheetname)
    for index, row in mydf.iterrows():
        peptides_list=(index,row['pep_seq'])
        pep_seq=peptides_list[1]
        mylist.append([pep_seq,sheetname])
    return mylist
    
def unique_peptides(list_pep):
    unique_list=[]
    
    for peptide, loc in list_pep:
        notunique = False
        for uniquepep, loc in unique_list:
            if peptide == uniquepep:
                notunique=True
                break
        if notunique==False:
            unique_list.append([peptide,loc])
    return unique_list
    
    

def write2Fasta(filename,list_pep, sheet_name=""):
    input_file_name='input_'+sheet_name+str(filename)+'.fasta'
    with open(input_file_name,'w') as f:
        for peptide, SL in list_pep:
            f.write(">"+SL +"\n"+ peptide + "\n")
    f.close()
        

        
if __name__=="__main__":
    
    sheetnames_Shekari=['CM (rep1)','CM (rep2)','CM (rep3)',
                        'M (rep1)','M (rep2)','M (rep3)',
                       'C (rep1)','C (rep2)','C (rep3)',
                       'N (rep1)' ,'N (rep2)' ,'N (rep3)',
                       'H (rep1)','H (rep2)','H (rep3)',
                       'L (rep1)','L (rep2)','L (rep3)']
    for sheetname in sheetnames_Shekari:
        
        print("Writing input file...please wait")
        
        list_pep_Shekari=get_peptides_from_Shekari2017_supp2('/Users/yifan/BIOC396/MSMS_data/Shekari2017/Shekari2017_supp_2.xlsx', sheetname)
        unique_list_pep_Shekari=unique_peptides(list_pep_Shekari)
        write2Fasta("Shekari2017_supp2",unique_list_pep_Shekari, sheet_name=sheetname)
        print("A fasta file is generated")
        
        
    #list_pep_Lee=get_peptides_from_Lee2017_fig2a('/Users/yifan/BIOC396/MSMS_data/Lee2017/ja6b10418_si_004.xlsx')
    #write2Fasta("Lee2017_fig2a",list_pep_Lee)
    print("A fasta file is generated")