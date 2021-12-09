import  pandas as pd
import  numpy as np


#https://www.gairuo.com/p/pandas-missing-data


df=pd.DataFrame(np.random.randn(5,3),index=['a','c','e','f','h'],columns=['one','two','three']).reindex(['a','b','c','d','e','f','g','h'])
print(df)
print('--------------------------------------')

#np.random.randn(5,3), 生成5行3列的数据。

#
# df1=pd.DataFrame(np.random.randn(5,3),index=['a','c','e','f','h'],columns=['one','two','three'])
# print(df1)


# 缺失值判定
print(df.one.notna()) #返回True、False
print('--------------------------------')

# 是缺失值
print(df.isna())
print('--------------------------------')

#进行筛选
print(df[df.one.notna()]) # 只返回了notno的部分。
print('--------------------------------')

#numpy中的np.nan和np.nan不相等
print(np.nan==np.nan)
print(None==np.nan)
print(None==None)
print('--------------------------------')
print(df.notna)
# print(df['team'].isna())
# print(df['team'].isnull())
print('--------------------------------')


# 缺失值查询
#每列有多少个缺失值
print(df.isnull().sum())
print('--------------------------------')

#每行有多少个缺失值
print(df.isnull().sum(1))
print('--------------------------------')

#总共有多少个缺失值
print(df.isna().sum().sum())
print('--------------------------------')









