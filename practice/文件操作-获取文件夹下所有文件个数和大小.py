# # 编写一个程序，统计当前目录下每个文件类型的文件数
# # 思路：
# # 打开当前的文件夹
# # 获取到当前文件夹下面所有的文件
# # 处理我们当期的文件夹下面可能有文件夹的情况
# # 做出统计
# import os
#
# # 得到当前文件夹下面所有的文件
# all_files = os.listdir(os.curdir)  # os.curdir 表示当前目录 curdir：currentdirectory
#
# type_dict = dict()
#
# for each_file in all_files:
#     # 如果说我们的each_file是文件夹
#     if os.path.isdir(each_file):
#         type_dict.setdefault("文件夹", 0)
#         type_dict['文件夹'] += 1
#     else:
#         # 如果不是文件夹，而是文件，统计我们的文件
#         ext = os.path.splitext(each_file)[1]  # 获取到文件的后缀
#         type_dict.setdefault(ext, 0)
#         type_dict[ext] += 1
#
# for each_type in type_dict:
#     print('该文件夹下面有类型为{}的文件有{}个'.format(each_type, type_dict[each_type]))
#
#
# 编写一个程序，计算当前文件夹下面所有文件的大小
# 思路
# 打开当前的文件夹
# 获取到所有的文件和文件大小
# 保存我们获取到的数据，然后淡印出来
import os

all_files = os.listdir(os.curdir)

file_dict = dict()

for each_file in all_files:
    # 判断each_file是否是文件
    if os.path.isfile(each_file):
        file_size = os.path.getsize(each_file)
        file_dict[each_file] = file_size

for each in file_dict.items():
    print('{}大小{}'.format(each[0], each[1]))
