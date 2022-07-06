### 1. Web服务的架构以及特点
```
web浏览器           ->      web服务器           ->  磁盘文件
Chrome、火狐、IE    <-  python flask/django    ->  数据库
                                              -> 远程服务API

web后台服务的特点：
    1. web服务对响应时间要求非常高，比如要求200MS返回
    2. web服务有大量的依赖IO操作的调用，比如磁盘文件、数据库、远程API
    3. web服务经常需要处理几万人、几百万人的同时请求
```

### 2. 使用线程池ThreadPoolExecutor加速
```
使用线程池ThreadPoolExecutor的好处：
1. 方便将磁盘文件、数据库、远程API的IO调用并发执行
2. 线程池的线程数目不会无限创建（导致系统挂掉），具有防御功能
```

### 3. 代码用Flask实现Web服务并实现加速
```
flask_thread_pool.py
```
