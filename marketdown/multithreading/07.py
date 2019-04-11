import time
import threading


def fun():
    print('Start fun')
    time.sleep(2)
    print('End fun')


print('Main thred')

t1 = threading.Thread(target=fun, args=())
# 设置守护线程的方法，必须在start之前设置，否则无效
t1.setDaemon(True)
t1.start()

time.sleep(1)
print('Main thread end')