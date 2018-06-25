# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 11:10:47 2018

@author: Lenovo
"""

import pandas as pd
data=pd.read_csv("election_data.csv")

noc=data['Name_of_Candidate'].drop_duplicates()
len(noc)

ass_noc=[]


for i in noc:
    ass_no=list(set[data['Assembly_no'][data['Constituency_no']== i]])
    


d1=list(set[(data['Assembly_no'] ['Constituency_no'] >= i)]




df2 = data[(data['Name_of_Candidate'].isin(['Assembly_no']))  & (data['Constituency_no']> 1)]
df2.head()

data.groupby(['Name_of_Candidate','Year','Party'])['Party'].size()

data.groupby(['Name_of_Candidate','Year'])['Year'].size()

data[data['Constituency_no'] > 1].groupby(['Name_of_Candidate','Party'])['Year'].unique()

data.groupby(['Name_of_Candidate','State'])['Year'].size()


data.Name_of_Candidate.unique()

