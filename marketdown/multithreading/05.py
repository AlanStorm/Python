'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
联系带参数的多线程启动方法
'''
import time
import threading


def loopl(in1):
    # ctime 得到当前时间
    print('Start loop 1 at:', time.ctime())
    # 把参数打印出来
    print('我是参数', in1)
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop 1 at:', time.ctime())


def loop2(in1, in2):
    # ctime 得到当前时间
    print('Start loop 2 at :', time.ctime())
    # 把参数in 和 in2打印出来，代表使用
    print("我是参数 ", in1, "和参数  ", in2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop 2 at:', time.ctime())


def main():
    print('Starting at:', time.ctime())
    # 启动多线程的意思是用多线程去执行某个桉树
    # 启动多线程函数为Start_new_thread
    # 参数连个，一个是需要运行的函数名，第二个参数作为元祖使用，为空则使用空元祖
    # 注意，如果连个函数只有一个参数，需要参数后有一个逗号
    t1 = threading.Thread(target=loopl, args=('王阿四',))
    t1.start()

    t2 = threading.Thread(target=loop2, args=('爱九点半', '阿斯达'))
    t2.start()

    t1.join()
    t2.join()

    print('All done at:', time.ctime())
    exit()


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
