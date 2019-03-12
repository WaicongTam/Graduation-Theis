from windrose import WindroseAxes
import windrose
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np

from dir_distribution import annual_table,winter_table,spring_table,summer_table,autumn_table

dir_space=np.arange(0,360,22.5)

ax = WindroseAxes.from_ax()
ax.box(dir_space,winter_table['PROB'],normed=True,bins=6,edgecolor='black')