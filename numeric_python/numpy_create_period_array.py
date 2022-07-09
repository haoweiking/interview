# numpy创建区间数组
import numpy as np


# numpy.arange()
x = np.arange(8) 
print (x)

x = np.arange(1,10,2) 
print (x)

# numpy.linspace()
#生成10个样本
a = np.linspace(1,10,10)
print(a)

arr = np.linspace(10, 20, 5, endpoint = False) 
print("数组数值范围 ：",arr)  

x = np.linspace(1,2,5, retstep = True)
print(x) 

# numpy.logspace
a = np.logspace(1.0,2.0, num = 10)
print (a)

a = np.logspace(1,10,num = 10, base = 2)
print(a)