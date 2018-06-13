from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from codistribution import *

fig_annual = plt.figure()  
ax1 = fig_annual.add_subplot(111, projection='3d')
X1=[]
Y1=[]
Z1=[]
for i in range(len(period_index)):
    for j in range(len(height_index)):
        X1.append(i)
        Y1.append(j)
        Z1.append(np.array(annual_height_period)[j,i])
ax1.plot_trisurf(X1,Y1,Z1)
plt.xlabel('period, s')
plt.ylabel('wave height, m')
ax1.set_zlabel('probablity')
plt.savefig('annual_height_period.png')
plt.show()

fig_winter = plt.figure()  
ax2 = fig_winter.add_subplot(111, projection='3d')
X2=[]
Y2=[]
Z2=[]
for i in range(len(period_index)):
    for j in range(len(height_index)):
        X2.append(i)
        Y2.append(j)
        Z2.append(np.array(season_height_period[0])[j,i])
ax2.plot_trisurf(X2,Y2,Z2)
plt.xlabel('period, s')
plt.ylabel('wave height, m')
ax2.set_zlabel('probablity')
plt.savefig('winter_height_period.png')
plt.show()

fig_spring = plt.figure()  
ax3 = fig_spring.add_subplot(111, projection='3d')
X3=[]
Y3=[]
Z3=[]
for i in range(len(period_index)):
    for j in range(len(height_index)):
        X3.append(i)
        Y3.append(j)
        Z3.append(np.array(season_height_period[1])[j,i])
ax3.plot_trisurf(X3,Y3,Z3)
plt.xlabel('period, s')
plt.ylabel('wave height, m')
ax3.set_zlabel('probablity')
plt.savefig('spring_height_period.png')
plt.show()

fig_summer = plt.figure()  
ax4 = fig_summer.add_subplot(111, projection='3d')
X4=[]
Y4=[]
Z4=[]
for i in range(len(period_index)):
    for j in range(len(height_index)):
        X4.append(i)
        Y4.append(j)
        Z4.append(np.array(season_height_period[2])[j,i])
ax4.plot_trisurf(X4,Y4,Z4)
plt.xlabel('period, s')
plt.ylabel('wave height, m')
ax4.set_zlabel('probablity')
plt.savefig('summer_height_period.png')
plt.show()

fig_autumn = plt.figure()  
ax5 = fig_autumn.add_subplot(111, projection='3d')
X5=[]
Y5=[]
Z5=[]
for i in range(len(period_index)):
    for j in range(len(height_index)):
        X5.append(i)
        Y5.append(j)
        Z5.append(np.array(season_height_period[3])[j,i])
ax5.plot_trisurf(X5,Y5,Z5)
plt.xlabel('period, s')
plt.ylabel('wave height, m')
ax5.set_zlabel('probablity')
plt.savefig('autumn_height_period.png')
plt.show()

plt.contourf(annual_height_period)
plt.colorbar()
plt.xlabel('period, s')
plt.ylabel('wave height, m')
plt.savefig('annual_height_period_hm.png')
plt.show()

plt.contourf(season_height_period[0])
plt.colorbar()
plt.xlabel('period, s')
plt.ylabel('wave height, m')
plt.savefig('winter_height_period_hm.png')
plt.show()

plt.contourf(season_height_period[1])
plt.colorbar()
plt.xlabel('period, s')
plt.ylabel('wave height, m')
plt.savefig('spring_height_period_hm.png')
plt.show()

plt.contourf(season_height_period[2])
plt.colorbar()
plt.xlabel('period, s')
plt.ylabel('wave height, m')
plt.savefig('summer_height_period_hm.png')
plt.show()

plt.contourf(season_height_period[3])
plt.colorbar()
plt.xlabel('period, s')
plt.ylabel('wave height, m')
plt.savefig('autumn_height_period_hm.png')
plt.show()



