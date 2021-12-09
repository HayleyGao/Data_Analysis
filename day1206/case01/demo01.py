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

data=pd.to_datetime(date)
print(data.dtypes) #datetime64[ns]
print('----------------------------------------')




#将data的所有时间转换为时间戳（此时data数据类型已经是datetime)
data1 = data.apply(lambda x:time.mktime(x.timetuple()))
#x.timetuple()将时间转换为时间元组，提前导入time模块
print(data1)
print('----------------------------------------')



#将data1的所有时间戳转换为可读时间(此时数据类型已经是datetime)：
data2 = data1.apply(lambda x:time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(x)))
#代码含义为：先读取时间戳数据，将其转换为时间元组，在通过格式化时间转换为可读的时间格式
print(data2)
print('----------------------------------------')




