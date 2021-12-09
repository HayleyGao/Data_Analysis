import  pandas as pd
import  numpy as np

# https://www.gairuo.com/p/pandas-interpolation
# 插值填充【interplate v.插值，插入】
# Series 和 DataFrame 对象都有interpolate()方法，默认情况下，该函数在缺失值处执行"线性插值"。
# 插值法是根据已知数据点来预测未知数据点，假如你有n个已知条件，就可以求一个n-1次的插值函数P（x），使得P（x）接近未知原函数f（x），
# 并由插值函数预测出你需要的未知点值。而又n个条件求n-1次P（x）的过程，实际上就是求n元一次线性方程组。


s=pd.Series([0,1,np.nan,3])
print(s)
print('--------------------')

print(s.interpolate()) # 线性插值




