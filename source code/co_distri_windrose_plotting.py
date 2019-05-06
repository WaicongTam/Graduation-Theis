from windrose import WindroseAxes
import windrose
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np

from preprocess import data_preprocessed as dt
season_data=[dt.loc[dt.SEASON==i,:] for i in range(4)]
#Create wind speed and direction variables

HS1 = dt['HS']
wd1 = dt['DMDIR']
ax = WindroseAxes.from_ax()
ax.box(wd1,HS1,bins=6,normed=True,edgecolor='black')
ax._info['table']
ax.set_legend()

HS2 = season_data[0]['HS']
wd2 = season_data[0]['DMDIR']
ax = WindroseAxes.from_ax()
ax.box(wd2,HS2,bins=6,normed=False,edgecolor='black')
ax.set_legend()

HS3 = season_data[1]['HS']
wd3 = season_data[1]['DMDIR']
ax = WindroseAxes.from_ax()
ax.box(wd3,HS3,bins=6,normed=False,edgecolor='black')
ax.set_legend()

HS4 = season_data[2]['HS']
wd4 = season_data[2]['DMDIR']
ax = WindroseAxes.from_ax()
ax.box(wd4,HS4,bins=6,normed=False,edgecolor='black')
ax.set_legend()

HS5 = season_data[3]['HS']
wd5 = season_data[3]['DMDIR']
ax = WindroseAxes.from_ax()
ax.box(wd5,HS5,bins=6,normed=False,edgecolor='black')
ax.set_legend()

