import numpy as np
import pandas as pd
from preprocess import data_preprocessed as dt

period_space=list(range(5,17))
height_space=[0,0.5,1,1.5,2,2.5,3]
dir_space=['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
height_index=['0~0.5','0.5~1','1~1.5','1.5~2','2~2.5','2.5~3']
period_index=['5~6','6~7','7~8','8~9','9~10','10~11','11~12','12~13','13~14','14~15','15~16']

def height_dir_distribute(data,space):
    table=np.zeros((len(height_space)-1,len(dir_space)))
    for i in range(len(data)):
        for j in range(len(dir_space)):
            if data.iloc[i,11]==dir_space[j]:
                column=j
                for k in range(len(height_space)-1):
                    if data.iloc[i,9]>=(space[k]) and data.iloc[i,9]<(space[k+1]):
                        row=k
                        table[row,column]+=1
                    else:continue
            else:continue
    table[:,:]/=(len(data)*0.01)
    return pd.DataFrame(table,index=height_index,columns=dir_space)

annual_height_dir=height_dir_distribute(dt,height_space)

season_data=[dt.loc[dt.SEASON==i,:] for i in range(4)]
season_height_dir=[height_dir_distribute(i,height_space) for i in season_data]

def height_period_distribute(data,space1,space2):
    table=np.zeros((len(space2)-1,len(space1)-1))
    for i in range(len(data)):
        for j in range(len(space1)-1):
            if data.iloc[i,8]>=(space1[j]) and data.iloc[i,8]<(space1[j+1]):
                column=j
                for k in range(len(space2)-1):
                    if data.iloc[i,9]>=(space2[k]) and data.iloc[i,9]<(space2[k+1]):
                        row=k
                        table[row,column]+=1
                    else:continue
            else:continue
    table[:,:]/=(len(data)*0.01)
    return pd.DataFrame(table,index=height_index,columns=period_index)

annual_height_period=height_period_distribute(dt,period_space,height_space)
season_height_period=[height_period_distribute(i,period_space,height_space) for i in season_data]

with pd.ExcelWriter('height_dir_codistribution.xlsx') as writer:
    annual_height_dir.to_excel(writer,sheet_name='annual')
    season_height_dir[0].to_excel(writer,sheet_name='winter')
    season_height_dir[1].to_excel(writer,sheet_name='spring')
    season_height_dir[2].to_excel(writer,sheet_name='summer')
    season_height_dir[3].to_excel(writer,sheet_name='autumn')

with pd.ExcelWriter('height_period_codistribution.xlsx') as writer:
    annual_height_period.to_excel(writer,sheet_name='annual')
    season_height_period[0].to_excel(writer,sheet_name='winter')
    season_height_period[1].to_excel(writer,sheet_name='spring')
    season_height_period[2].to_excel(writer,sheet_name='summer')
    season_height_period[3].to_excel(writer,sheet_name='autumn')

