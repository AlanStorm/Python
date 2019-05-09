# # 用协程的方式完成播放
# import time
# import asyncio
#
# movie_list = ['斗破.mp4', '复仇者联盟.avi', '钢铁雨.rmvb', 'xxx.mp4']
# music_list = ['周杰伦.mp3', '五月天.mp3']
# movie_format = ['mp4', 'avi']
# music_format = ['mp3']
#
#
# # @asyncio.coroutine
# # def play(playlist):
# #     for i in playlist:
# #         if i.split('.')[1] in movie_format:
# #             print('你现在收看的是{}'.format(i))
# #             yield time.sleep(3)
# #         elif i.split('.')[1] in music_format:
# #             print('你现在收听的是{}'.format(i))
# #             yield time.sleep(2)
# #         else:
# #             print('没有能播放的格式')
#
#
# async def play(playlist):
#     for i in playlist:
#         if i.split('.')[1] in movie_format:
#             print('你现在收看的是{}'.format(i))
#             await asyncio.sleep(3)
#         elif i.split('.')[1] in music_format:
#             print('你现在收听的是{}'.format(i))
#             await asyncio.sleep(2)
#         else:
#             print('没有能播放的格式')
#
# loop = asyncio.get_event_loop()
# task = [play(movie_list), play(music_list)]
# loop.run_until_complete(asyncio.wait(task))
# loop.close()
#
#
# 使用协程的概念，输入a,b,c,d四个证书，打印出(a+b)*(c+d)的值，假设a+b 和 c+d是一个耗时1s的IO操作

import asyncio
import threading


async def sum(a, b):
    print('现在开始准备计算,current thread is {}'.format(threading.currentThread()))
    r = int(a) + int(b)
    await asyncio.sleep(1)
    print('现在计算完了，current thread is {}'.format(threading.currentThread()))
    return r


loop = asyncio.get_event_loop()
task = asyncio.gather(sum(1, 2), sum(3, 4))
loop.run_until_complete(task)
r1, r2 = task.result()
print(int(r1) * int(r2))
loop.close()
