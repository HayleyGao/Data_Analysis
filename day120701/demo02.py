import pandas as pd
import matplotlib.pyplot as plt # 显示pandas绘制的图像
import seaborn as sns
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import warnings
import plotly.offline as pyo

#https://mp.weixin.qq.com/s/p5SO03tKMFU2u93RbidlaQ


df=pd.read_csv(r"/Users/hayleygao/PycharmProjects/Data_Analysis/day120701/data/PoliceKillingsUS.csv",encoding='cp1252')
# print(df.head())

# 转换为时间类型
df['date']=df['date'].apply(lambda x:pd.to_datetime(x))
print(df['date']) # dtype: datetime64[ns]


print(df['date'].dt.to_period('M')) # <period[M],时期>
# Name: date, Length: 2535, dtype: period[M]


# 分组
# 按照日期进行分组，以'M'代表'月份'为单位，统计总数,to_period时期，频率是月份
df['date'].groupby(df['date'].dt.to_period('M')).count().plot(kind='line')
# plt.show()


# 日期-周内-周末
# 这是一个对象
count=df['date'].apply(lambda x:'Weekday' if x.dayofweek<5 else 'Weekend').value_counts(normalize=True)
# value_counts函数用于统计dataframe或series中不同数或字符串出现的次数

f, ax = plt.subplots(1,1) # 一纸多图，fig,ax = plt.subplots(nrows=1, ncols=1) # 生成1*1 个图
sns.barplot(x=count.index,y=count.values,ax=ax,palette='twilight') #<palette,调色板><twilight,暮光>
# plt.show()
print('---------------------------------------------------')

# datetime类中，dayofweek() 展示一周中的第几天。统计次数，排序。
# count=df['date'].apply(lambda x:x.dayofweek).value_counts(normalize=True).sort_index()
# print(count)

# count=df['date'].apply(lambda x:x.dayofweek)
# print(count)
# print('---------------------------------------------------')


count=df['date'].apply(lambda x:x.dayofweek).value_counts(normalize=True)  #(normalize=False)
print(count)
"""
1    0.154241
3    0.149507
6    0.146351
5    0.143984
2    0.141223
0    0.132939
4    0.131755
Name: date, dtype: float64
"""
print('------------------------------------------------')
count.index=['Mon','Tue','Wed','Thu','Fir','Sat','Sun']
print(count)
"""
Mon    0.154241
Tue    0.149507
Wed    0.146351
Thu    0.143984
Fir    0.141223
Sat    0.132939
Sun    0.131755
Name: date, dtype: float64
"""

print('------------------------------------------------')

f,ax=plt.subplots(1,1) # nrows=1,ncolumns=1,生成1*1个图
sns.barplot(x=count.index,y=count.values,ax=ax,palette='twilight')
ax.set_title('Cases (%) for each of the week')
# plt.show()
print('------------------------------------------------')


# 特征分布
# signs_of_mental_illness：是否精神不稳定
# threat_level：威胁等级
# body_camera：警察是否带了随身摄像头
# manner_of_death：死亡方式


count1=df['signs_of_mental_illness'].value_counts(normalize=True)
count2=df['threat_level'].value_counts(normalize=True)
count3=df['body_camera'].value_counts(normalize=True)
count4=df['manner_of_death'].value_counts(normalize=True)

fig,axes=plt.subplots(2,2,figsize=(8,8),sharey=True) # sharey,这个参数是干嘛用的。生成2*2个图

sns.barplot(x=count1.index,y=count1.values,palette='rocket',ax=axes[0,0]) #多个axes时,[0,0]表示第一行、第一列的位置。
axes[0,0].set_title('signs_of_mental_illness (%)')

sns.barplot(x=count2.index,y=count2.values,palette='viridis',ax=axes[0,1])
axes[0,1].set_title('threat_level (%)')

sns.barplot(x=count3.index,y=count3.values,palette='nipy_spectral',ax=axes[1,0])
axes[1,0].set_title('body_camera (%)')

sns.barplot(x=count4.index,y=count4.values,palette='gist_heat',ax=axes[1,1])
axes[1,1].set_title('manner_of_death (%)')

# plt.show()
print('------------------------------------------------')

# count=df['race']
count=df.race.value_counts(normalize=True) # normalize=True 是否显示"计数占比"
print(count)
"""
W    0.513248
B    0.264103
H    0.180769
A    0.016667
N    0.013248
O    0.011966
Name: race, dtype: float64
"""

count.index=['White', 'Black', 'Hispanic', 'Asian', 'Native American', 'Other']
print(count)
"""
White              0.513248
Black              0.264103
Hispanic           0.180769
Asian              0.016667
Native American    0.013248
Other              0.011966
Name: race, dtype: float64
"""

# 用一张图展示出来
f,ax=plt.subplots(1,1,figsize=(8,6))
sns.barplot(y=count.index,x=count.values,palette='Reds_r')
ax.set_title('Total cases for each race (%)')
plt.show()








