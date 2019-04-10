# 环境
- xubuntu 16.04
- anaconda
- pycharm
- python3.6
- https://www.cnblogs.com/jokerbj/p/7460260.html
- http://www.dabeaz.com/python/UnderstandingGIL.pdf

# 多线程 vs 多进程
- 程序：一对代码已文本形式存入一个文档
- 进程：程序运行的一个状态
    - 包含地址控件、内存、数据栈等
    - 每个进程有自己完全独立的运行环境，多进程共享数据是一个问题
- 线程
    - 一个进程的独立运行片段，一个进程可以有多个线程
    - 轻量化的进程
    - 一个进程的过个线程间共享数据和上下文运行环境
    - 共享互斥问题
    - 全局解释器锁（GIL）
        - Python代码的执行是由Python虚拟机进行控制
        - 在主循环中只能有一个控制线程在执行