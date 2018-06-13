import numpy as np
import matplotlib.pyplot as plt

from preprocess import data_preprocessed as dt

season_mean=[dt.loc[dt.SEASON==i,:].mean() for i in range(4)]

dt.mean