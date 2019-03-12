import numpy as np
import pandas as pd
from preprocess import data_preprocessed as dt

dir_list=['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
season_data=[dt.loc[dt.SEASON==i,:] for i in range(4)]


annual_table=pd.DataFrame(np.zeros((len(dir_list),2)),index=dir_list,columns=['NUMBER','PROB'])
winter_table=pd.DataFrame(np.zeros((len(dir_list),2)),index=dir_list,columns=['NUMBER','PROB'])
spring_table=pd.DataFrame(np.zeros((len(dir_list),2)),index=dir_list,columns=['NUMBER','PROB'])
summer_table=pd.DataFrame(np.zeros((len(dir_list),2)),index=dir_list,columns=['NUMBER','PROB'])
autumn_table=pd.DataFrame(np.zeros((len(dir_list),2)),index=dir_list,columns=['NUMBER','PROB'])

for i in dt['WAVEDIR']:
    annual_table.iloc[dir_list.index(i),0]+=1

annual_table['PROB']=[i/len(dt) for i in annual_table['NUMBER']]

season_table=[winter_table,spring_table,summer_table,autumn_table]

for i in range(4):
     for j in season_data[i]['WAVEDIR']:
         season_table[i].iloc[dir_list.index(j),0]+=1
         
winter_table['PROB']=[i/len(season_data[0]) for i in winter_table['NUMBER']]
spring_table['PROB']=[i/len(season_data[1]) for i in spring_table['NUMBER']]
summer_table['PROB']=[i/len(season_data[2]) for i in summer_table['NUMBER']]
autumn_table['PROB']=[i/len(season_data[3]) for i in autumn_table['NUMBER']]


