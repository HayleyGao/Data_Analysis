import  pandas as pd
import  numpy as np


# https://www.gairuo.com/p/pandas-replace
# 数据替换
# Series 中的 replace() 和 DataFrame 中的 replace() 提供了一种高效而灵活的方法。


ser=pd.Series([0.,1.,2.,3.,4.])
print(ser)
print('----------------------')

# 将0替换为5
print(ser.replace(0,5))
print('----------------------')

# 批量替换
print(ser.replace([0,1,2,3,4],[4,3,2,1,0]))
print('----------------------')

print(ser.replace({0:10,1:100}))

