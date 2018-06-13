import numpy as np
import pandas as pd
from preprocess import data_preprocessed as dt
import matplotlib.pyplot as plt

description=dt.describe()

period_space=list(range(5,17))
height_space=[0,0.5,1,1.5,2,2.5,3]

def distribute(data,space,variable):
    table=np.zeros((1,len(space)-1))
    for i in data[variable]:
        for j in range(len(space)-1):
            if i>=(space[j]) and i<(space[j]+1):
                table[0,j]+=1
            else:continue
    return table

annual_period=distribute(dt,period_space,'Tbar')
annual_height=distribute(dt,height_space,'HS')

season_data=[dt.loc[dt.SEASON==i,:] for i in range(4)]

season_period=[distribute(i,period_space,'Tbar') for i in season_data]
season_height=[distribute(i,height_space,'HS') for i in season_data]

plt.hist(annual_period)
plt.show()