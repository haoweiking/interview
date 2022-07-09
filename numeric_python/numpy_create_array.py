# numpy 创建数组
import numpy as np

# numpy.empty()
arr = np.empty((3,2), dtype = int) 
print(arr)

# numpy.zeros()
#默认数据类型为浮点数
a=np.zeros(6)
print(a)
b=np.zeros(6,dtype="complex64" )
print(b)
c = np.zeros((3,3), dtype = [('x', 'i4'), ('y', 'i4')])
#输出x,y，并指定的数据类型
print(c)

# numpy.ones()
arr1 = np.ones((3,2), dtype = int) 
print(arr1)

# numpy.asarray()
l=[1,2,3,4,5,6,7] 
a = np.asarray(l); 
print(type(a)) 
print(a) 

l=[[1,2,3,4,5,6,7],[8,9]] 
a = np.asarray(l); 
print(type(a)) 
print(a) 

# numpy.frombuffer()
#字节串类型
l = b'hello world' 
print(type(l)) 
a = np.frombuffer(l, dtype = "S1") 
print(a) 
print(type(a)) 

# numpy.fromiter()
# 使用 range 函数创建列表对象 
list=range(6)
#生成可迭代对象i
i=iter(list)
#使用i迭代器，通过fromiter方法创建ndarray
array=np.fromiter(i, dtype=float)
print(array)
