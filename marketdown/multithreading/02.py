'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''
import time
import _thread


def loopl():
    # ctime 得到当前时间
    print('Start loop 1 at:', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop 1 at:', time.ctime())


def loop2():
    # ctime 得到当前时间
    print('Start loop 2 at:', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop 2 at:', time.ctime())


def main():
    print('Starting at:', time.ctime())
    # 启动多线程的意思是用多线程去执行某个桉树
    # 启动多线程函数为Start_new_thread
    # 参数连个，一个是需要运行的函数名，第二个参数作为元祖使用，为空则使用空元祖
    # 注意，如果连个函数只有一个参数，需要参数后有一个逗号
    _thread.start_new_thread(loopl, ())

    _thread.start_new_thread(loop2, ())

    print('All done at:', time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
