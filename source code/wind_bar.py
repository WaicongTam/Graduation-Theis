from windrose import WindroseAxes
import windrose
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
from preprocess import data_preprocessed as dt

season_data=[dt.loc[dt.SEASON==i,:] for i in range(4)]

HS = dt['WS']
wd = dt['WD']
ax = WindroseAxes.from_ax()
ax.contourf(wd,HS,bins=6,normed=True)

HS = season_data[0]['WS']
wd = season_data[0]['WD']
ax = WindroseAxes.from_ax()
ax.contourf(wd,HS,bins=6,normed=True)

HS = season_data[1]['WS']
wd = season_data[1]['WD']
ax = WindroseAxes.from_ax()
ax.contourf(wd,HS,bins=6,normed=True)

HS = season_data[2]['WS']
wd = season_data[2]['WD']
ax = WindroseAxes.from_ax()
ax.contourf(wd,HS,bins=6,normed=True)

HS = season_data[3]['WS']
wd = season_data[3]['WD']
ax = WindroseAxes.from_ax()
ax.contourf(wd,HS,bins=6,normed=True)