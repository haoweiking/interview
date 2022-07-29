# numpy使用需求
```
随着数据科学（Data Science，简称 DS，包括大数据分析与处理、大数据存储、数据抓取等分支）的蓬勃发展，像 NumPy、SciPy（Python科学计算库）、Pandas（基于NumPy的数据处理库） 等数据分析库都有了大量的增长，它们都具有较简单的语法格式。

在矩阵乘法与数组形状处理上，NumPy 有着非常不错的性能，再加上 NumPy 的计算速度很快，这些都是 NumPy 成为一款数据分析工具的重要原因。

数组形状可以理解为数组的维度，比如一维数组、二维数组、三维数组等；以二维数组为例，改变数组形状就是交换数组的行和列，也即将数组旋转 90 度。
```
NumPy 可以很便捷高效地处理大量数据，使用 NumPy 做数据处理的优点:
- NumPy 是 Python 科学计算基础库；
- NumPy 可以对数组进行高效的数学运算；
- NumPy 的 ndarray 对象可以用来构建多维数组；
- NumPy 能够执行傅立叶变换与重塑多维数组形状；
- NumPy 提供了线性代数，以及随机数生成的内置函数。

# numpy应用场景
NumPy 通常与 SciPy（Python科学计算库）和 Matplotlib（Python绘图库）等软件包组合使用，这种组合方式被用来广泛地代替 MatLab 的使用。

MatLab 是一款强大的数学计算软件，广泛应用在数据分析、电子通信、深度学习、图像处理、机器视觉、量化金融等领域，但近些年随着 Python 语言的迅猛发展，Python 被看作是一种更适合代替  MatLab 的编程语言。您可以使用 NumPy、SciPy 与 Matplotlib 等 Python 工具包搭建科学计算环境，比如 Anaconda 就是是一个开源的 Python 发行版本，它包含了 Python 、NumPy 等 180 多个科学包及其依赖项。

# Numpy ndarray 对象
```
  NumPy 定义了一个 n 维数组对象，简称 ndarray 对象，它是一个一系列相同类型元素组成的数组集合。
数组中的每个元素都占有大小相同的内存块，您可以使用索引或切片的方式获取数组中的每个元素。

  ndarray 对象有一个 dtype 属性，该属性用来描述元素的数据类型.

  ndarray 对象采用了数组的索引机制，将数组中的每个元素映射到内存块上，并且按照一定的布局对内存块进行排列，
常用的布局方式有两种，即按行或者按列。
```
```
创建ndarray对象
numpy.array(object, dtype = None, copy = True, order = None,ndmin = 0)

参数说明：
    object 表示一个数组序列
    dtype  可选参数，通过它可以梗概数组的数据类型
    copy   可选参数，表示数组能否被复制，默认是True
    order  以哪种内存布局创建数组，有3个可选值，分别是C（行序列）/F（列序列）/A（默认）
    ndmin  用于指定数组的维度
```

## ndim 查看数组维度

## reshape 数组变维

# Numpy 数据类型

|序号|数据类型|语言描述|
|:--:|:--:|:--:|
|1|bool_|布尔型数据类型（True 或者 False）|
|2|int_|默认整数类型，类似于 C 语言中的 long，取值为 int32 或 int64|
|3|intc|和 C 语言的 int 类型一样，一般是 int32 或 int 64|
|4|intp|用于索引的整数类型（类似于 C 的 ssize_t，通常为 int32 或 int64）|
|5|int8|代表与1字节相同的8位整数。值的范围是-128到127。|
|6|int16|代表 2 字节（16位）的整数。范围是-32768至32767。|
|7|int32|代表 4 字节（32位）整数。范围是-2147483648至2147483647。|
|8|int64|表示 8 字节（64位）整数。范围是-9223372036854775808至9223372036854775807。|
|9|uint8|代表1字节（8位）无符号整数。|
|10|uint16|2 字节（16位）无符号整数。|
|11|uint32|4 字节（32位）的无符号整数。|
|12|uint64|8 字节（64位）的无符号整数。|
|13|float_|float64 类型的简写。|
|14|float16|半精度浮点数，包括：1 个符号位，5 个指数位，10个尾数位。|
|15|float32|单精度浮点数，包括：1 个符号位，8 个指数位，23个尾数位。|
|16|float64|双精度浮点数，包括：1 个符号位，11 个指数位，52个尾数位。|
|17|complex_|复数类型，与 complex128 类型相同。|
|18|complex64|表示实部和虚部共享 32 位的复数。|
|19|complex128|表示实部和虚部共享 64 位的复数。|
|20|str_|表示字符串类型|
|21|string_|表示字节串类型|

## 数据类型对象
```
数据类型对象（Data Type Object）又称 dtype 对象，主要用来描述数组元素的数据类型、大小以及字节顺序。同时，它也可以用来创建结构化数据。比如常见的 int64、float32 都是 dtype 对象的实例
```

## 数据类型标识码
**NumPy 中每种数据类型都有一个唯一标识的字符码**
|字符|对应类型|
|:--:|:--:|
|b|代表布尔型|
|i|带符号整型|
|u|无符号整型|
|f|浮点型|
|c|复数浮点型|
|m|时间间隔（timedelta）|
|M|datatime（日期时间）|
|O|Python对象|
|S,a|字节串（S）与字符串（a）|
|U|Unicode|
|V|原始数据（void）|

## 定义结构化数据
**结构化数据使用字段的形式来描述某个对象的特征**

# Numpy 数组属性
## ndarray.shape
shape 属性的返回值一个由数组维度构成的元组
## ndarray.reshape()
调整数组形状
## ndarray.ndim
获取数组的维数
## ndarray.itemsize
返回数组中每个元素的大小（以字节为单位）
## ndarray.flags
返回 ndarray 数组的内存信息，比如 ndarray 数组的存储方式，以及是否是其他数组的副本等

# Numpy 创建数组
## numpy.empty()
numpy.empty() 创建未初始化的数组，可以指定创建数组的形状（shape）和数据类型（dtype），语法格式如下：
```
    numpy.empty(shape, dtype = float, order = 'C')
```
它接受以下参数：
- shape：指定数组的形状；
- dtype：数组元素的数据类型，默认值是值 float；
- order：指数组元素在计算机内存中的储存顺序，默认顺序是“C”(行优先顺序)。

*numpy.empty() 返回的数组带有随机值，但这些数值并没有实际意义。切记 empty 并非创建空数组。*

## numpy.zeros()
该函数用来创建元素均为 0 的数组，同时还可以指定被数组的形状，语法格式如下：
```
numpy. zeros(shape,dtype=float,order="C")
```
|参数名称|	说明描述|
|:--:|:--:|
|shape|	指定数组的形状大小。|
|dtype|	可选项，数组的数据类型|
|order|	“C”代表以行顺序存储，“F”则表示以列顺序存储|
## numpy.ones()
返回指定形状大小与数据类型的新数组，并且新数组中每项元素均用 1 填充
```
numpy.ones(shape, dtype = None, order = 'C')
```
## numpy.asarray()
asarray() 与 array() 类似，但是它比 array() 更为简单。asarray() 能够将一个 Python 序列转化为 ndarray 对象，语法格式如下：
```
numpy.asarray（sequence，dtype = None ，order = None ）
```
它接受下列参数：
- sequence：接受一个 Python 序列，可以是列表或者元组；
- dtype：可选参数，数组的数据类型；
- order：数组内存布局样式，可以设置为 C 或者 F，默认是 C。
## numpy.frombuffer()
表示使用指定的缓冲区创建数组。下面给出了该函数的语法格式：
```
numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
```
它的参数说明如下所示：

- buffer：将任意对象转换为流的形式读入缓冲区；
- dtype：返回数组的数据类型，默认是 float32；
- count：要读取的数据数量，默认为 -1 表示读取所有数据；
- offset：读取数据的起始位置，默认为 0。
## numpy.fromiter()
该方法可以把迭代对象转换为 ndarray 数组，其返回值是一个一维数组。
```
numpy.fromiter(iterable, dtype, count = -1)
```
|参数名称|	描述说明|
|:--:|:--:|
|iterable|	可迭代对象。|
|dtype|	返回数组的数据类型。|
|count|	读取的数据数量，默认为 -1，读取所有数据。|

# Numpy 创建区间数组
## numpy.arange()
使用 arange() 来创建给定数值范围的数组，语法格式如下：
```
numpy.arange(start, stop, step, dtype)
```
|参数名称|	参数说明|
|:--:|:--:|
|start|	起始值，默认是 0。|
|stop|	终止值，注意生成的数组元素值不包含终止值。|
|step|	步长，默认为 1。|
|dtype|	可选参数，指定 ndarray 数组的数据类型。|
根据start与stop指定的范围以及step步长值，生成一个 ndarray 数组
## numpy.linspace()
表示在指定的数值区间内，返回均匀间隔的一维等差数组，默认均分 50 份，语法格式如下：
```
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
```
参数说明如下：
- start：代表数值区间的起始值；
- stop：代表数值区间的终止值；
- num：表示数值区间内要生成多少个均匀的样本。默认值为 50；
- endpoint：默认为 True，表示数列包含 stop 终止值，反之不包含；
- retstep：默认为 True，表示生成的数组中会显示公差项，反之不显示；
- dtype：代表数组元素值的数据类型。
## numpy.logspace
该函数同样返回一个 ndarray 数组，它用于创建等比数组，语法格式如下：
```
np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
```
其中 base 代表对数函数的底数，默认为 10，参数详细说明见下表：
|参数名称|	说明描述|
|:--:|:--:|
|start|	序列的起始值：base**start。|
|stop|	序列的终止值：base**stop。|
|num|	数值范围区间内样本数量，默认为 50。|
|endpoint|	默认为 True 包含终止值，反之不包含。|
|base|	对数函数的 log 底数，默认为10。|
|dtype|	可选参数，指定 ndarray 数组的数据类型。|

# Numpy 索引和切片
```
在 NumPy 中，如果想要访问，或修改数组中的元素，您可以采用索引或切片的方式，比如使用从 0 开始的索引依次访问数组中的元素，这与 Python 的 list 列表是相同的。

NumPy 提供了多种类型的索引方式，常用方式有两种：基本切片与高级索引。
```
## 基本切片
NumPy 内置函数 slice() 可以用来构造切片对象，该函数需要传递三个参数值分别是 start（起始索引）、stop（终止索引） 和 step（步长） ，通过它可以实现从原数组的上切割出一个新数组。
也可以通过冒号来分割切片参数，最终也能获得相同结果。
冒号切片做简单地说明：
- 如果仅输入一个参数，则将返回与索引相对应的元素。 对于上述示例来说[3] 就会返回 3。
- 如果在其前面插入“:”如[:9]，则会返回 0-8 的所有数字（不包含9）。
- 如是 [2:] 则会返回 2-9 之间的数字。
- 如果在两个参数之间，如[2:9]，则对两个索引值之间的所有元素进行切片（不包括停止索引）。
## 多维数组切片
注意：切片还可以使用省略号“…”，如果在行位置使用省略号，那么返回值将包含所有行元素，反之，则包含所有列元素。

# Numpy高级索引
NumPy 与 Python 的内置序列相比，它提供了更多的索引方式。还可以使用高级索引方式，比如整数数组索引、布尔索引以及花式索引。
高级索引返回的是数组的副本（深拷贝），而切片操作返回的是数组视图（浅拷贝）。
## 整数数组索引
整数数组索引，它可以选择数组中的任意一个元素
也可以将切片所使用的:或省略号...与整数数组索引结合使用
## 布尔数组索引
当输出的结果需要经过布尔运算（如比较运算）时，此时会使用到另一种高级索引方式，即布尔数组索引。
```
#返回所有大于6的数字组成的数组
import numpy as np
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
print (x[x > 6])
```
可以使用补码运算符来去除 NaN（即非数字元素）
```
import numpy as np
a = np.array([np.nan, 1,2,np.nan,3,4,5])
print(a[~np.isnan(a))
```
删除数组中整数元素
```
import numpy as np
a = np.array([1, 2+6j, 5, 3.5+5j])
print( a[np.iscomplex(a)])
```
## 花式索引（拓展知识）
花式索引也可以理解为整数数组索引，但是它们之间又略有不同 **花式索引也会生成一个新的副本。**
当原数组是一维数组时，使用一维整型数组作为索引，那么索引结果就是相应索引位置上的元素。
```
import numpy as np
x=np.array([1,2,3,4])
print(x[0])
```
如果原数组是二维数组，那么索引数组也需要是二维的，索引数组的元素值与被索引数组的每一行相对应
```
import numpy as np
x=np.arange(32).reshape((8,4))
#分别对应 第4行数据、第2行数据、第1行数据、第7行数据项
print (x[[4,2,1,7]])
```
也可以使用倒序索引数组
```
import numpy as np
x=np.arange(32).reshape((8,4))
print (x[[-4,-2,-1,-7]])
```
可以同时使用多个索引数组，但这种情况下需要添加 **np.ix_**
```
import numpy as np
x=np.arange(32).reshape((8,4))
print(x[np.ix_([1,5,7,2],[0,3,1,2])])
```
其中 [1,5,7,2] 代表行索引，而 [0,3,1,2] 表示与行索引相对应的列索引值，也就是行中的元素值会按照列索引值排序。比如，第一行元素，未排序前的顺序是 [4,5,6,7]，经过列索引排序后变成了 [4,7,5,6]。
**花式索引 不易理解，不建议过多使用**

# Numpy广播机制
NumPy 中的广播机制（Broadcast）旨在解决不同形状数组之间的算术运算问题
为了保持数组形状相同，NumPy 设计了一种广播机制，这种机制的核心是对形状较小的数组，在横向或纵向上进行一定次数的重复，使其与形状较大的数组拥有相同的维度。
当进行运算的两个数组形状不同，Numpy 会自动触发广播机制.

# Numpy遍历数组
NumPy 提供了一个 nditer 迭代器对象，它可以配合 for 循环完成对数组元素的遍历。

## 遍历顺序
在内存中，Numpy 数组提供了两种存储数据的方式，分别是 C-order（行优先顺序）与 Fortrant-order（列优先顺序）。 nditer 迭代器选择了一种与数组内存布局一致的顺序，之所以这样做，是为了提升数据的访问效率。

在默认情况下，当遍历数组中元素的时候，不需要考虑数组的存储顺序，这一点可以通过遍历上述数组的转置数组来验证。

## 指定遍历顺序
通过 nditer 对象的order参数来指定数组的遍历的顺序
## 修改数组元素值
nditer 对象提供了一个可选参数op_flags，它表示能否在遍历数组时对元素进行修改。它提供了三种模式，如下所示：
1) read-only
只读模式，在这种模式下，遍历时不能修改数组中的元素。
2) read-write
读写模式，遍历时可以修改元素值。
3) write-only
只写模式，在遍历时可以修改元素值。
## 外部循环使用
nditer 对象的构造函数有一个“flags”参数，它可以接受以下参数值（了解即可）：
|参数值|	描述说明|
|:--:|:--:|
|c_index|	可以跟踪 C 顺序的索引。|
|f_index|	可以跟踪 Fortran 顺序的索引。|
|multi_index|	每次迭代都会跟踪一种索引类型。|
|external_loop|	返回的遍历结果是具有多个值的一维数组。|
## 迭代多个数组
如果两个数组都能够被广播，那么 nditer 对象就可以同时对它们迭代。

假设数组 a 的维度是 3*4，另一个数组 b 的维度是 1*4 （即维度较小的数组 b 可以被广播到数组 a 中）

# NumPy相关数组操作
NumPy 中包含了一些处理数组的常用方法，大致可分为以下几类：

- 数组变维操作
- 数组转置操作
- 修改数组维度操作
- 连接与分割数组操作

## 数组变维操作
|函数名称|	函数介绍|
|:--:|:--:|
|reshape|	在不改变数组元素的条件下，修改数组的形状。|
|flat|	返回是一个迭代器，可以用 for 循环遍历其中的每一个元素。|
|flatten|	以一维数组的形式返回一份数组的副本，对副本的操作不会影响到原数组。|
|ravel|	返回一个连续的扁平数组（即展开的一维数组），与 flatten不同，它返回的是数组视图（修改视图会影响原数组）。|

### numpy.ndarray.flat
numpy.ndarray.flat 返回一个数组迭代器
```
import numpy as np
a = np.arange(9).reshape(3,3)
for row in a:
    print (row)
#使用flat属性：
for ele in a.flat:
    print (ele,end="，")
```
### numpy.ndarray.flatten()
返回一份数组副本，对副本修改不会影响原始数组
```
import numpy as np
a = np.arange(8).reshape(2,4)
print (a)
#默认按行C风格展开的数组
print (a.flatten())
#以F风格顺序展开的数组
print (a.flatten(order = 'F'))
```
### numpy.ravel()
将多维数组中的元素以一维数组的形式展开，该方法返回数组的视图（view），如果修改，则会影响原始数组。
```
import numpy as np
a = np.arange(8).reshape(2,4)
print ('原数组：')
print (a)
print ('调用 ravel 函数后：')
print (a.ravel())
print ('F 风格顺序调用 ravel 函数之后：')
print (a.ravel(order = 'F'))
```
## 数组转置操作
|函数名称|	说明|
|:--:|:--:|
|transpose|	将数组的维度值进行对换，比如二维数组维度(2,4)使用该方法后为(4,2)。|
|ndarray.T|	与 transpose 方法相同。|
|rollaxis|	沿着指定的轴向后滚动至规定的位置。|
|swapaxes|	对数组的轴进行对换。|
### numpy.transpose()
用于对换多维数组的维度，比如二维数组使用此方法可以实现矩阵转置
参数说明如下：

- arr：要操作的数组
- axes：可选参数，元组或者整数列表，将会按照该参数进行转置。
```
import numpy as np
a = np.arange(12).reshape(3,4)
print (a)
print (np.transpose(a))
```
### numpy.rollaxis()
该方法表示沿着指定的轴，向后滚动至一个特定位置，格式如下：
```
numpy.rollaxis(arr, axis, start)
```
参数说明：
- arr：要传入的数组；
- axis：沿着哪条轴向后滚动，其它轴的相对位置不会改变；
- start：默认以 0 轴开始，可以根据数组维度调整它的值。

### numpy.swapaxes()
该方法用于交换数组的两个轴，其语法格式如下：
```
numpy.swapaxes(arr, axis1, axis2) 
```
```
import numpy as np
# 创建了三维的 ndarray
a = np.arange(27).reshape(3,3,3)
print (a)
#对换0轴与2轴
print(np.swapaxes(a,2,0))
```
## 修改数组维度操作
|函数名称|	描述说明|
|:--:|:--:|
|broadcast|	生成一个模拟广播的对象。|
|broadcast_to|	将数组广播为新的形状。|
|expand_dims|	扩展数组的形状。|
|squeeze|	从数组的形状中删除一维项。|
### numpy.broadcast()
返回值是数组被广播后的对象，该函数以两个数组作为输入参数
### numpy.broadcast_to()
该函数将数组广播到新形状中，它在原始数组的基础上返回一个只读视图。 如果新形状不符合 NumPy 的广播规则，则会抛出 ValueError 异常。函数的语法格式如下：
```
numpy.broadcast_to(array, shape, subok)
```
### numpy.expand_dims()
在指定位置插入新的轴，从而扩展数组的维度，语法格式如下:
```
numpy.expand_dims(arr, axis)
```
参数说明：
- arr：输入数组
- axis：新轴插入的位置
### numpy.squeeze()
删除数组中维度为 1 的项，例如，一个数组的 shape 是 (5,1)，经此函数后，shape 变为 (5,) 。其函数语法格式如下：
```
numpy.squeeze(arr, axis)
```
参数说明：
- arr：输入数的组；
- axis：取值为整数或整数元组，用于指定需要删除的维度所在轴，指定的维度值必须为 1 ，否则将会报错，若为 None，则删除数组维度中所有为 1 的项。

## 连接与分割数组操作
连接与分割数组是数组的两种操作方式，我们为了便于大家记忆，现将它们的方法整合在一起
|类型|	函数名称|	描述说明|
|:--:|:--:|:--:|
|连接数组方法|	concatenate|	沿指定轴连接两个或者多个相同形状的数组|
|连接数组方法|  stack|	沿着新的轴连接一系列数组|
|连接数组方法|  hstack|	按水平顺序堆叠序列中数组（列方向）|
|连接数组方法|  vstack|	按垂直方向堆叠序列中数组（行方向）|
|分割数组方法|	split|	将一个数组分割为多个子数组|
|分割数组方法|  hsplit|	将一个数组水平分割为多个子数组（按列）|
|分割数组方法|  vsplit|	将一个数组垂直分割为多个子数组（按行）|
### 连接数组操作
沿指定轴连接相同形状的两个或多个数组，格式如下：
```
numpy.concatenate((a1, a2, ...), axis)
```
参数说明：
- a1, a2, ...：表示一系列相同类型的数组；
- axis：沿着该参数指定的轴连接数组，默认为 0。

数组连接操作至少需要两个维度相同的数组，才允许对它们进行垂直或者水平方向上的操作。
### 分割数组操作
沿指定的轴将数组分割为多个子数组，语法格式如下：
```
numpy.split(ary, indices_or_sections, axis)
```
参数说明：

- ary：被分割的数组
- indices_or_sections：若是一个整数，代表用该整数平均切分，若是一个数组，则代表沿轴切分的位置（左开右闭）；
- axis：默认为0，表示横向切分；为1时表示纵向切分。
### hsplit 切分数组
```
np.hsplit(arr1, 3)
#原arr1数组
[[2. 1. 5. 3. 1. 7.]
 [1. 2. 9. 0. 9. 9.]]
#经过水平切分后得到的数组
[array([[2., 1.],[1., 2.]]), 
 array([[5., 3.],[9., 0.]]), 
 array([[1., 7.],[9., 9.]])]]
```

# Numpy数组元素增删改查
|函数名称|	描述说明|
|:--:|:--:|
|resize|	返回指定形状的新数组。|
|append|	将元素值添加到数组的末尾。|
|insert|	沿规定的轴将元素值插入到指定的元素前。|
|delete|	删掉某个轴上的子数组，并返回删除后的新数组。|
|argwhere|	返回数组内符合条件的元素的索引值。|
|unique|	用于删除数组中重复的元素，并按元素值由大到小返回一个新数组。|
## numpy.resize()
numpy.resize() 返回指定形状的新数组。
```
numpy.resize(arr, shape)
```
这里需要区别 resize() 和 reshape() 的使用方法，它们看起来相似，实则不同。resize 仅对原数组进行修改，没有返回值，而 reshape 不仅对原数组进行修改，同时返回修改后的结果。
## numpy.append()
在数组的末尾添加值，它返回一个一维数组。
```
numpy.append(arr, values, axis=None)
```
参数说明：
- arr：输入的数组；
- values：向 arr 数组中添加的值，需要和 arr 数组的形状保持一致；
- axis：默认为 None，返回的是一维数组；当 axis =0 时，追加的值会被添加到行，而列数保持不变，若 axis=1 则与其恰好相反。
## numpy.insert()
表示沿指定的轴，在给定索引值的前一个位置插入相应的值，如果没有提供轴，则输入数组被展开为一维数组。
```
numpy.insert(arr, obj, values, axis)
```
参数说明：
- arr：要输入的数组
- obj：表示索引值，在该索引值之前插入 values 值；
- values：要插入的值；
- axis：指定的轴，如果未提供，则输入数组会被展开为一维数组。
## numpy.delete()
该方法表示从输入数组中删除指定的子数组，并返回一个新数组。它与 insert() 函数相似，若不提供 axis 参数，则输入数组被展开为一维数组。
```
numpy.delete(arr, obj, axis)
```
参数说明：
- arr：要输入的数组；
- obj：整数或者整数数组，表示要被删除数组元素或者子数组；
- axis：沿着哪条轴删除子数组。
## numpy.argwhere()
该函数返回数组中非 0 元素的索引，若是多维数组则返回行、列索引组成的索引坐标。
## numpy.unique()
用于删除数组中重复的元素，其语法格式如下：
```
numpy.unique(arr, return_index, return_inverse, return_counts)
```
参数说明：
- arr：输入数组，若是多维数组则以一维数组形式展开；
- return_index：如果为 True，则返回新数组元素在原数组中的位置（索引）；
- return_inverse：如果为 True，则返回原数组元素在新数组中的位置（索引）；
- return_counts：如果为 True，则返回去重后的数组元素在原数组中出现的次数。

# Numpy 位运算
|序号|	函数|	位运算符|	描述说明|
|:--:|:--:|:--:|:--:|
|1|	bitwise_and|	&|	计算数组元素之间的按位与运算。|
|2|	bitwise_or|	||	计算数组元素之间的按位或运算。|
|3|	invert|	~|	计算数组元素之间的按位取反运算。|
|4|	left_shift|	<<|	将二进制数的位数向左移。|
|5|	right_shift|	>>|	将二进制数的位数向右移。|
## bitwise_and()
该函数对数组中整数的二进制数进行“按位与”运算。
如果两个的二进制数相对应的位都为 1，那么执行位与运算后，该位的结果就为 1，否则就为 0。上述示例：a 与 b 位与运算的结果为 1000，因此它的十进制结果为 8。
## bitwise_or()
对数组中整数的二进制数执行“按位或”运算。
## Invert()
该方法对数组中整数做按位取反运算，也就是 0 变成 1，1 变为 0。若是有符号的负整数，取其二进制数的补码，并执行 +1 操作。
对于有符号二进制数，其最高位为 0， 表示正数；最高位为 1， 表示负数。
## left_shift() 
该方法把数组元素的二进制数向左移动到指定位置，而其返回值所对应的二进制数，则会从右侧追加相等数量的 0（移动了多少位便追加多少个0）。
## right_shift()
将数组中元素的二进制数向右移动到指定位置，其返回值对应的二进制数会从左侧追加相等数量的 0。该函数使用与 left_shift() 恰好相反。

# NumPy字符串处理函数
NumPy 提供了许多字符串处理函数，它们被定义在用于处理字符串数组的 numpy.char 这个类中，这些函数的操作对象是 string_ 或者 unicode_ 字符串数组。
|函数名称|	描述|
|:--:|:--:|
|add()|	对两个数组相应位置的字符串做连接操作。|
|multiply()| 	返回多个字符串副本，比如将字符串“ hello”乘以3，则返回字符串“ hello hello hello”。|
|center()|	用于居中字符串，并将指定的字符，填充在原字符串的左右两侧。|
|capitalize()|	将字符串第一个字母转换为大写。|
|title()|	标题样式，将每个字符串的第一个字母转换为大写形式。|
|lower()|	将数组中所有的字符串的大写转换为小写。|
|upper()| 	将数组中所有的字符串的小写转换为大写。|
|split()| 	通过指定分隔符对字符串进行分割，并返回一个数组序列，默认分隔符为空格。|
|splitlines()| 	以换行符作为分隔符来分割字符串，并返回数组序列。|
|strip()|	删除字符串开头和结尾处的空字符。|
|join()| 	返回一个新的字符串，该字符串是以指定分隔符来连接数组中的所有元素。|
|replace()|	用新的字符串替换原数组中指定的字符串。|
|decode()| 	用指定的编码格式对数组中元素依次执行解码操作。|
|encode()|	用指定的编码格式对数组中元素依次执行编码操作。|

## numpy.char.add()
将两个数组对应位置的字符串元素进行连接
## numpy.char.multiply()
该函数将指定的字符串进行多次拷贝，并将拷贝结果返回
## numpy.char.center()
用于居中字符串，其语法格式如下：
```
np.char.center(string, width, fillchar) 
```
string: 代表字符串，width: 表示长度，fillchar: 要填充的字符
## numpy.char.capitalize()
将字符串的第一个字母转换为大写
## numpy.char.title()
将字符串数组中每个元素的第一个字母转换为大写
## numpy.char.lower()
将字符串数组中每个元素转换为小写
## numpy.char.upper()
将数组中的每个元素转换为大写
## numpy.char.split()
该函数通过指定分隔符对字符串进行分割，并返回数组序列
## numpy.char.splitlines()
以换行符作为分隔符来分割字符串，并返回一个数组序列
## numpy.char.strip() 
用于移除开头或结尾处的空格
## numpy.char.join()
通过指定的分隔符来连接数组中的元素或字符串
## numpy.char.replace() 
使用新字符替换字符串中的指定字符
## numpy.char.encode()与decode()
默认以utf-8的形式进行编码与解码

# NumPy数学函数
NumPy 中包含了大量的数学函数，它们用于执行各种数学运算，其中包括三角函数、舍入函数等等
## 三角函数
NumPy 中提供了用于弧度计算的的 sin()（正弦）、cos()（余弦）和 tan()（正切）三角函数。
```
import numpy as np 
arr = np.array([0, 30, 60, 90, 120, 150, 180]) 
#计算arr数组中给定角度的三角函数值
#通过乘以np.pi/180将其转换为弧度
print(np.sin(arr * np.pi/180)) 
print(np.cos(arr * np.pi/180)) 
print(np.tan(arr * np.pi/180))  
```
NumPy 提供了 arcsin，arcos 和 arctan 反三角函数
```
import numpy as np 
arr = np.array([0, 30, 60, 90]) 
#正弦值数组
sinval = np.sin(arr*np.pi/180) 
print(sinval) 
#计算角度反正弦，返回值以弧度为单位
cosec = np.arcsin(sinval) 
print(cosec) 
#通过degrees函数转化为角度进行验证
print(np.degrees(cosec)) 
#余弦值数组
cosval = np.cos(arr*np.pi/180) 
print(cosval) 
#计算反余弦值，以弧度为单位
sec = np.arccos(cosval) 
print(sec) 
#通过degrees函数转化为角度进行验证
print(np.degrees(sec)) 
#下面是tan()正切函数 
tanval = np.tan(arr*np.pi/180) 
print(tanval) 
cot = np.arctan(tanval) 
print(cot) 
print(np.degrees(cot))  
```
## 舍入函数
### numpy.around() 
该函数返回一个十进制值数，并将数值四舍五入到指定的小数位上。该函数的语法如下：
```
numpy.around(a,decimals)
```
参数说明：
- a：代表要输入的数组；
- decimals：要舍入到的小数位数。它的默认值为0，如果为负数，则小数点将移到整数左侧。
```
import numpy as np 
arr = np.array([12.202, 90.23120, 123.020, 23.202]) 
print(arr) 
print("数组值四舍五入到小数点后两位",np.around(arr, 2)) 
print("数组值四舍五入到小数点后-1位",np.around(arr, -1))  
```
### numpy.floor()
该函数表示对数组中的每个元素向下取整数，即返回不大于数组中每个元素值的最大整数。示例如下：
```
import numpy as np
a = np.array([-1.8,  1.1,  -0.4,  0.9,  18])
#对数组a向下取整
print (np.floor(a))
```
### numpy.ceil()
该函数与 floor 函数相反，表示向上取整。示例如下：
```
import numpy as np
a = np.array([-1.8,  1.1,  -0.4,  0.9,  18])
#对数组a向上取整
print (np.ceil(a))
```
