### 单线程爬虫的执行路径
```
爬取第1个URL -> 爬取第2个URL -> 爬取第3个URL -> 
CPU 等待IO CPU
```

### 协程：在单线程内实现并发
```
核心原理：用一个超级循环（其实就是while true）循环
核心原理：配合IO多路复用原理（IO时CPU可以干其他事情）
```

### Python异步IO库介绍： asyncio
```
import asyncio

# 获取时间循环
loop = asyncio.get_event_loop()

# 定义协程
async def myfunc(url):
    await get_url(url)

# 创建task列表
tasks = [loop.create_task(myfunc(url)) for url in urls]

# 执行爬虫事件列表
loop.run_until_complete(asyncio.wait(tasks))

注意：
    要用在异步IO变成中，依赖的库必须支持异步IO特性

爬虫引用中：
    requests 不支持异步，需要用aiohttp

文件： async_spider.py
```