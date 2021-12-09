import  pandas as pd

# https://www.cnblogs.com/xxswkl/p/11022832.html
# vaule_counts()函数

"""
value_counts函数用于统计dataframe或series中不同数或字符串出现的次数
ascending=True时,按升序排列.
normalize=True时,可计算出不同字符出现的频率,画柱状图统计时可以用到.
"""

df1=pd.DataFrame({"a":[3,4,5,6,2,3,4,4],"b":[2,4,5,6,5,4,3,4]})
print(df1)
print('---------------')

print(df1.apply(pd.value_counts))
print('---------------')

print(df1['a'].map(df1['a'].value_counts()))
print('---------------')

print(df1['a'].value_counts())
print('---------------')

