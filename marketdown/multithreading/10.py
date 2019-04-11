import threading
from time import sleep, ctime

loop = [4, 2]


class ThreadFunc:

    def __init__(self, name):
        self.name = name

    def loop(self, nsec):
        print(self.name)
        print('Start loop ', self.name, 'at ', ctime())
        sleep(nsec)
        print('Done loop ', self.name, ' at ', ctime())


def main():
    print("Starting at: ", ctime())

    # ThreadFunc("loop").loop 跟一下两个式子相等：
    # t = ThreadFunc("loop")
    # t.loop
    # 以下t1 和  t2的定义方式相等
    t = ThreadFunc("loop1")
    t1 = threading.Thread(target=t.loop, args=(4,))
    # 下面这种写法更西方人，工业化一点
    t2 = threading.Thread(target=ThreadFunc('loop2').loop, args=(2,))

    # 常见错误写法
    # t1 = threading.Thread(target=ThreadFunc('loop').loop(100,4))
    # t2 = threading.Thread(target=ThreadFunc('loop').loop(100,2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("ALL done at: ", ctime())


if __name__ == '__main__':
    main()
