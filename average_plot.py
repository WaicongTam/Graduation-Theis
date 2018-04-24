import matplotlib.pyplot as plt
import numpy as np

from average import period_average
from average import height_average

plt.plot(period_average['YEAR'],period_average['ANNUAL'])
plt.savefig("annual period average.png")  

plt.show()

plt.plot(height_average['YEAR'],height_average['ANNUAL'])
plt.savefig("annual height average.png")  

