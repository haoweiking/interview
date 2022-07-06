### 1. 多组件的Pipeline技术架构
```
复杂的事情一般都不会一下子做完，而是会分很多中间步骤一步步完成

输入数据-> 处理1 -> 中间数 -> 处理器X很多个 -> 中间数据 -> 处理器N -> 输出数据 -> 
```

### 2. 生产者消费者爬虫的架构
```
待爬取的URL列表 -> 线程组1 网页下载（生产者） -> 现在好的网页队列 -> 线程组2 解析存储（消费者） -> 解析后的结果数据 -> Excel MySQL
```

### 3. 多线程数据通信的queue.Queue
```
queue.Queue 可以用于多线程之间的、线程安全的数据通信

1. 导入类库
import queue

2. 创建Queue
q = queue.Queue()

3. 添加元素
q.put(item)

4. 获取元素
item = q.get()

5. 查询状态
# 查看元素的多少
q.qsize()
# 判断是否为空
q.empty()
# 判断是否已满
q.full()

```

### 4. 代码编写实现生产者消费者爬虫
```
producer_consumer_spider.py
```
