import  pandas as pd
import  numpy as np

#https://www.gairuo.com/p/pandas-dropping-missing
# 缺失值删除


df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})

print(df)
#NaN 和NaT 有什么区别呢？
print('------------------------------')

# 删除所有缺失值的行
print(df.dropna())
print('------------------------------')

# 删除所有缺失值的列
# print(df.dropna(axis='columns'))
print(df.dropna(axis=1))
print('------------------------------')

# 指定列的缺失值删除
print(df.toy.dropna())

