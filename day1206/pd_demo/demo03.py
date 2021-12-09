import  pandas as pd
import  numpy as np
import time
import matplotlib.pyplot as plt # 接近pd.plot() 不显示图像的问题。


#https://www.jb51.net/article/140738.htm
#https://www.gairuo.com/p/pandas-plot


#DataFrame 使用 plot 时 x 轴为索引，y 轴为索引对应的多个具体值.
df=pd.DataFrame(np.random.randn(6,4),index=pd.date_range('1/1/2020',periods=6),columns=list('ABCD'))
#参数period=n,次数/个数。DataFrame(data,index,columns)
print(df)


# df.plot()
print(df.plot())
#AxesSubplot(0.125,0.11;0.775x0.77)

plt.show()


#np.random.randn(6,4) 给定维度，生成array.
# （6行4列的一维矩阵）

"""
# 运行结果：
                   A         B         C         D
2020-01-01 -1.355751 -0.746083  0.005989  0.359195
2020-01-02  0.493030 -0.073065  2.838424  0.659935
2020-01-03  0.344783 -0.814842  0.051438 -0.174257
2020-01-04 -1.135453  0.873068  0.870089 -0.796843
2020-01-05  3.712449  1.911825 -0.479993  0.767826
2020-01-06  1.645536  0.136051  0.154165 -0.701493
AxesSubplot(0.125,0.11;0.775x0.77)
"""



