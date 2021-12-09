import  pandas as pd
import  numpy as np


#https://www.gairuo.com/p/pandas-filling-missing
# 缺失值填充

df=pd.DataFrame([[np.nan,2,np.nan,0],
                 [3,4,np.nan,1],
                 [np.nan,np.nan,np.nan,5],
                 [np.nan,3,np.nan,4]],columns=list('ABCD'))

print(df)
print('------------------------------------')


#填写值fillna()

#填充为0
print(df.fillna(0))
print('------------------------------------')

#填充为指定字符
print(df.fillna('missing'))
print(df.fillna('暂无'))
print(df.fillna('待补充'))
print('------------------------------------')

# 指定字段填充
# print(df.one.fillna('暂无'))
#AttributeError: 'DataFrame' object has no attribute 'one'

# 只替换第一个
print(df.fillna(0,limit=1))
print('------------------------------------')

# 不同列替换不同的值
values={'A':0,'B':1,'C':2,'D':3}
print(df.fillna(value=values))
