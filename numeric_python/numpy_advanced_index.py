# Numpy高级索引
import numpy as np


# 整数数组索引
#创建二维数组
x = np.array([[1,  2],  [3,  4],  [5,  6]])
#[0,1,2]代表行索引;[0,1,0]代表列索引
y = x[[0,1,2],[0,1,0]] 
print (y)

b = np.array([[ 0, 1, 2],
              [ 3, 4, 5],
              [ 6, 7, 8],
              [ 9,10,11]])
r = np.array([[0,0],[3,3]])
c = np.array([[0,2],[0,2]])
#获取四个角的元素
c = b[r,c]
print(c)

d = np.array([[ 0,  1,  2],
              [ 3,  4,  5],
              [ 6,  7,  8],
              [ 9, 10, 11]])
#对行列分别进行切片
e = d[1:4,1:3]
print(e)
#行使用基础索引，对列使用高级索引
f = d[1:4,[1,2]]
#显示切片后结果
print (f)
#对行使用省略号
h=d[...,1:]
print(h)

# 布尔数组索引
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
print (x[x > 6])

a = np.array([np.nan, 1,2,np.nan,3,4,5])
print(a[~np.isnan(a)])

a = np.array([1, 2+6j, 5, 3.5+5j])
print( a[np.iscomplex(a)])

# 花式索引（拓展知识）
x=np.array([1,2,3,4])
print(x[0])

x=np.arange(32).reshape((8,4))
#分别对应 第4行数据、第2行数据、第1行数据、第7行数据项
print (x[[4,2,1,7]])

x=np.arange(32).reshape((8,4))
print (x[[-4,-2,-1,-7]])

x=np.arange(32).reshape((8,4))
print (x[np.ix_([1,5,7,2],[0,3,1,2])])
