import matplotlib.pyplot as plt
import numpy as np


#https://blog.csdn.net/liulina603/article/details/78676723
# 逻辑回归模型（逻辑回归（Logistic Regression))




def Sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


x = np.arange(-10, 10, 0.1)
h = Sigmoid(x)  # Sigmoid函数
plt.plot(x, h)
plt.axvline(0.0, color='k')  # 坐标轴上加一条竖直的线（0位置）
plt.axhspan(0.0, 1.0, facecolor='1.0', alpha=1.0, ls='dotted')
plt.axhline(y=0.5, ls='dotted', color='k')
plt.yticks([0.0, 0.5, 1.0])  # y轴标度
plt.ylim(-0.1, 1.1)  # y轴范围
plt.show()

