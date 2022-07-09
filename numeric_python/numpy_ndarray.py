'''
  NumPy 定义了一个 n 维数组对象，简称 ndarray 对象，它是一个一系列相同类型元素组成的数组集合。
数组中的每个元素都占有大小相同的内存块，您可以使用索引或切片的方式获取数组中的每个元素。

  ndarray 对象有一个 dtype 属性，该属性用来描述元素的数据类型.

  ndarray 对象采用了数组的索引机制，将数组中的每个元素映射到内存块上，并且按照一定的布局对内存块进行排列，
常用的布局方式有两种，即按行或者按列。
'''

import numpy


# 创建ndarray对象
# numpy.array(object, dtype = None, copy = True, order = None,ndmin = 0)
'''
参数说明：
    object 表示一个数组序列
    dtype  可选参数，通过它可以梗概数组的数据类型
    copy   可选参数，表示数组能否被复制，默认是True
    order  以哪种内存布局创建数组，有3个可选值，分别是C（行序列）/F（列序列）/A（默认）
    ndmin  用于指定数组的维度
'''

# 创建一维数组
a = numpy.array([1,2,3])

print(a)

print(type(a))

# 创建多维数组
b = numpy.array([[1,2,3], [4,5,6]])
print(b)

# 将数组中的元素变成复数类型
c = numpy.array([2,4,6,8], dtype="complex")
print(c)

# ndim 查看数组维度
arr = numpy.array([[1,2,3,4], [4,5,6,7],[9,10,11,12]])
print(arr.ndim)

# 使用ndim参数创建不同维度的数组
arr1 = numpy.array([1,2,3,4,5], ndmin=2)
print(arr1)

# reshape 数组变维
e = numpy.array([[1,2], [3,4], [5,6]])
print(e)
e = e.reshape(2, 3)
print('reshape: ', e)
