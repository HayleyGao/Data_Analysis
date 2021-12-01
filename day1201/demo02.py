import numpy as np
import pandas as pd
import statsmodels.api as sm

#https://blog.csdn.net/BF02jgtRS00XKtCx/article/details/108231365



file = r'/Users/hayleygao/PycharmProjects/Data_Analysis/day1201/test_data.xlsx'
data = pd.read_excel(file)

#数据预处理，因为原数据的列标太长，我们要处理一下，去除其中的中文，只留下英文名称
data.columns = ['y', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9']
# print(data)


#生成多元线性模型
x = sm.add_constant(data.iloc[:,1:]) #生成自变量,这里是指去除第一行标题行。
y = data['y'] #生成因变量
model = sm.OLS(y, x) #生成模型
result = model.fit() #模型拟合
# result.summary() #模型描述
print(result.summary())


