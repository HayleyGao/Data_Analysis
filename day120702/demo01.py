import  pandas as pd
import  numpy as np


#https://www.gairuo.com/p/pandas-missing-data


df=pd.DataFrame(np.random.randn(5,3),index=['a','c','e','f','h'],columns=['one','two','three']).reindex(['a','b','c','d','e','f','g','h'])
print(df)
print('--------------------------------------')

#np.random.randn(5,3), 生成5行3列的数据。


df1=pd.DataFrame(np.random.randn(5,3),index=['a','c','e','f','h'],columns=['one','two','three'])
print(df1)



