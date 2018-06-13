import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from month_average import period_monthly_average,height_monthly_average,ws_monthly_average,wavedir_monthly_average

month_index=list(range(1,13))

period_month_plot=plt.plot(month_index,period_monthly_average.iloc[0,:],marker='o',markerfacecolor='orange',linestyle='--',color='steelblue')
my_x_ticks = np.arange(1, 13, 1)
plt.xticks(my_x_ticks)
plt.ylabel('period, s')
plt.xlabel('month')
plt.savefig('period_monthly.png')
plt.show()

height_month_plot=plt.plot(month_index,height_monthly_average.iloc[0,:],marker='o',markerfacecolor='orange',linestyle='--',color='steelblue')
my_x_ticks = np.arange(1, 13, 1)
plt.xticks(my_x_ticks)
plt.ylabel('wave height, m')
plt.xlabel('month')
plt.savefig('height_monthly.png')
plt.show()

wavedir_month_plot=plt.plot(month_index,wavedir_monthly_average.iloc[0,:],marker='o',markerfacecolor='orange',linestyle='--',color='steelblue')
my_x_ticks = np.arange(1, 13, 1)
plt.xticks(my_x_ticks)
plt.ylabel('wave direction, deg')
plt.xlabel('month')
plt.savefig('wavedir_monthly.png')
plt.show()

ws_month_plot=plt.plot(month_index,ws_monthly_average.iloc[0,:],marker='o',markerfacecolor='orange',linestyle='--',color='steelblue')
my_x_ticks = np.arange(1, 13, 1)
plt.xticks(my_x_ticks)
plt.ylabel('wind speed, m/s')
plt.xlabel('month')
plt.savefig('ws_monthly.png')
plt.show()

height_month_plot=plt.plot(month_index,height_monthly_average.iloc[0,:],marker='o',markerfacecolor='orange',linestyle='--',color='steelblue')
ws_month_plot=plt.plot(month_index,ws_monthly_average.iloc[0,:],marker='s',markerfacecolor='blue',linestyle='--',color='grey')
my_x_ticks = np.arange(1, 13, 1)
plt.xticks(my_x_ticks)
plt.ylabel('wave height, m')
plt.xlabel('month')
plt.savefig('height_ws_monthly.png')