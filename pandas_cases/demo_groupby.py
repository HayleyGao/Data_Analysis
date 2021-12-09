import  pandas as pd
import  numpy as np


# https://www.cnblogs.com/jason--/p/11427145.html
#pandas中的map()、apply()、applymap()函数的区别
#它们的区别就在于应用对象的不同


df=pd.DataFrame({'key1':['a','b','c','d'],'key2':['one','two','three','four'],'data1':np.arange(4),'data2':np.arange(5,9)})
print(df)
print('------------------------')

"""
  key1   key2  data1  data2
0    a    one      0      5
1    b    two      1      6
2    c  three      2      7
3    d   four      3      8
"""

#　map()是Series对象的一个函数，DataFrame中没有map()，map()的功能是将一个自定义函数作用于Series对象的每个元素。

df['data']=df['data1'].map(lambda  x:"%.3f"%x)  # 转为浮点数，精度保持3位。

print(df)
print('------------------------')


#apply()函数的功能是将一个自定义函数作用于DataFrame的行或者列
df['total']=df[['data1','data2']].apply(lambda x:x.sum,axis=1)
print(df)
print('------------------------')


#applymap()函数的功能是将自定义函数作用于DataFrame的所有元素
def add(n):
    return '#' + str(n)
df.applymap(add)
print(df)
print('------------------------')

