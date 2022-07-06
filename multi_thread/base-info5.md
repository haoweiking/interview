### 1. 线程池的原理
```
线程的生命周期：
    新建（start）-> 就绪 -> 获取cpu资源 -> 运行 -> run方法执行完 -> 终止
                       <- 失去cpu资源 <-
                                        运行 -> sleep/io -> 阻塞 -> sleep/io结束 -> 就绪

新建线程系统需要分配资源、终止线程系统需要回收资源
如果可以重用线程，则可以减去新建/终止的开销
```

### 2. 使用线程池的好处
```
1. 提升性能：因为减去了大量新建、终止线程的开销，重用了线程资源
2. 适用场景：适合处理突发性大量请求或需要大量线程完成任务、但实际任务处理时间较短
3. 防御功能：能有效避免系统因为创建线程过多，而导致系统负荷过大相应变慢等问题
4. 代码优势：使用线程池的语法比自己新建线程执行线程更加简洁
```

### 3. ThreadPoolExecutor的使用语法
```
from concurrent.futures import ThreadPoolExecutor, as_completed

用法1： map函数，很简单
注意map的结果和入参是顺序对应的
with ThreadPoolExecutor() as pool:
    results = pool.map(craw, urls)

    for result in results:
        print(result)

用法2：future模式，更强大
注意如果用as_completed顺序是不定的
with ThreadPoolExecutor() as pool:
    features = [pool.submit(craw, url) for url in urls]

    for future in futures:
        print(future.result())

    for future in as_completed(futures):
        print(future.result())

```

### 4. 使用线程池改造爬虫程序
```
thread_pool.py
```