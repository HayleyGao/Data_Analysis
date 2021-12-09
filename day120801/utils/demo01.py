import  numpy as np
from numpy import  *


#https://blog.csdn.net/qq_38150441/article/details/79893747

a1=array([1,2,3])
print(a1)

a1=mat(a1)
print(a1)

matrix([1,2,3])
print(shape(a1)) # 1行3列

data1=mat(zeros((3,3))) # 创建一个3*3的零矩阵，矩阵这里zero函数的参数是一个tuple类型(3,3)
print(data1)


data2=mat(ones((2,4)),dtype=int) # 创建一个2*4的1矩阵，使用dtype参数指定类型为int。
print(data2)

data3=mat(random.rand(2,2)) # 使用np中的random模块，创建一个2*2的数组/二维数组，需要将其转换为matrix.
print(data3)

data4=mat(random.randint(10,size=(3,3))) # 生成一个3*3的0-10之间的随机整数矩阵，若需要指定下界可以多加一个参数。
print(data4)

data5=mat(random.randint(2,8,size=(2,5))) ##产生一个2-8之间的随机整数矩阵
print(data5)

data6=mat(eye(2,2,dtype=int)) # 生成一个2*2的对角矩阵
print(data6)

print('---------------------------------------------------')

aa1=[1,2,3]
aa2=mat(diag(aa1)) # 生成一个对角线为1、2、3的对角矩阵
print(aa2)

