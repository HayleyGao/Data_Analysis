import  numpy as np
from numpy import  *


#https://blog.csdn.net/qq_38150441/article/details/79893747
# 常见的矩运算

# 计算最大、最小值和索引

a1=mat([[1,1],[2,3],[4,2]])
print(a1)
print('----------------------------')

# print(a1.max())   # 获取整个数组里的最大值
# print(max(a1[:,1]))  # 获取第二列的最大值
# print(a1[1,:].max()) # 获取第二行的最大值
print('----------------------------')

print(np.max(a1,0)) #axis=0代表往跨行（down)，而axis=1代表跨列（across) 获取所有列的最大值，这里使用的是numpy中的max函数
print(np.max(a1,1)) # 获取所有列的最大值，这里使用的是numpy中的max函数
print('----------------------------')

print(np.argmax(a1,0))  #xis=0代表往跨行（down)，而axis=1代表跨列（across) # 计算所有列的最大值对应在该列中的索引。
print(np.argmax(a1[1,:])) # 计算第二行中最大值对应在该行的索引
