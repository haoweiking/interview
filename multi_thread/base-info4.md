### 1. 线程安全概念介绍
```
线程安全指某个函数、函数库在多线程环境中被调用时，能够正确地处理多个线程之间的共享变量，使程序功能正确完成。
由于线程的执行随时会发生切换，就造成了不可预料的结果，出现线程不安全

```

### 2. Lock 用于解决线程安全问题
```
用法1： try-finally模式
import threading
lock = threading.Lock()

lock.acquire()
try:
    # do something
finally:
    lock.relaease()

用法2：with模式
import threading
lock = threading.Lock()

with lock:
    # do something
```


### 3. 实力代码演示问题以及解决方案
```
lock_concurrent.py
```
