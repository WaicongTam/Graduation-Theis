import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from preprocess import data_preprocessed as dt
from season_average import period_average
from season_average import height_average

season_data=[dt.loc[dt.SEASON==i,:] for i in range(4)]
 


hist_data=np.histogram(dt['Tbar'],bins=22,range=(5,16))
hist_prob=hist_data[0]/len(dt)
hist_for_bar=[(hist_data[1][i]+hist_data[1][i+1])/2 for i in range(len(hist_data[1])-1)]
width_for_bar=(hist_data[1][1]-hist_data[1][0])
plt.bar(hist_for_bar,height=hist_prob,width=width_for_bar,edgecolor='black')
plt.grid(True,linestyle='--',color='grey')
plt.title('Distribution of average period')
plt.xlabel('Wave period /s')
plt.ylabel('Probability')
plt.savefig('period_annual_hist.png')
plt.show()

hist_data=np.histogram(season_data[0]['Tbar'],bins=22,range=(5,16))
hist_prob=hist_data[0]/len(season_data[0])
hist_for_bar=[(hist_data[1][i]+hist_data[1][i+1])/2 for i in range(len(hist_data[1])-1)]
width_for_bar=(hist_data[1][1]-hist_data[1][0])
plt.bar(hist_for_bar,height=hist_prob,width=width_for_bar,edgecolor='black')
plt.grid(True,linestyle='--',color='grey')
plt.title('Distribution of average period in winter')
plt.xlabel('Wave period /s')
plt.ylabel('Probability')
plt.savefig('period_winter_hist.png')
plt.show()

hist_data=np.histogram(season_data[1]['Tbar'],bins=22,range=(5,16))
hist_prob=hist_data[0]/len(season_data[1])
hist_for_bar=[(hist_data[1][i]+hist_data[1][i+1])/2 for i in range(len(hist_data[1])-1)]
width_for_bar=(hist_data[1][1]-hist_data[1][0])
plt.bar(hist_for_bar,height=hist_prob,width=width_for_bar,edgecolor='black')
plt.grid(True,linestyle='--',color='grey')
plt.title('Distribution of average period in spring')
plt.xlabel('Wave period /s')
plt.ylabel('Probability')
plt.savefig('period_spring_hist.png')
plt.show()

hist_data=np.histogram(season_data[2]['Tbar'],bins=22,range=(5,16))
hist_prob=hist_data[0]/len(season_data[2])
hist_for_bar=[(hist_data[1][i]+hist_data[1][i+1])/2 for i in range(len(hist_data[1])-1)]
width_for_bar=(hist_data[1][1]-hist_data[1][0])
plt.bar(hist_for_bar,height=hist_prob,width=width_for_bar,edgecolor='black')
plt.grid(True,linestyle='--',color='grey')
plt.title('Distribution of average period in summer')
plt.xlabel('Wave period /s')
plt.ylabel('Probability')
plt.savefig('period_summer_hist.png')
plt.show()

hist_data=np.histogram(season_data[3]['Tbar'],bins=22,range=(5,16))
hist_prob=hist_data[0]/len(season_data[3])
hist_for_bar=[(hist_data[1][i]+hist_data[1][i+1])/2 for i in range(len(hist_data[1])-1)]
width_for_bar=(hist_data[1][1]-hist_data[1][0])
plt.bar(hist_for_bar,height=hist_prob,width=width_for_bar,edgecolor='black')
plt.grid(True,linestyle='--',color='grey')
plt.title('Distribution of average period in autumn')
plt.xlabel('Wave period /s')
plt.ylabel('Probability')
plt.savefig('period_autumn_hist.png')
plt.show()


hist_data=np.histogram(dt['HS'],bins=12,range=(0,3))
hist_prob=hist_data[0]/len(dt)
hist_for_bar=[(hist_data[1][i]+hist_data[1][i+1])/2 for i in range(len(hist_data[1])-1)]
width_for_bar=(hist_data[1][1]-hist_data[1][0])
plt.bar(hist_for_bar,height=hist_prob,width=width_for_bar,edgecolor='black')
plt.grid(True,linestyle='--',color='grey')
plt.title('Distribution of wave height')
plt.xlabel('Wave height /m')
plt.ylabel('Probability')
plt.savefig('height_annual_hist.png')
plt.show()

hist_data=np.histogram(season_data[0]['HS'],bins=12,range=(0,3))
hist_prob=hist_data[0]/len(season_data[0])
hist_for_bar=[(hist_data[1][i]+hist_data[1][i+1])/2 for i in range(len(hist_data[1])-1)]
width_for_bar=(hist_data[1][1]-hist_data[1][0])
plt.bar(hist_for_bar,height=hist_prob,width=width_for_bar,edgecolor='black')
plt.grid(True,linestyle='--',color='grey')
plt.title('Distribution of wave height in winter')
plt.xlabel('Wave height /m')
plt.ylabel('Probability')
plt.savefig('height_winter_hist.png')
plt.show()

hist_data=np.histogram(season_data[1]['HS'],bins=12,range=(0,3))
hist_prob=hist_data[0]/len(season_data[1])
hist_for_bar=[(hist_data[1][i]+hist_data[1][i+1])/2 for i in range(len(hist_data[1])-1)]
width_for_bar=(hist_data[1][1]-hist_data[1][0])
plt.bar(hist_for_bar,height=hist_prob,width=width_for_bar,edgecolor='black')
plt.grid(True,linestyle='--',color='grey')
plt.title('Distribution of wave height in spring')
plt.xlabel('Wave height /m')
plt.ylabel('Probability')
plt.savefig('height_spring_hist.png')
plt.show()

hist_data=np.histogram(season_data[2]['HS'],bins=12,range=(0,3))
hist_prob=hist_data[0]/len(season_data[2])
hist_for_bar=[(hist_data[1][i]+hist_data[1][i+1])/2 for i in range(len(hist_data[1])-1)]
width_for_bar=(hist_data[1][1]-hist_data[1][0])
plt.bar(hist_for_bar,height=hist_prob,width=width_for_bar,edgecolor='black')
plt.grid(True,linestyle='--',color='grey')
plt.title('Distribution of wave height in summer')
plt.xlabel('Wave height /m')
plt.ylabel('Probability')
plt.savefig('height_summer_hist.png')
plt.show()

hist_data=np.histogram(season_data[3]['HS'],bins=12,range=(0,3))
hist_prob=hist_data[0]/len((season_data[3]))
hist_for_bar=[(hist_data[1][i]+hist_data[1][i+1])/2 for i in range(len(hist_data[1])-1)]
width_for_bar=(hist_data[1][1]-hist_data[1][0])
plt.bar(hist_for_bar,height=hist_prob,width=width_for_bar,edgecolor='black')
plt.grid(True,linestyle='--',color='grey')
plt.title('Distribution of wave height in autumn')
plt.xlabel('Wave height /m')
plt.ylabel('Probability')
plt.savefig('height_autumn_hist.png')
plt.show()