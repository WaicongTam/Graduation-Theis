import numpy as np
import pandas as pd
from preprocess import data_preprocessed as dt

dir_list=['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']

def division(data):
    border=data.quantile(0.9)['HS']
    above=data.loc[data.HS>=border,:]
    below=data.loc[data.HS<border,:]
    return [(above,below),(above.mean()['HS'],below.mean()['HS'])]

annual_strong=division(dt)
season_data=[dt.loc[dt.SEASON==i,:] for i in range(4)]
season_strong=[division(i) for i in season_data]

def dir_stat(data):
    table_number=np.zeros((len(dir_list),1))
    for i in data['WAVEDIR']:
        table_number[dir_list.index(i),0]+=1
    table_prob=table_number[:,:]/len(data)*100
    return (pd.DataFrame(table_number,index=dir_list),pd.DataFrame(table_prob,index=dir_list))

annual_strong_dir_stat=dir_stat(annual_strong[0][0])
season_strong_dir_stat=[dir_stat(i[0][0]) for i in season_strong]

