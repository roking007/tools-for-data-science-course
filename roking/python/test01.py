'''
弹簧受力与拉伸长度的关系建模
by Luo Jun QI
'''
import numpy as np
import matplotlib.pyplot as plt

mass = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550] #弹簧下挂的重物质量列表
length = [1.10,2.10,2.85,3.450,4.38,4.88,5.55,6.48,7.70,8.13,9.51] #弹簧的拉伸的长度列表

factor = np.polyfit(mass,length,1) #按一次多项式拟合(线性关系)出多项式各项系数
equation = np.poly1d(factor) #方程式
print("拟合多项式： " ,equation)

plt.plot(mass, length,'rx') #画实验数据点：红色散点

x = np.linspace(0, 600, 50)
plt.plot(x, equation(x)) #画拟合直线
plt.show()
