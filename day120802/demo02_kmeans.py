import numpy as np
import matplotlib.pyplot as plt

#https://blog.csdn.net/qq_37509235/article/details/82925781
#https://www.cnblogs.com/pinard/p/6164214.html



# 两点距离
def distance(e1, e2):
    return np.sqrt((e1[0]-e2[0])**2+(e1[1]-e2[1])**2)


# 集合中心
def means(arr):
    """
    求数组中点的平均值用的。e_avg(avg(x),avg(y))
    :param arr:
    :return:
    """
    return np.array([np.mean([e[0] for e in arr]), np.mean([e[1] for e in arr])])

# arr中距离a最远的元素，用于初始化聚类中心
def farthest(k_arr, arr):
    """
    返回的是个点e1(x,y)
    :param k_arr:
    :param arr:
    :return:
    """
    f = [0, 0]
    max_d = 0
    for e in arr:
        d = 0
        for i in range(k_arr.__len__()):
            d = d + np.sqrt(distance(k_arr[i], e))
        if d > max_d:
            max_d = d
            f = e
    return f

# arr中距离a最近的元素，用于聚类
def closest(a, arr):
    c = arr[1]
    min_d = distance(a, arr[1])
    arr = arr[1:]
    for e in arr:
        d = distance(a, e)
        if d < min_d:
            min_d = d
            c = e
    return c


if __name__=="__main__":
    ## 生成二维随机坐标，手上有数据集的朋友注意，理解arr改起来就很容易了
    ## arr是一个数组，每个元素都是一个二元组，代表着一个坐标
    ## arr形如：[ (x1, y1), (x2, y2), (x3, y3) ... ]
    arr = np.random.randint(100, size=(100, 1, 2))[:, 0, :]  #小于100，100个1*2的随机数，相当于100个点e1(x,y)。

    ## 初始化聚类中心和聚类容器
    m = 5
    r = np.random.randint(arr.__len__() - 1) # r,小于数组length的随机数。作为索引用。
    k_arr = np.array([arr[r]]) # arr[r] 返回的是第r个集合。k_arr是个list。相当于是初始化了一个数组[0,0],一个点的坐标。#初始化，随机选择集合里的一个元素（arr[r]）作为第一个聚类中心放入容器(k_arr)。
    cla_arr = [[]]    #<cluster 聚类>
    for i in range(m-1):  #
        k = farthest(k_arr, arr)  # 求arr中的每一个元素中离质心最远的点
        k_arr = np.concatenate([k_arr, np.array([k])]) # 拼接数组 #np.array()是用来创建数组的。# 第一个点k_arr，选择距离第一个聚类中心最远的一个元素k作为第二个聚类中心放入容器
        cla_arr.append([]) # Q:为什么天津一个空集合？创建容器吗？m个。


    ## 迭代聚类
    n = 20
    cla_temp = cla_arr
    for i in range(n):    # 迭代n次
        for e in arr:    # 把集合里每一个元素聚到最近的类
            ki = 0        # 假定点e距离第一个中心最近
            min_d = distance(e, k_arr[ki])  # ki，表示第i个质心。初始化最小距离.min_d.
            for j in range(1, k_arr.__len__()):   # 求每个点(即点e)到其它质心的距离
                if distance(e, k_arr[j]) < min_d:       # 找到更近的聚类中心
                    min_d = distance(e, k_arr[j])
                    ki = j         #点e距离最近的质心下标换为j。
            cla_temp[ki].append(e) #则在质心ki的聚集容器/聚集簇中放入点e.
        # 迭代更新聚类中心
        for k in range(k_arr.__len__()):
            if n - 1 == i:  # 迭代次数到达时，则不再更新质心集合。
                break
            k_arr[k] = means(cla_temp[k]) # 求平均数更新质心集合。
            cla_temp[k] = []  #初始化聚集容器/聚集簇。

    # 所以，这里有几个点，聚集容器/聚集簇cla_temp，质心的集合k_arr。


    ## 可视化展示
    col = ['HotPink', 'Aqua', 'Chartreuse', 'yellow', 'LightSalmon']
    for i in range(m):
        plt.scatter(k_arr[i][0], k_arr[i][1], linewidth=10, color=col[i])
        plt.scatter([e[0] for e in cla_temp[i]], [e[1] for e in cla_temp[i]], color=col[i])
    plt.show()

