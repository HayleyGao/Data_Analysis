import  pandas as pd
import  numpy as np
from  sklearn.cluster import  KMeans

#https://www.cnblogs.com/fragrant-breeze/p/13287666.html

dat=pd.read_excel(r"/Users/hayleygao/PycharmProjects/Data_Analysis/day1210/case01/data01.xlsx")
print(dat)

# 指定簇的个数，即分成几类

#转置一下
data=dat.T
# print(data)

#去掉id(病例号)这一行
data=data.drop(['病例号'])
print(data)

# 将行索引变更为英文字母
data.index=['a','b','c','d','e','f','g']
print(data)

# # 以列的形式
x = []
for i in range(28):
    x.append(data[i].values.tolist())
X = np.array(x)
print(X)


