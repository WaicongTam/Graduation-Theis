import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from season_average import period_average
from season_average import height_average



def linear_regression(data_x,data_y,own_color):
    model=LinearRegression()
    X=np.array(data_x)
    Y=np.array(data_y)
    model.fit(X.reshape(-1,1),Y)
    plt.plot(X,model.predict(X.reshape(-1,1)),linestyle='--',color=own_color)
    k=model.coef_ 
    b=model.intercept_ 
    return (k,b)

period_1=plt.plot(period_average['YEAR'],period_average['ANNUAL'],marker='o',color='black',label='Annual average period')
period_2=plt.plot(period_average['YEAR'],period_average['WINTER'],marker='s',color='blue',label='Winter average period')
period_3=plt.plot(period_average['YEAR'],period_average['SPRING'],marker='^',color='green',label='Spring average period')
period_4=plt.plot(period_average['YEAR'],period_average['SUMMER'],marker='v',color='yellow',label='Summer average period')
period_5=plt.plot(period_average['YEAR'],period_average['AUTUMN'],marker='+',color='orange',label='Autumn average period')
annual_period_regr=linear_regression(period_average['YEAR'],period_average['ANNUAL'],'black')
winter_period_regr=linear_regression(period_average['YEAR'],period_average['WINTER'],'blue')
spring_period_regr=linear_regression(period_average['YEAR'],period_average['SPRING'],'green')
summer_period_regr=linear_regression(period_average['YEAR'],period_average['SUMMER'],'yellow')
autumn_period_regr=linear_regression(period_average['YEAR'],period_average['AUTUMN'],'orange')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
fig_period = plt.gcf()
fig_period.subplots_adjust(right=0.7)  
fig_period.set_size_inches(16,9)


plt.show()

height_1=plt.plot(height_average['YEAR'],height_average['ANNUAL'],marker='o',color='black',label='Annual average wave height')
height_2=plt.plot(height_average['YEAR'],height_average['WINTER'],marker='s',color='blue',label='Winter average wave height')
height_3=plt.plot(height_average['YEAR'],height_average['SPRING'],marker='^',color='green',label='Spring average wave height')
height_4=plt.plot(height_average['YEAR'],height_average['SUMMER'],marker='v',color='yellow',label='Summer average wave height')
height_5=plt.plot(height_average['YEAR'],height_average['AUTUMN'],marker='+',color='orange',label='Autumn average wave height')
annual_height_regr=linear_regression(height_average['YEAR'],height_average['ANNUAL'],'black')
winter_height_regr=linear_regression(height_average['YEAR'],height_average['WINTER'],'blue')
spring_height_regr=linear_regression(height_average['YEAR'],height_average['SPRING'],'green')
summer_height_regr=linear_regression(height_average['YEAR'],height_average['SUMMER'],'yellow')
autumn_height_regr=linear_regression(height_average['YEAR'],height_average['AUTUMN'],'orange')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
fig_height = plt.gcf()
fig_height.subplots_adjust(right=0.7)  
fig_height.set_size_inches(16,9)

plt.show()
