import  pandas as pd

data='''
 userid  mini_amt  amount     date
      1      1000     300 20210501
      1      1000     800 20210511
      1      1000     200 20210521
      2      5000    2400 20210510
      2      5000     500 20210514
      2      5000    1000 20210518
      2      5000    3000 20210529
      2      5000     300 20210531
'''

# df=pd.read_clipboard()
# print(df)


df=pd.DataFrame({'userid':[1,1,1,2,2,2,2,2],'mini_amt':[1000,1000,1000,5000,5000,5000,5000,5000],'amount':[300,800,200,2400,500,1000,3000,300],
                 'date':[20210501,20210511,20210521,20210510,20210514,20210518,20210529,20210531]})
print(df)
print('--------------------------')


df1=df.loc[df.userid == 1].sort_values('date').assign(累积入账=lambda x: x.amount.cumsum())
print(df1)
# pandas中assign() 直接增加或者覆盖pf的列。
print('--------------------------')

def get_date(df):
    # df2=df.loc[df.userid==1].sort_values('date').assign(累积入账=lambda x:x.amount.cumsum()).query('累积入账>=mini_amt').date
    df2=df.loc[df.userid==1].sort_values('date').assign(累积入账=lambda x:x.amount.cumsum()).query('累积入账>=mini_amt').date.iat[0]
    print(df2)
    #cumsum() 没有指定坐标轴的时候，变成累加的一位数组。
    return df2
    print('--------------------------')



df3=df.groupby('userid').apply(get_date(df))
print(df3)
print('--------------------------')

