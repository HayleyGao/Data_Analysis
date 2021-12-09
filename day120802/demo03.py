import pandas as pd
import numpy as np


#https://blog.csdn.net/qq_43895215/article/details/120779740



arr1=np.random.randint(100,size=(3,4,5)) # 3个4*5的矩阵
print("out1:\n")
print(arr1)


# 常见x[:,n]就是所有集合的第n个数据
print('out2:\n')
print(arr1[:,0,:])  #与out3效果一致

print('out3:\n')
print(arr1[:,0]) #取所有集合中的第0个数据

print('out4:\n')
print(arr1[0,:]) #取第0个集合中的所有数据


#常见用法x[:,m,n] 取所有数据集的第m到n-1列数据
print('out5:\n')
print(arr1[:,0,3]) # 所有数据集，第0项，第3列

"""
/usr/local/bin/python3 /Users/hayleygao/PycharmProjects/Data_Analysis/day120802/demo03.py
out1:

[[[11 42 65 95 97]
  [16 59 60 91 93]
  [36 89 10 17 79]
  [86 23 37 54 47]]

 [[45 62 59 84  1]
  [44  4  6 22 10]
  [35 41 15 86  1]
  [11 93  6 92 77]]

 [[22 62 53 26 54]
  [53 15 71  2 58]
  [23 95 74 11  9]
  [ 0 98 60 65 28]]]
out2:

[[11 42 65 95 97]
 [45 62 59 84  1]
 [22 62 53 26 54]]
out3:

[[11 42 65 95 97]
 [45 62 59 84  1]
 [22 62 53 26 54]]
out4:

[[11 42 65 95 97]
 [16 59 60 91 93]
 [36 89 10 17 79]
 [86 23 37 54 47]]
out5:

[95 84 26]

"""







