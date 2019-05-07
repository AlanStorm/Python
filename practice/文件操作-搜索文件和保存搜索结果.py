# # 编写一个程序，用户输入文件名以及开始所搜的路径，搜索该文件是否存在，如果遇到文件夹，则进入该文件夹继续搜索
# # 思路
# # input 去接受用户输入的文件名和开始搜索的路径
# # os.path,isdir 去判断是不是文件夹，如果是的话，就需要进入该文件夹继续搜索，循环调用一下我们的函数来实现
# import os
#
# start_dir = input('请输入目录：')
# target = input('请输入文件名：')
#
#
# def search_file(start_dir, target):
#     os.chdir(start_dir)  # 切换到用户输入的路径
#
#     for each_file in os.listdir(os.curdir):
#         if each_file == target:
#             print(os.getcwd() + os.sep + each_file)
#         if os.path.isdir(each_file):
#             search_file(each_file, target)  # 递归调用
#             os.chdir(os.pardir)
#
#
# search_file(start_dir, target)
#
#
# # 对上述题目加一些需求，模糊匹配，判断我们的target是否包含在某一个文件中
# # in 去判断target这个字符串是否在文件的名字中
# import os
#
# start_dir = input('请输入目录：')
# target = input('请输入文件名：')
#
#
# def search_file(start_dir, target):
#     os.chdir(start_dir)  # 切换到用户输入的路径
#
#     for each_file in os.listdir(os.curdir):
#         if target in each_file:
#             print(os.getcwd() + os.sep + each_file)
#         if os.path.isdir(each_file):
#             search_file(each_file, target)  # 递归调用
#             os.chdir(os.pardir)
#
#
# search_file(start_dir, target)
#
#
# 再加一个需求，上述题目，我们需要保存我们的文件存在的地方，到我们指定的路径
# file I/O 写文件
import os

start_dir = input('请输入目录：')
target = input('请输入文件名：')
backup = []


def search_file(start_dir, target):
    os.chdir(start_dir)  # 切换到用户输入的路径

    for each_file in os.listdir(os.curdir):
        if target in each_file:
            backup_file = os.getcwd() + os.sep + each_file
            backup.append(backup_file)
        if os.path.isdir(each_file):
            search_file(each_file, target)  # 递归调用
            os.chdir(os.pardir)

    return backup


rt = search_file(start_dir, target)

f = open(os.getcwd() + os.sep + "backup.txt", 'wb')
f.write("\n".join(rt).encode('utf-8'))
f.close()
