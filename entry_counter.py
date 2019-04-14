#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:31:16 2019

@author: yifan
"""
#counter


import pandas as pd

#df1=pd.read_excel("/Users/yifan/BIOC396/MSMS_BLAST/data_summary/supp_table/supp_table_2-output_Lee2017_fig2a_parsed.xlsx",
#                 usecols="B:D")
#
# 
#lee_unique_ensg = set(df1.iloc[:,0].values.tolist())
#lee_unique_enst = set(df1.iloc[:,2].values.tolist())
#print(len(lee_unique_ensg)) #468
#print(len(lee_unique_enst)) #1541
#
#
#xls=pd.ExcelFile("/Users/yifan/BIOC396/MSMS_BLAST/data_summary/supp_table/supp_table_3-output_Shekari2017_parsed.xlsx")
#
#df2=pd.read_excel(xls, 'N1', usecols="B:D")
#df3=pd.read_excel(xls, 'N23', usecols="B:D")
#df4=pd.read_excel(xls, 'C1', usecols="B:D")
#df5=pd.read_excel(xls, 'C23', usecols="B:D")
#df6=pd.read_excel(xls, 'M1', usecols="B:D")
#df7=pd.read_excel(xls, 'M23', usecols="B:D")
#
#
#
#shekari_unique_ensg = set(
#        df2.iloc[:,0].values.tolist()+
#        df3.iloc[:,0].values.tolist()+
#        df4.iloc[:,0].values.tolist()+
#        df5.iloc[:,0].values.tolist()+
#        df6.iloc[:,0].values.tolist()+
#        df7.iloc[:,0].values.tolist())
#print(len(shekari_unique_ensg)) #3309
#
#shekari_unique_enst = set(
#        df2.iloc[:,2].values.tolist()+
#        df3.iloc[:,2].values.tolist()+
#        df4.iloc[:,2].values.tolist()+
#        df5.iloc[:,2].values.tolist()+
#        df6.iloc[:,2].values.tolist()+
#        df7.iloc[:,2].values.tolist())
#print(len(shekari_unique_enst)) #14295
#
#
#all_ensg=set(list(lee_unique_ensg)+list(shekari_unique_ensg))
#all_enst=set(list(lee_unique_enst)+list(shekari_unique_enst))
#print(len(all_ensg)) #3449
#print(len(all_enst)) #14750
#



my_df=pd.read_csv('/Users/yifan/BIOC396/MSMS_BLAST/data_summary/supp_table/supp_table_5-getpra_comparison.csv',       
                usecols=['Ensembl transcript ID', 
                         'Predicted SL','Lee2017 Evidence','Shekari2017 Evidence','Transcript type'])
entry_list=df.values.tolist()

#ENST_dic maps ENST to a 2D array of [getpraSL, MSSL]
ENST_dic={}
ctr=0
ctr2=0
for entry in entry_list:
    ENST_dic[entry[0]]=[[],[]]

for entry in entry_list:
    covered=False
    ENST_dic[entry[0]][0].append(entry[2]) #getra SL
    print(entry[3])
    if entry[3]== 'Inner Mitochondrial Membrane':
        ENST_dic[entry[0]][1].append('m') #lee SL
        covered=True
    #Shekari SL
    if type(entry[4])!= float:
        
        if entry[4].startswith("C"):
            ENST_dic[entry[0]][1].append("c") 
            covered=True
        elif entry[4].startswith("M"):
            ENST_dic[entry[0]][1].append("m") 
            covered=True
        elif entry[4].startswith("N"):
            ENST_dic[entry[0]][1].append("n") 
            covered=True
    if covered==True:
        ctr+=1
print(ctr, ' is the number of entries covered by datasets')







