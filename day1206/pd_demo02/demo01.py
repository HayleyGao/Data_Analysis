import  pandas as pd
import  numpy as np


#https://www.cnblogs.com/yanmai/p/12989183.html

df=pd.DataFrame({'A':range(1,6),'B':range(10,0,-2),'C C':2}) # range(start,stop,step)
print(df)

"""
   A   B  C C
0  1  10    2
1  2   8    2
2  3   6    2
3  4   4    2
4  5   2    2
"""
print('----------------------------')

print(df.query('B==2')) # 查询B列中值等于2的行记录。
print('----------------------------')


print(df.query('A<B')) # 查询A列数值小于B列的行记录。
print('----------------------------')
print(df[df.A<df.B]) # 查询A列数值小于B列的行记录。
print('----------------------------')


