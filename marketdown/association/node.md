# 协程
- 参考资料
    - http://python.jobbole.com/86481/
    - http://python.jobbole.com/87310/
    - https://segmentfault.com/a/1190000009781688
# 迭代器
- 可迭代（Iterable）：直接作用于for循环的变量
- 迭代器（Iterator）：不但可以作用与for循环，开可以被next调用
- list是点醒的可迭代对象，但不是迭代器
- 通过isinstance判断
- iterable和iterator可以转换
    - 通过iter函数
# 生成器
- generator：一边循环一边计算下一个元素的机制/算法
- 需要满足三个条件：
    - 每次调用都生产出for循环需要的下一个元素
    - 如果达到最后一个后，爆出StopIteration异常
    - 可以被next函数调用
- 如何生成一个生成器
    - 直接使用
    - 如果函数中包含yield，则这个函数就叫做生成器
    - next调用函数，遇到yield返回
# 协程
- 历史历程
    - 3.4引入协程，用yield实现
    - 3.5引入协程语法
    - 实现的协程比较好的包有asyncio，tornado，gevent
- 定义：协程 是为非抢占式多任务产生子程序的计算机程序组件，协程允许不同入口点在不同位置暂停或开始执行程序
- 从技术角度讲，协程就是一个你可以暂停执行的函数，或者干脆理解成生成器0
- 协程的实现：
    - yield返回
    - send调用
- 协程的四个状态
    - inspect.getgeneratorstate(…) 函数确定，该函数会返回下述字符串中的一个：
    - GEN_CREATED：等待开始执行
    - GEN_RUNNING：解释器正在执行
    - GEN_SUSPENED：在yield表达式处暂停
    - GEN_CLOSED：执行结束
    - next预激（prime)
- 协程终止
    - 协程中未处理的异常会向上冒泡，传给nex函数或者send函数的调用方（即触发协程的对象）
    - 终止协程的一种方式：发送某个哨符值，让协程退出，内置的None 和Ellipsis等常量经常作哨符值==。
- yield from
    - 调用协程为了得到返回值，协程必须正常终止
    - 生成器正常终止会发出StopIteration异常，异常对象的value属性保存返回值
    - yield from从内部捕获StopIteration异常
    - 委派生成器
        - 包含yield from表达式的生成器函数
        - 委派生成器在yield from表达式出暂停，调用方可以直接把数据发给自生成器
        - 子生成器在把产生的值发给调用方
        - 子生成器在最后，解释器会抛出StopIteration，并且把返回值附加到异常对象上

# 剩下的内容
- xml，json
- re，xpath
- 网络编程：socket，ftp，mail
- http协议，==> http web server小项目
- django，尽可能详细

---------
# 习题课
- 爬虫
# asyncio
- python3.4开始引入标准库中，内置异步io的支持
- asyncio本身是一个消息循环
- 步骤:
    - 创建消息循环
    - 把协程导入
    - 关闭
# async and await
- 为了更好的表示异步io
- python3.5引入
- 让协程代码更简洁
- 使用上，可以简单的进行替换
    - 用async替换@asyncio.coroutine
    - await 替换yield from
# aiottp
- asynico实现单线程的并发io，在客户端用处不大
- 在服务器端可以asyncio+coroutine配合，因为http是io啊哦做
- asynico实现了tcp，udp，ssl等协议
- aiohttp是给予asycio实现的http框架
- pip install aiohttp
# concurrent.futures
- python3新增的库
- 类似其他语言的线程池的概念
- 利用multiprocessing实现真正的并行计算
- 核心原理：concurrent.futures会以子进程的形式，平行的运行多个python解释器，从而令python程序可以利用多核CPU来提升执行速度。 由于子进程与主解释器相分离，所以他们的全局解释器锁也是相互独立的。每个子进程都能够完整的使用一个CPU内核。
- concurrent.futures.Executor
    - ThreadPoolExecutor
    - ProcessPoolExecutor
    - 执行的时候需要自行选择
- submit（fn， args， kwargs）
    - fn：异步执行的函数
    - args，kwargs参数
# current中的map函数
- map(fn, *iterables, timeout=None)
    - 跟map函数类似
    - 函数需要异步执行
    - timeout：超时时间
    - map跟submit使用一个就行
# Future
- 未来需要完成的任务
- future 实例由Excutor.submit创建