import  numpy as np
from numpy import  *


#https://blog.csdn.net/qq_38150441/article/details/79893747
# 常见的矩运算

# 矩阵的合并
a=mat(ones((2,2)))
print(a)
print('--------------------------')

b=mat(eye(2)) # 生成2维的对角矩阵
print(b)
print('--------------------------')

# 按列合并，即增加行数
c=vstack((a,b))
print(c)
print('--------------------------')

d=hstack((a,b)) # 按行合并，行数不变
print(d)
print('--------------------------')






