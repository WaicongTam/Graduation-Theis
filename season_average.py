import numpy as np
import pandas as pd

from preprocess import data_preprocessed as dt

years=[]

for i in list(range(1979,2016)):
    years.append(dt.loc[dt.YEAR==i,:])

annual_average=pd.DataFrame([i.mean(axis=0) for i in years])

period_average=pd.DataFrame(columns=['YEAR','ANNUAL','WINTER','SPRING','SUMMER','AUTUMN'])
height_average=pd.DataFrame(columns=['YEAR','ANNUAL','WINTER','SPRING','SUMMER','AUTUMN'])

def season_mean(year):
    season_data=[year.loc[year.SEASON==i,:] for i in range(4)]
    year_season=[(i.mean(axis=0)['Tbar'],i.mean(axis=0)['HS']) for i in season_data]
    return year_season

seasons=[]
for i in years:
    seasons.append(season_mean(i))

height_average['YEAR']=list(range(1979,2016))
period_average['YEAR']=list(range(1979,2016))
height_average['ANNUAL']=annual_average['HS']
period_average['ANNUAL']=annual_average['Tbar']

for i in range(len(period_average)):
    for j in range(2,6):
        period_average.iloc[i,j]=seasons[i][j-2][0]
        height_average.iloc[i,j]=seasons[i][j-2][1]

with pd.ExcelWriter('season_average.xlsx') as writer:
    height_average.to_excel(writer,sheet_name='HS')
    period_average.to_excel(writer,sheet_name='Tbar')