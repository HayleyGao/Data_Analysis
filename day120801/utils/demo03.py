import  numpy as np
from numpy import  *


#https://blog.csdn.net/qq_38150441/article/details/79893747
# 常见的矩运算


#算矩阵对应行列的最大、最小值、和。

a1=mat([[1,1],[2,3],[4,2]])
print(a1)
print('-------------------')

#计算每一列、行的和
a2=a1.sum(axis=0) # 列和，也许简单的来记就是axis=0代表往跨行（down)，而axis=1代表跨列（across)
print(a2)
print('-------------------')

a3=a1.sum(axis=1) # 跨列，行和。
print(a3)
print('-------------------')

a4=sum(a1[1,:]) # 计算第一行所有列的和，这里得到的是一个数值。
print(a4)  ##第0行：1+1；第2行：2+3；第3行：4+2


