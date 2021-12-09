import  pandas as  pd
import numpy as np


df=pd.DataFrame({'key1':['a','b','c','d'],
                 'ke2':['a','b','c','d'],
                 'data1':np.arange(4),
                'data2':np.arange(5,9)})  # arange() 定义坐标轴。
print(df)


# pandas apply的用法
df['total']=df[['data1','data2']].apply(lambda x :x.sum(),axis=1) # axis表示列方向
print(df)

df.loc['total_']=df[['data1','data2']].apply(lambda x:x.sum(),axis=0) # axis表示行方向
print(df)




