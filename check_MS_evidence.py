#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:26:49 2019

@author: yifan
"""

#check_MS_evidence
'''
this module uses the csv file obtained from compare_with_GeTPRA
to analyze the SL prediction in getpra (whether the experimental SL confirms/refutes the wolf psort predicition) 
'''

import pandas as pd

df=pd.read_csv('/Users/yifan/BIOC396/MSMS_BLAST/data_summary/supp_table/supp_table_5-getpra_comparison.csv',       
                usecols=['Ensembl transcript ID', 
                         'Predicted SL','Lee2017 Evidence','Shekari2017 Evidence','Transcript type'])
entry_list=df.values.tolist()


#ENST_dic maps ENST to a 2D array of [getpraSL, leeSL, ShekariSL]
ENST_dic={}
for entry in entry_list:
    ENST_dic[entry[0]]=[[],[],[],[entry[1]]]
for entry in entry_list:
    ENST_dic[entry[0]][0].append(entry[2]) #getra SL
    if entry[3]== 'Inner Mitochondrial Membrane':
        ENST_dic[entry[0]][1].append('m') #lee SL
    #Shekari SL
    if type(entry[4])!= float:
        if entry[4].startswith("C"):
            ENST_dic[entry[0]][2].append("c") 
        elif entry[4].startswith("M"):
            ENST_dic[entry[0]][2].append("m") 
        elif entry[4].startswith("N"):
            ENST_dic[entry[0]][2].append("n") 
                        


MS_evidence_list=[]

for key,value in ENST_dic.items():
    getpra=value[0]
    lee=value[1]
    shekari=value[2]
    MS=lee+shekari
    for sl in getpra:        
        if sl in MS:
            MS_evidence_list.append([key, sl])
            
df2=pd.DataFrame(MS_evidence_list, columns=['Ensembl transcript ID', 'SL with MS evidence'])
df2.to_csv('/Users/yifan/BIOC396/MSMS_BLAST/data_summary/supp_table/supp_table_6-getpra_location_with_MS_evidence.csv', sep=',')
print('A csv file is generated.')

#unique enst
enst_set=set()
for enst, sl in MS_evidence_list:
    enst_set.add(enst)
enst_list=list(enst_set)
df3=pd.DataFrame(enst_list, columns=['Ensembl transcript ID that has SL with MS evidence'])
df3.to_csv('/Users/yifan/BIOC396/MSMS_BLAST/data_summary/supp_table/supp_table_7-unique_enst_list_MS_evidence.csv', sep=',')
print('A second csv file is generated.')
    
            
#for m,n,c locations only: look for the case where m/n/c locations are 
# included in getpra loc entry but not supported by MSMS datasets (for ENSTs covered by MSMS)


not_supported=[]
enst_MS_ctr=0
for key,value in ENST_dic.items():
    getpra=value[0]
    lee=value[1]
    shekari=value[2]
    MS=lee+shekari
    if MS!=[]:
        enst_MS_ctr+=1
    for sl in getpra:   
        
        if sl in ["c","m","n"]:
            if MS != []:
                                
                if sl not in MS:
                    not_supported.append([key, sl])
#                    print(MS)
#                    print("SL is: " ,sl)
#                    print(key)
#                    

df4=pd.DataFrame(not_supported, columns=["Ensembl transcript ID that has SL not supported by MSMS", "SL"])
df4.to_csv('/Users/yifan/BIOC396/MSMS_BLAST/data_summary/supp_table/supp_table_8-getpra_location_without_MS_evidence.csv', sep=',')
print('A third csv file is generated.')
print('enst_MS_ctr is:',enst_MS_ctr)
    
#unique enst
enst_set_without=set()
for enst, sl in not_supported:
    enst_set_without.add(enst)
enst_list_without=list(enst_set_without)
df5=pd.DataFrame(enst_list_without, columns=['Ensembl transcript ID that has SL not supported by MSMS'])
df5.to_csv('/Users/yifan/BIOC396/MSMS_BLAST/data_summary/supp_table/supple_table_9-unique_enst_list_without_MS_evidence.csv', sep=',')
print('A fourth csv file is generated.')
print('Number of unqiue enst without: ', len(enst_set_without))
    

