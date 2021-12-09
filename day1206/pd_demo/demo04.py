import  pandas as pd
import  numpy as np
import time
import matplotlib.pyplot as plt



df = pd.DataFrame(np.random.randn(6, 4),
                  index=pd.date_range('1/1/2000', periods=6),
                  columns=list('ABCD'))
df.plot()
# <matplotlib.axes._subplots.AxesSubplot at 0x7fa4c699b490>
# 会显示折线图


#DataFrame 在绘图时可以指定 x 和 y 轴的列：

df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()
df3['A'] = pd.Series(list(range(len(df))))
df3.plot(x='A', y='B') # 指定 x 和 y 轴内容

plt.show()

