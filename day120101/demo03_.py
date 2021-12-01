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


"""
运行结果：
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.993
Model:                            OLS   Adj. R-squared:                  0.989
Method:                 Least Squares   F-statistic:                     285.6
Date:                Wed, 01 Dec 2021   Prob (F-statistic):           2.44e-18
Time:                        14:42:54   Log-Likelihood:                -208.39
No. Observations:                  29   AIC:                             436.8
Df Residuals:                      19   BIC:                             450.5
Df Model:                           9                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const        417.5488   4841.391      0.086      0.932   -9715.600    1.06e+04
x1             1.3320      0.111     11.995      0.000       1.100       1.564
x2             1.6602      0.311      5.340      0.000       1.009       2.311
x3             2.2070      0.535      4.129      0.001       1.088       3.326
x4            -0.0630      0.486     -0.130      0.898      -1.079       0.953
x5             1.6803      0.221      7.616      0.000       1.218       2.142
x6             0.0049      0.014      0.341      0.737      -0.025       0.035
x7             0.0054      0.011      0.481      0.636      -0.018       0.029
x8           -17.5237     39.517     -0.443      0.662    -100.234      65.187
x9            -9.0961    160.962     -0.057      0.956    -345.994     327.802
==============================================================================
Omnibus:                        3.988   Durbin-Watson:                   2.417
Prob(Omnibus):                  0.136   Jarque-Bera (JB):                2.599
Skew:                          -0.702   Prob(JB):                        0.273
Kurtosis:                       3.423   Cond. No.                     4.44e+06
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 4.44e+06. This might indicate that there are
strong multicollinearity or other numerical problems.


"""
