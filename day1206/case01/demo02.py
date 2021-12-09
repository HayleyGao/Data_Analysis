import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import warnings
import plotly.offline as pyo
# pyo.init_notebook_mode()
# warnings.filterwarnings('ignore')
# pd.set_option('display.max_columns', 500)
# sns.set_style('white')
# # %matplotlib inline
import time


#https://mp.weixin.qq.com/s/p5SO03tKMFU2u93RbidlaQ
#https://blog.csdn.net/DataCastle/article/details/84323603
# pd 对于时间datetime的处理。



df = pd.read_csv('./data/PoliceKillingsUS.csv', encoding='cp1252')
# print(df.head())

# print(df['date'])

date=df['date']
print(date)
#Name: date, Length: 2535, dtype: object
print('----------------------------------------')

date=pd.to_datetime(date) # 转换成为datetime类型
print(date.dtypes) #datetime64[ns]
print('----------------------------------------')


# print(date.dt.to_period('M'))
#Name: date, Length: 2535, dtype: period[M]
# 通过to_period方法，可以将时间戳(timestamp)索引的Series和DataFrame对象转换为以时期(period)索引


# date.groupby(date.dt.to_period('M')).count().plot(kind='line')
# groupby分组,count统计数据的数量,plot()画图‘line’ : line plot (default)#折线图



date.plot()




