# numpy 数组属性
import numpy as np


a = np.array([[2,4,6],[3,5,7]])
print(a.shape)

a = np.array([[1,2,3],[4,5,6]])
a.shape = (3,2)
print(a)

a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print(b)

#随机生成一个一维数组
c = np.arange(24)
print(c)
print(c.ndim)
#对数组进行变维操作
e = c.reshape(2,4,3)
print(e) 
print(e.ndim)

x = np.array([1,2,3,4,5], dtype = np.int8)
print (x.itemsize)

x = np.array([1,2,3,4,5], dtype = np.int64)
print (x.itemsize)

x = np.array([1,2,3,4,5])
print (x.flags)
