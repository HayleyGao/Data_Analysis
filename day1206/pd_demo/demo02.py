import time
import pandas as pd
import  numpy as np


#https://blog.csdn.net/bqw18744018044/article/details/80947243


# 定义一个period
p = pd.Period(2007,freq='A-DEC') #表示以12月作为结束的一整年，这里表示从2007-01-01到2017-12-31的全年
# print(p)

"""
Timestamp与Period互相转换
1.通过to_period方法，可以将时间戳(timestamp)索引的Series和DataFrame对象转换为以时期(period)索引.
"""

rng=pd.date_range('1/1/2000',periods=3,freq='M')
ts=pd.Series(np.random.randn(3),index=rng)
print(ts)

"""
2000-01-31    1.042882
2000-02-29   -1.735505
2000-03-31    1.987141
Freq: M, dtype: float64
"""

# rng=pd.date_range('1/1/2000',periods=3,freq='Y') # freq,Y,M,D
# ts=pd.Series(np.random.randn(3),index=rng)
# print(ts)

# rng=pd.date_range('1/1/2000',periods=3,freq='D') # freq,Y,M,D
# ts=pd.Series(np.random.randn(3),index=rng)
# print(ts)


# rng=pd.date_range('1/1/2000',periods=10,freq='D') # freq,Y,M,D;period=个数的意思。
# ts=pd.Series(np.random.randn(10),index=rng)
# print(ts)

print('---------------------------')
pts = ts.to_period()
print(pts)



