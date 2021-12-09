import  pandas as pd

# datetime，批量处理时间

#https://blog.csdn.net/DataCastle/article/details/84323603


"""
三种取值，‘ignore’, ‘raise’, ‘coerce’，默认为raise。

'raise'，则无效的解析将引发异常

'coerce'，那么无效解析将被设置为NaT

'ignore'，那么无效的解析将返回输入值

"""

df=pd.DataFrame({'year':[2015,2016],'month':[2,3],'day':[4,5]})
print(pd.to_datetime(df) )
print('--------------------------------------------------------')
print(df)
print('--------------------------------------------------------')



"""
0   2015-02-04
1   2016-03-05
dtype: datetime64[ns]

# 将字典形式时间转换为可读时间。
"""

print(pd.to_datetime('13000101', format='%Y%m%d', errors='ignore'))
# datetime.datetime(1300, 1, 1, 0, 0)

print(pd.to_datetime('13000101', format='%Y%m%d', errors='coerce'))
# NaT
# 如果日期不符合时间戳限制，则errors ='ignore'将返回原始输入，而不会报错。
# errors='coerce'将强制超出NaT的日期，返回NaT。

"""
通过pandas.read_csv()或者pandas.read_excel()读取文件过后，得到的数据列对应的类型是“object”，这样没法对时间数据处理，
可以用过pd.to_datetime将该列数据转换为时间类型，即datetime。
"""
"""
data.dtypes
# object

data = pd.to_datetime(data)
data.dtypes
# datetime64[ns]
"""



