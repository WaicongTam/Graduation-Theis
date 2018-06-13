import numpy as np
import pandas as pd
from preprocess import data_preprocessed as dt

season_data=[dt.loc[dt.SEASON==i,:] for i in range(4)]

height_analysis=pd.DataFrame(index=['ANNUAL','WINTER','SPRING','SUMMER','AUTUMN'],columns=['Variance','Skewness','Kurtosis'])
period_analysis=pd.DataFrame(index=['ANNUAL','WINTER','SPRING','SUMMER','AUTUMN'],columns=['Variance','Skewness','Kurtosis'])

height_analysis.iloc[0,0]=dt['HS'].var()
height_analysis.iloc[0,1]=dt['HS'].skew()
height_analysis.iloc[0,2]=dt['HS'].kurt()


period_analysis.iloc[0,0]=dt['Tbar'].var()
period_analysis.iloc[0,1]=dt['Tbar'].skew()
period_analysis.iloc[0,2]=dt['Tbar'].kurt()

for i in range(1,5):
    height_analysis.iloc[i,0]=season_data[i-1]['HS'].var()
    height_analysis.iloc[i,1]=season_data[i-1]['HS'].skew()
    height_analysis.iloc[i,2]=season_data[i-1]['HS'].kurt()
    period_analysis.iloc[i,0]=season_data[i-1]['Tbar'].var()
    period_analysis.iloc[i,1]=season_data[i-1]['Tbar'].skew()
    period_analysis.iloc[i,2]=season_data[i-1]['Tbar'].kurt()
    
with pd.ExcelWriter('advance_stats.xlsx') as writer:
    height_analysis.to_excel(writer,sheet_name='HS')
    period_analysis.to_excel(writer,sheet_name='Tbar')