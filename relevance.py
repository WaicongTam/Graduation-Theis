import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from math import sqrt
from sklearn.linear_model import LinearRegression
from preprocess import data_preprocessed as dt

season_data=[dt.loc[dt.SEASON==i,:] for i in range(4)]

def linear_regression(data_x,data_y,labelX,labelY,filename):
    model=LinearRegression()
    X=np.array(data_x)
    Y=np.array(data_y)
    r=np.corrcoef(X,Y)
    model.fit(X.reshape(-1,1),Y)
    plt.scatter(X,Y,marker='o',facecolors='none',edgecolors='c')
    plt.plot(X,model.predict(X.reshape(-1,1)),color='orange')
    k=model.coef_ 
    b=model.intercept_
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    plt.savefig(filename)
    plt.show()
    return (k,b,r)
    

HS_WS_annual=linear_regression(dt['HS'],dt['WS'],'wave height,m','wind speed,m/s','hs_ws_annual.png')
HS_WS_winter=linear_regression(season_data[0]['HS'],season_data[0]['WS'],'wave height,m','wind speed,m/s','hs_ws_winter.png')
HS_WS_spring=linear_regression(season_data[1]['HS'],season_data[1]['WS'],'wave height,m','wind speed,m/s','hs_ws_spring.png')
HS_WS_summer=linear_regression(season_data[2]['HS'],season_data[2]['WS'],'wave height,m','wind speed,m/s','hs_ws_summer.png')
HS_WS_autumn=linear_regression(season_data[3]['HS'],season_data[3]['WS'],'wave height,m','wind speed,m/s','hs_ws_autumn.png')

from strong_waves import annual_strong,season_strong
strong_HS_Tbar_annual=linear_regression(annual_strong[0][0]['HS'],annual_strong[0][0]['Tbar'],'wave height,m','wave period,s','strong_hs_tbar_annual.png')
strong_HS_Tbar_winter=linear_regression(season_strong[0][0][0]['HS'],season_strong[0][0][0]['Tbar'],'wave height,m','wave period,s','strong_hs_tbar_winter.png')
strong_HS_Tbar_spring=linear_regression(season_strong[1][0][0]['HS'],season_strong[1][0][0]['Tbar'],'wave height,m','wave period,s','strong_hs_tbar_spring.png')
strong_HS_Tbar_summer=linear_regression(season_strong[2][0][0]['HS'],season_strong[2][0][0]['Tbar'],'wave height,m','wave period,s','strong_hs_tbar_summer.png')
strong_HS_Tbar_autumn=linear_regression(season_strong[3][0][0]['HS'],season_strong[3][0][0]['Tbar'],'wave height,m','wave period,s','strong_hs_tbar_autumn.png')

strong_Tbar_WS_annual=linear_regression(annual_strong[0][0]['Tbar'],annual_strong[0][0]['WS'],'wave period,s','wind speed,m/s','strong_tbar_ws_annual.png')
strong_Tbar_WS_winter=linear_regression(season_strong[0][0][0]['Tbar'],season_strong[0][0][0]['WS'],'wave period,s','wind speed,m/s','strong_tbar_ws_winter.png')
strong_Tbar_WS_spring=linear_regression(season_strong[1][0][0]['Tbar'],season_strong[1][0][0]['WS'],'wave period,s','wind speed,m/s','strong_tbar_ws_spring.png')
strong_Tbar_WS_summer=linear_regression(season_strong[2][0][0]['Tbar'],season_strong[2][0][0]['WS'],'wave period,s','wind speed,m/s','strong_tbar_ws_summer.png')
strong_Tbar_WS_autumn=linear_regression(season_strong[3][0][0]['Tbar'],season_strong[3][0][0]['WS'],'wave period,s','wind speed,m/s','strong_tbar_ws_autumn.png')

strong_HS_WS_annual=linear_regression(annual_strong[0][0]['HS'],annual_strong[0][0]['WS'],'wave height,m','wind speed,m/s','strong_hs_ws_annual.png')
strong_HS_WS_winter=linear_regression(season_strong[0][0][0]['HS'],season_strong[0][0][0]['WS'],'wave height,m','wind speed,m/s','strong_hs_ws_winter.png')
strong_HS_WS_spring=linear_regression(season_strong[1][0][0]['HS'],season_strong[1][0][0]['WS'],'wave height,m','wind speed,m/s','strong_hs_ws_spring.png')
strong_HS_WS_summer=linear_regression(season_strong[2][0][0]['HS'],season_strong[2][0][0]['WS'],'wave height,m','wind speed,m/s','strong_hs_ws_summer.png')
strong_HS_WS_autumn=linear_regression(season_strong[3][0][0]['HS'],season_strong[3][0][0]['WS'],'wave height,m','wind speed,m/s','strong_hs_ws_autumn.png')


