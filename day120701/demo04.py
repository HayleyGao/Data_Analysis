import  pandas as pd


#https://blog.csdn.net/qq_36076233/article/details/66969108



df=pd.DataFrame({'date1':['2021/10/11','2021/10/12','2021/10/15','2021/10/18','2021/10/19']})

print(df)
print('--------------------------------')

# print(df.describe())

# print(pd.to_datetime(df['date1']))

df['date1']=pd.to_datetime(df['date1']) # 把时间列标准化格式
print(df['date1'])

df['dayofweek']=df['date1'].dt.dayofweek  # 输出这一天是周中的第几天，Monday=0,Sunday=6,一周[0-6]
print(df['dayofweek'])



# 输出这一天是周几
df['daynameofweek']=df['date1'].dt.day_name()
print(df['daynameofweek'])


