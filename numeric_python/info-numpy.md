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
