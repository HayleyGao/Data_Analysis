import  pandas as pd
import  numpy as np
from  sklearn.cluster import  KMeans

#https://www.cnblogs.com/fragrant-breeze/p/13287666.html


X=np.array([[1,2],[1,4],[1,0],[10,2],[10,4],[10,0]]) # 相当于是创建了6个点。

kmeans=KMeans(n_clusters=2,random_state=0).fit(X)  #n_clusters 表示聚集簇的个数，fit() 表示训练模型,random_state 这个参数的意思是？
print(kmeans.labels_) # 这个labelb表示什么意思？
# [1 1 1 0 0 0]


d=kmeans.predict([[0,0],[12,3]]) #predict() 预测，预测什么？ 属于哪个簇还是？
print(d) #[1,0]


print(kmeans.cluster_centers_) # 聚集中心，n_clusters=2 表示有两个簇，则应该是两个点。
"""
[[10.  2.]
 [ 1.  2.]]
"""


