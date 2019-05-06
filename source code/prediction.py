import numpy as np
import pandas as pd
from preprocess import data_preprocessed as dt
year_data=[dt.loc[dt.YEAR==i,:] for i in range(1979,2016)]

max_table=pd.DataFrame(index=list(range(1979,2016)),columns=['max','max^2'])

for i in range(37):
    max_table.iloc[i,0]=year_data[i].max()['HS']
    max_table.iloc[i,1]=max_table.iloc[i,0]**2
    
vbar=max_table.sum()['max']/len(max_table)
sigma=(max_table.sum()['max^2']/len(max_table)-vbar**2)**0.5

lambda_list=[2.153,2.356,2.979,3.598]
max_result=[vbar+i*sigma for i in lambda_list]

with pd.ExcelWriter('prediction.xlsx') as writer:
    max_table.to_excel(writer,sheet_name='max table')
    