import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from preprocess import data_preprocessed as dt


year_data=[dt.loc[dt.YEAR==i,:] for i in range(1979,2016)]
season_data=[[year_data[i].loc[year_data[i].SEASON==j,:] for j in range(4)] for i in range(37)]

def division(data):
    border1=data.quantile(0.995)['HS']
    border2=data.quantile(0.99)['HS']
    border3=data.quantile(0.98)['HS']
    above1=data.loc[data.HS>=border1,:]
    above2=data.loc[data.HS>=border2,:]
    above3=data.loc[data.HS>=border3,:]
    return [(above1,border1),(above2,border2),(above3,border3)]

annual_extreme_table=pd.DataFrame(index=list(range(1979,2016)),columns=['0.005','0.01','0.02'])
winter_extreme_table=pd.DataFrame(index=list(range(1979,2016)),columns=['0.005','0.01','0.02'])
spring_extreme_table=pd.DataFrame(index=list(range(1979,2016)),columns=['0.005','0.01','0.02'])
summer_extreme_table=pd.DataFrame(index=list(range(1979,2016)),columns=['0.005','0.01','0.02'])
autumn_extreme_table=pd.DataFrame(index=list(range(1979,2016)),columns=['0.005','0.01','0.02'])
season_extreme_table=[winter_extreme_table,spring_extreme_table,summer_extreme_table,autumn_extreme_table]

for i in range(37):
    for j in range(4):
        for k in range(3):
            annual_extreme_table.iloc[i,k]=division(year_data[i])[k][1]
            season_extreme_table[j].iloc[i,k]=division(season_data[i][j])[k][1]
    

with pd.ExcelWriter('extreme_list.xlsx') as writer:
    annual_extreme_table.to_excel(writer,sheet_name='annual')
    season_extreme_table[0].to_excel(writer,sheet_name='winter')
    season_extreme_table[1].to_excel(writer,sheet_name='spring')
    season_extreme_table[2].to_excel(writer,sheet_name='summer')
    season_extreme_table[3].to_excel(writer,sheet_name='autumn')

def linear_regression(data_x,data_y,own_color):
    model=LinearRegression()
    X=np.array(data_x)
    Y=np.array(data_y)
    model.fit(X.reshape(-1,1),Y)
    plt.plot(X,model.predict(X.reshape(-1,1)),linestyle='--',color=own_color)
    k=model.coef_ 
    b=model.intercept_ 
    return (k,b)

annual_1=plt.plot(list(range(1979,2016)),annual_extreme_table['0.005'],marker='o',color='black',label='Quantile=0.995')
annual_2=plt.plot(list(range(1979,2016)),annual_extreme_table['0.01'],marker='s',color='blue',label='Quantile=0.99')
annual_3=plt.plot(list(range(1979,2016)),annual_extreme_table['0.02'],marker='^',color='green',label='Quantile=0.98')
annual1_regr=linear_regression(list(range(1979,2016)),annual_extreme_table['0.005'],'black')
annual2_regr=linear_regression(list(range(1979,2016)),annual_extreme_table['0.01'],'blue')
annual3_regr=linear_regression(list(range(1979,2016)),annual_extreme_table['0.02'],'green')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
fig_annual = plt.gcf()
fig_annual.subplots_adjust(right=0.7)  
fig_annual.set_size_inches(16,9)
plt.savefig('extreme_annual.png')
plt.show()

winter_1=plt.plot(list(range(1979,2016)),season_extreme_table[0]['0.005'],marker='o',color='black',label='Quantile=0.995')
winter_2=plt.plot(list(range(1979,2016)),season_extreme_table[0]['0.01'],marker='s',color='blue',label='Quantile=0.99')
winter_3=plt.plot(list(range(1979,2016)),season_extreme_table[0]['0.02'],marker='^',color='green',label='Quantile=0.98')
winter1_regr=linear_regression(list(range(1979,2016)),season_extreme_table[0]['0.005'],'black')
winter2_regr=linear_regression(list(range(1979,2016)),season_extreme_table[0]['0.01'],'blue')
winter3_regr=linear_regression(list(range(1979,2016)),season_extreme_table[0]['0.02'],'green')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
fig_winter = plt.gcf()
fig_winter.subplots_adjust(right=0.7)  
fig_winter.set_size_inches(16,9)
plt.savefig('extreme_winter.png')
plt.show()

spring_1=plt.plot(list(range(1979,2016)),season_extreme_table[1]['0.005'],marker='o',color='black',label='Quantile=0.995')
spring_2=plt.plot(list(range(1979,2016)),season_extreme_table[1]['0.01'],marker='s',color='blue',label='Quantile=0.99')
spring_3=plt.plot(list(range(1979,2016)),season_extreme_table[1]['0.02'],marker='^',color='green',label='Quantile=0.98')
spring1_regr=linear_regression(list(range(1979,2016)),season_extreme_table[1]['0.005'],'black')
spring2_regr=linear_regression(list(range(1979,2016)),season_extreme_table[1]['0.01'],'blue')
spring3_regr=linear_regression(list(range(1979,2016)),season_extreme_table[1]['0.02'],'green')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
fig_spring = plt.gcf()
fig_spring.subplots_adjust(right=0.7)  
fig_spring.set_size_inches(16,9)
plt.savefig('extreme_spring.png')
plt.show()

summer_1=plt.plot(list(range(1979,2016)),season_extreme_table[2]['0.005'],marker='o',color='black',label='Quantile=0.995')
summer_2=plt.plot(list(range(1979,2016)),season_extreme_table[2]['0.01'],marker='s',color='blue',label='Quantile=0.99')
summer_3=plt.plot(list(range(1979,2016)),season_extreme_table[2]['0.02'],marker='^',color='green',label='Quantile=0.98')
summer1_regr=linear_regression(list(range(1979,2016)),season_extreme_table[2]['0.005'],'black')
summer2_regr=linear_regression(list(range(1979,2016)),season_extreme_table[2]['0.01'],'blue')
summer3_regr=linear_regression(list(range(1979,2016)),season_extreme_table[2]['0.02'],'green')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
fig_summer = plt.gcf()
fig_summer.subplots_adjust(right=0.7)  
fig_summer.set_size_inches(16,9)
plt.savefig('extreme_summer.png')
plt.show()

autumn_1=plt.plot(list(range(1979,2016)),season_extreme_table[3]['0.005'],marker='o',color='black',label='Quantile=0.995')
autumn_2=plt.plot(list(range(1979,2016)),season_extreme_table[3]['0.01'],marker='s',color='blue',label='Quantile=0.99')
autumn_3=plt.plot(list(range(1979,2016)),season_extreme_table[3]['0.02'],marker='^',color='green',label='Quantile=0.98')
autumn1_regr=linear_regression(list(range(1979,2016)),season_extreme_table[3]['0.005'],'black')
autumn2_regr=linear_regression(list(range(1979,2016)),season_extreme_table[3]['0.01'],'blue')
autumn3_regr=linear_regression(list(range(1979,2016)),season_extreme_table[3]['0.02'],'green')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
fig_autumn = plt.gcf()
fig_autumn.subplots_adjust(right=0.7)  
fig_autumn.set_size_inches(16,9)
plt.savefig('extreme_autumn.png')
plt.show()

