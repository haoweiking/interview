### 信号量（英语： Semaphore）
信号量（英语： Semaphore）又称为信号量、旗语<br>
是一个同步对象，用于保持在0至指定最大值之间的一个计数值。<br>
* 当线程完成一次对该semaphore对象的等待（wait）时，该计数值减一。
* 当线程完成一次对semaphore对象的释放（release）时，计数值加一。
* 当计数值为0，则线程等待该semaphore对象不再能成功直至该semaphore对象变成signaled状态。
* semaphore对象的计数值大于0，为signaled状态；计数值等于0，为nonsignaled状态。
#### 使用方式1：
```
sem = asyncio.Semaphore(10)

# ... later
async with sem:
    # work with shared resource

```

#### 使用方式2：
```
sem = asyncio.Semaphore(10)

# ... later
await sem.acquire()
try:
    # work with shared resource
finally:
    sem.release()
```

#### 代码实现
```
async_spider_semaphore.py

ps: sem = asyncio.Semaphore(10) # 限制协程数量，避免爬虫量太大触发网站相关安全机制
```