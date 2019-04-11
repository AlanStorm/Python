import time
import threading


def loop1():
    # ctime 得到当前时间
    print('Start loop 1 at :', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(6)
    print('End loop 1 at:', time.ctime())


def loop2():
    # ctime 得到当前时间
    print('Start loop 2 at :', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(1)
    print('End loop 2 at:', time.ctime())


def loop3():
    # ctime 得到当前时间
    print('Start loop 3 at :', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(5)
    print('End loop 3 at:', time.ctime())


def main():
    print('Starting at:', time.ctime())
    # 生成threading.Thread实例
    t1 = threading.Thread(target=loop1, args=())
    # setName是给每一个子线程设置一个名字
    t1.setName('THR_1')
    t1.start()

    t2 = threading.Thread(target=loop2, args=())
    t2.setName('THR_2')
    t2.start()

    t3 = threading.Thread(target=loop3, args=())
    t3.setName('THR_3')
    t3.start()

    # 预期3秒后，thread2已经自动结束
    time.sleep(3)
    # enumerate 得到正在运行子程序，即线程1和线程3
    for thr in threading.enumerate():
        # getName能够得到线程的名字
        print('正在运行的线程名字是：{0}', format(thr.getName()))
    print('正在运行的子程序数量为：{0}', format(threading.activeCount()))

    print("All done at:", time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
