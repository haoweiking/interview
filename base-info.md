## 多线程 多进程

### 1. 什么是CPU密集型计算、IO密集型计算
##### CPU密集型（CPU-bound）：
```
CPU密集型也叫计算密集型，是指I/O在很短的时间就可以完成，CPU需要大量的计算和处理，特点是CPU占用率相当高
例如：压缩解压缩、加密解密、正则表达式搜索
```
##### IO密集型（I/O bound）：
```
IO密集型只的是系统运作大部分的状况是CPU在等I/O（硬盘、内存）的读/写操作，CPU占用率仍然较低。
例如：文件处理程序、网络爬虫程序、读写数据库程序
```

### 2. 多进程、多线程、多协程的对比
一个进程中可以启动N个线程
一个线程中可以启动N个协程
##### 多进程 Process（multiprocessing）
```
优点：可以利用多核CPU并行运算
缺点：占用资源最多、可启动数目比线程少
适用于：CPU密集型计算
```

##### 多线程 Thread（threading）
```
优点：相比进程，更轻量级、占用资源少
缺点：
    相比进程：多线程只能并发执行，不能利用多CPU（GIL），只能同时使用单个CPU
    相比协程：启动数目有限制，占用内存资源，有线程切换开销
适用于：IO密集型计算、同时运行的任务数目要求不多
```

##### 多协程 Coroutine（asyncio）
```
优点：内存开销最少、启动协程数量最多
缺点：支持的库有限制（aiohttp vs requests）、代码实现复杂
适用于：IO密集型计算、需要超多任务运行、但有现成库支持的场景
```

### 3. 怎么根据任务选择对应技术
```
待执行任务
    任务特点
    CPU密集型->使用多进程 multiprocessing
    IO密集型-> 
        1. 需要超多任务量？
        2. 有现成协程库支持？
        3. 协程实现复杂度可接受？
        否： 使用多线程 threading
        是： 使用多协程 asyncio

```