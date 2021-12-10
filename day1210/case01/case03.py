import  pandas as pd
import  numpy as np
from  sklearn.cluster import  KMeans
import  matplotlib.pyplot as plt


#https://www.cnblogs.com/fragrant-breeze/p/13287666.html

dat=pd.read_excel(r"/Users/hayleygao/PycharmProjects/Data_Analysis/day1210/case01/data01.xlsx")
# print(dat)

# 指定簇的个数，即分成几类

#转置一下
data=dat.T
# print(data)

#去掉id(病例号)这一行
data=data.drop(['病例号'])
# print(data)

# 将行索引变更为英文字母
data.index=['a','b','c','d','e','f','g']
# print(data)

# # 以列的形式
x = []
for i in range(28):
    x.append(data[i].values.tolist())
X = np.array(x)
print(X)

km=KMeans(n_clusters=3).fit(X)  # 3个簇
rs_labels=km.labels_        # 这个标签是干嘛用的？
rs_center_ids=km.cluster_centers_

print('rs_labels\n',rs_labels) # 标签结果
print('rs_center_ids\n',rs_center_ids,'\nlen(rs_center_ids)：',len(rs_center_ids)) # 每个类别的中心点，3个簇，3个中心点。

# 描绘各个点
plt.scatter(X[:,0],X[:,1],c=rs_labels,alpha=0.5)

# 描绘质心
# plt.scatter(rs_center_ids[:,0],rs_center_ids[:,1],c='red')

plt.show()

