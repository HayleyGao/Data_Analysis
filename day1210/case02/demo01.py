from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


#https://www.cnblogs.com/woyaofei/p/14748354.html

# KMeans聚类算法的SKlearn的实现。

#自己创建数据集
X,Y = make_blobs(n_samples=1000,n_features=2,centers=4)  #<blob n.一点，一滴;一小片，斑点>
#make_blobs创建数据集，参数n_samples代表创建的数据集的个数，
#n_features代表创建数据集的特征个数，
#n_center代表创建数据的中心的个数
#X返回的使数据的个数*特征，Y返回的是属于的类别即标签
print(X)
print('------------------------------------')
print(Y)
print('------------------------------------')


fig = plt.figure(figsize=(20,12))
plt.rcParams['font.family'] = 'KaiTi' # 设置字体样式
plt.rcParams['axes.unicode_minus'] =False
plt.subplot(2,3,1)
colors = ['red','pink','orange','gray','blue','green']
for i in range(4):
    plt.scatter(X[Y==i,0],X[Y==i,1],marker="o",s=8,color=colors[i])
    plt.title("生成的数据集图")
#实例化一个KMeans对象,检测不同n_cluster下的参数
for i in range(2,7):
    cluster = KMeans(n_clusters= i )
    #对对象进行训练拟合
    cluster = cluster.fit(X)
    y_pred = cluster.labels_#获取训练后对象的每个样本的标签
    centtrod = cluster.cluster_centers_
    plt.subplot(2,3,i)
for j in range(i):
    plt.scatter(X[y_pred==j,0],X[y_pred==j,1],marker="o",s=8,color=colors[j])
    plt.scatter(centtrod[:,0],centtrod[:,1],s=28,marker="H",color = "",edgecolors="purple")
    plt.title("分了%d类的数据图"%i)

plt.show()


