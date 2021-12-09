import  pandas as pd
import  numpy as np


# https://www.gairuo.com/p/pandas-duplicated
# pandas 重复值

"""
df.duplicated(subset=None, keep='first')可以返回表示重复行的布尔系列，可以指定列。keep参数确定要标记的重复项（如果有），选项有：

first：将除第一次出现的重复值标记为True，默认。
last：将除最后一次出现的重复值标记为True。
False：将所有重复值标记为True。
"""


df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})
print(df)
print('------------------------------')

print(df.duplicated())
print('------------------------------')

print(df.duplicated(keep='last'))
print('------------------------------')


print(df.duplicated(keep=False))
#通过将keep设置为False，所有重复项都为True。
print('------------------------------')

# 在特定列上查找重复项
print(df.duplicated(subset=['brand']))
print('------------------------------')

# 删除重复值
print(df.drop_duplicates(subset=None,keep='first',inplace=False,ignore_index=False)) # <inplace,原地>
print('------------------------------')

# 删除特定列的重复值
print(df.drop_duplicates(subset=['brand']))


