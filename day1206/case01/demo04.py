import pandas as pd
import matplotlib.pyplot as plt  # 展示pd.plot()绘制的图像
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


# 时间特征

# 月度时间特征
df['date'] = df['date'].apply(lambda x: pd.to_datetime(x)) # 转换成为datetime
df['date'].groupby(df.date.dt.to_period('M')).count().plot(kind='line') # to_period('M')月度且转换成为索引。kind='line' 折线图
# plt.show()
print('---------------------------')


#周末时间特征
count = df['date'].apply(lambda x: 'Weekday' if x.dayofweek < 5 else 'Weekend').value_counts(normalize=True)
f,ax=plt.subplots(1,1)  # <subplot 决定画布排版><subplot(1,1),生成1*1个画布空间>
sns.barplot(x=count.index,y=count.values,ax=ax,palette='twilight') # 画个条状图
# plt.show()
print('---------------------------')


# 从周内，细化到工作日的每一天
count=df['date'].apply(lambda  x:x.dayofweek).value_counts(normalize=True).sort_index() #
count.index=['Mon','Tue','Wed','Thu','Fir','Sat','Sun']  # 索引
f,ax=plt.subplots(1,1)
sns.barplot(x=count.index,y=count.values,ax=ax,palette='twilight') # seaborn as sns # 条状图
ax.set_title('Cases (%) for each of the week')  # 设置了标题
plt.show()


