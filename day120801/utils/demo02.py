import  numpy as np
from numpy import  *


#https://blog.csdn.net/qq_38150441/article/details/79893747
# 常见的矩运算


# 相乘
a1=mat([1,2])
a2=mat([[1],[2]])
a3=a1*a2
print(a3)
print(a2)
print(a1)
print('--------------------')
# 矩阵对应元素相乘
a1=mat([1,1]);
a2=mat([2,2]);
a3=multiply(a1,a2)
print(a3)
print('--------------------')

# 矩阵点乘
a1=mat([2,2]);
a2=a1*2>>a2
print(matrix([[4, 4]]))
print('--------------------')

#矩阵求逆，转置
# 矩阵求逆
a1=mat(eye(2,2)*0.5)
print(a1)
print('--------------------')

a2=a1.I  # #求矩阵matrix([[0.5,0],[0,0.5]])的逆矩阵
print(a2)
print('--------------------')

# 矩阵的转置
a1=mat([[1,1],[0,0]])
print(a1)
print('--------------------')

a2=a1.T # 矩阵的转置
print(a2)
