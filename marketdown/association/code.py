# # 可迭代
# l = [i for i in range(10)]
#
# # l是可迭代的，但是不是迭代器
# for idx in l:
#     print(idx)
#
# # range是个迭代器
# for i in range(5):
#     print(i)
#
#
# # isinstance案例
# # 判断某个变量是否是一个实例
#
# # 判断是否可迭代
# from collections.abc import Iterable
#
# ll = [1, 2, 3, 4, 5]
#
# print(isinstance(ll, Iterable))
#
# from collections.abc import Iterator
#
# print(isinstance(ll, Iterator))
#
#
# # iter函数
# s = 'i love zhang'
# from collections.abc import Iterator
# from collections.abc import Iterable
#
# print(isinstance(s, Iterator))
# print(isinstance(s, Iterable))
#
# s_iter = iter(s)
# print(isinstance(s_iter, Iterator))
# print(isinstance(s_iter, Iterable))
#
#
# # 直接使用生成器
# # 放在中括号中是列表生成器
# L = [x * x for x in range(5)]
# # 放在小括号中就是生成器
# g = (x * x for x in range(5))
# print(type(L))
# print(type(g))
#
#
# # 函数案例
# def odd():
#     print('Stop 1')
#     yield 1
#     print('Stop 2')
#     yield 2
#     print('Stop 3')
#     yield 3
#     return None
#
#
# # odd() 是调用生成器
# g = odd()
# one = next(g)
# print(one)
# two = next(g)
# print(two)
# for i in odd():
#     print(i)
#
#
# # for循环调用生成器 斐波那契数列
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n += 1
#     return 'Done'
#
#
# fib(5)
#
#
# #  斐波那契数列
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n += 1
#     # 需要注意，爆出异常时的返回值是return的返回值
#     return 'Done'
#
#
# g = fib(5)
# for i in range(6):
#     rst = next(g)
#     print(rst)
#
# ge = fib(10)
# '''
# 生成器的典型用法是在for中使用
# 比较常用的典型生成器就是range
# '''
# # 在for循环中使用生成器
# for i in ge:
#     print(i)
#
#
# # 协程代码案例1
# def simple_coroutine():
#     print('-> start')
#     x = yield
#     print('-> revived', x)
#
#
# # 主线程
# sc = simple_coroutine()
# print(111)
# # 可以使用sc.send(None),效果一样
# next(sc)  # 预激
#
# print(222)
# sc.send('zhexiao')
#
#
# # 协程的状态
# def simple_coroutine(a):
#     print('-> start')
#
#     b = yield a
#     print('-> recived', a, b)
#
#     c = yield a + b
#     print('-> recived', a, b, c)
#
#
# # runc
# sc = simple_coroutine(5)
#
# aa = next(sc)
# print(aa)
# bb = sc.send(6)  # 5,6
# print(bb)
# cc = sc.send(7)  # 5,6,7
# print(cc)
#
#
# # yield from
# def gen():
#     for c in 'AB':
#         yield c
#
#
# # list直接用生成器作为参数
# print(list(gen()))
#
#
# def gen_new():
#     yield from 'AB'
#
#
# print(list(gen_new()))
#
#
# # 委派生成器
# from collections import namedtuple
#
# '''
# 解释：
# 1. 外层 for 循环每次迭代会新建一个 grouper 实例，赋值给 coroutine 变量； grouper 是委派生成器。
# 2. 调用 next(coroutine)，预激委派生成器 grouper，此时进入 while True 循环，调用子生成器 averager 后，在 yield from 表达式处暂停。
# 3. 内层 for 循环调用 coroutine.send(value)，直接把值传给子生成器 averager。同时，当前的 grouper 实例（coroutine）在 yield from 表达式处暂停。
# 4. 内层循环结束后， grouper 实例依旧在 yield from 表达式处暂停，因此， grouper函数定义体中为 results[key] 赋值的语句还没有执行。
# 5. coroutine.send(None) 终止 averager 子生成器，子生成器抛出 StopIteration 异常并将返回的数据包含在异常对象的value中，yield from 可以直接抓取 StopItration 异常并将异常对象的 value 赋值给 results[key]
# '''
# ResClass = namedtuple('Res', 'count average')
#
#
# # 子生成器
# def averager():
#     total = 0.0
#     count = 0
#     average = None
#
#     while True:
#         term = yield
#         # None是哨兵值
#         if term is None:
#             break
#         total += term
#         count += 1
#         average = total / count
#
#     return ResClass(count, average)
#
#
# # 委派生成器
# def grouper(storages, key):
#     while True:
#         # 获取averager()返回的值
#         storages[key] = yield from averager()
#
#
# # 客户端代码
# def client():
#     process_data = {
#         'boys_2': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
#         'boys_1': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46]
#     }
#
#     storages = {}
#     for k, v in process_data.items():
#         # 获得协程
#         coroutine = grouper(storages, k)
#
#         # 预激协程
#         next(coroutine)
#
#         # 发送数据到协程
#         for dt in v:
#             coroutine.send(dt)
#
#         # 终止协程
#         coroutine.send(None)
#     print(storages)
#
# # run
# client()
#
#
# import threading
# # 引入异步io包
# import asyncio
#

# # 使用协程
# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     print('Start..... (%s)' % threading.currentThread())
#     yield from asyncio.sleep(10)
#     print('Done..... (%s)' % threading.currentThread())
#     print('Hello again! (%s)' % threading.currentThread())
#
#
# # 启动消息循环
# loop = asyncio.get_event_loop()
# # 定义任务
# tasks = [hello(), hello()]
# # asyncio使用wait等待task执行完毕
# loop.run_until_complete(asyncio.wait(tasks))
# # 关闭消息循环
# loop.close()
#
#
# import asyncio
#
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     # 异步请求网络地址
#     connect = asyncio.open_connection(host, 80)
#     # 注意yield from
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         # http协议的换行使用/r/n
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
#
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
#
#
# # 使用协程
# import threading
# # 引入异步io包
# import asyncio
#
#
# # @asyncio.coroutine
# async def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     print('Start..... (%s)' % threading.currentThread())
#     await asyncio.sleep(10)
#     print('Done..... (%s)' % threading.currentThread())
#     print('Hello again! (%s)' % threading.currentThread())
#
#
# # 启动消息循环
# loop = asyncio.get_event_loop()
# # 定义任务
# tasks = [hello(), hello()]
# # asyncio使用wait等待task执行完毕
# loop.run_until_complete(asyncio.wait(tasks))
# # 关闭消息循环
# loop.close()
#
#
# # aiohttp案例
# import asyncio
#
# from aiohttp import web
#
#
# async def index(request):
#     await asyncio.sleep(0.5)
#     return web.Response(body=b'<h1>Index</h1>')
#
#
# async def hello(request):
#     await asyncio.sleep(0.5)
#     text = '<h1>hello, %s!</h1>' % request.match_info['name']
#     return web.Response(body=text.encode('utf-8'))
#
#
# async def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     app.router.add_route('GET', '/hello/{name}', hello)
#     srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
#     print('Server started at http://127.0.0.1:8000...')
#     return srv
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()
#
#
# # 关于concurrent案例
# from concurrent.futures import ThreadPoolExecutor
# import time
#
#
# def return_future(msg):
#     time.sleep(3)
#     return msg
#
#
# # 创建一个线程池
# pool = ThreadPoolExecutor(max_workers=2)
#
# # 往线程池加入2个task
# f1 = pool.submit(return_future, 'hello')
# f2 = pool.submit(return_future, 'world')
#
# # 等待执行完毕
# print(f1.done())
# time.sleep(3)
# print(f2.done())
#
# # 结果
# print(f1.result())
# print(f2.result())
#
#
# # map函数
# import time, re
# import os, datetime
# from concurrent import futures
#
# data = ['1', '2']
#
#
# def wait_on(argument):
#     print(argument)
#     time.sleep(2)
#     return "ok"
#
#
# ex = futures.ThreadPoolExecutor(max_workers=2)
# for i in ex.map(wait_on, data):
#     print(i)
#
#
from concurrent.futures import ThreadPoolExecutor as Pool
from concurrent.futures import as_completed
import requests

URLS = ['http://qq.com', 'http://sina.com', 'http://www.baidu.com', ]


def task(url, timeout=10):
    return requests.get(url, timeout=timeout)


with Pool(max_workers=3) as executor:
    future_tasks = [executor.submit(task, url) for url in URLS]

    for f in future_tasks:
        if f.running():
            print('%s is running' % str(f))

    for f in as_completed(future_tasks):
        try:
            ret = f.done()
            if ret:
                f_ret = f.result()
                print('%s, done, result: %s, %s' % (str(f), f_ret.url, len(f_ret.content)))
        except Exception as e:
            f.cancel()
            print(str(e))
