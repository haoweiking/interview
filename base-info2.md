### 1. python 创建多线程的方法
```
1. 准备一个函数
def my_func(a, b):
    do_craw(a, b)

2. 怎样创建一个线程
import threading
t = threading.Thread(target=my_func, args=(100, 200))

3. 启动线程
t.start()

4. 等待结束
t.join()
```

### 2. 改写爬虫程序，变成多线程爬取


### 3. 速度对比：单线程爬虫 VS 多线程爬虫

