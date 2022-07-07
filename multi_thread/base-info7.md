### 1. 有了多线程threading，为什么还要用多进程multiprocessing
```
如果遇到了CPU密集型计算，多线程反而会降低执行速度！

虽然有全局解释器锁GIL，但是因为有IO的存在多线程依然可以加速运行

CPU密集型计算，线程的自动切换反而变成了负担，多线程甚至减慢了运行速度

multiprocessing模块就是python为了解决GIL缺陷引入的一个模块，原理是用多进程在多CPU上并行执行
```

### 2. 多进程multiprocessing知识梳理（对比多线程threading）
|语法条目|多线程|多进程|
|:--|:--|:--|
|引入模块|from threading import Thread|from multiprocessing import Process|
|新建<br>启动<br>等待结束|t = Thread(target=func, args=(100,))<br>t.start()<br>t.join()|p = Process(target=f, args=('bob', ))<br>p.start()<br>p.join()|
|数据通信|import queue<br>q = queue.Queue()<br>q.put(item)<br>item = q.get()|from multiprocessing import Queue<br>q = Queue()<br>q.put([42, None, 'hello'])<br>item = q.get()|
|线程安全加锁|from threading import Lock<br>lock = Lock()<br>with lock:<br>    # do something|from multiprocessing import Lock<br>lock = Lock()<br>with lock:<br>    # do something|
|池化技术|from concurrent.futures import ThreadPoolExecutor<br>with ThreadPoolExecutor() as executor:<br>   # 方法1<br> results = executor.map(func, [1,2,3])<br><br>   # 方法2<br> future = executor.submit(func, 1)<br>   result = future.result()|from concurrent.futures import ProcessPoolExecutor<br>with ProcessPoolExecutor() as executor:<br>  # 方法1<br> results = executor.map(func, [1,2,3])<br><br>   # 方法2<br> future = executor.submit(func, 1)<br>   result = future.result()|
---


### 3. 代码实战：单线程、多线程、多进程对比CPU密集计算速度
```
CPU密集型计算： 100次”判断大数字是否是素数“的计算

由于GIL的存在，多线程比单线程计算的还慢，而多进程可以明显加快执行速度
thread_process_cpu_bound.py
```