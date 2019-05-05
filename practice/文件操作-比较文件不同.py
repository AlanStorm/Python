# # 编写一个程序，接受用户输入的内容，并且保存为新的文件
# # 如果用户单独输入:w
# # 表示文件保存退出
#
# file_name = input('请用户输入文件名：')
#
#
# def file_write(file_name):
#     f = open(file_name, 'w')  # 打开我们用户的文件
#
#     print('请输入内容，（单独输入:w 保存瑞出）')
#
#     while True:
#         write_something = input()
#         # 判断用户输入的是不是 :w
#         if write_something != ":w":
#             # 向文件中写入用户输入的内容
#             f.write("%s\n" % write_something)
#         else:
#             # 用户输入的是 :w
#             break
#     f.close()
#
#
# file_write(file_name)
#
#
# 编写一个程序，比较用户输入的文件是否相同，如果不同，显示出所有不同处的行号
file1 = input('请输入需要比较的第一个文件名：')
file2 = input('请输入需要比较的第二个文件名：')


def file_compare(file1, file2):
    f1 = open(file1)
    f2 = open(file2)

    count = 0  # 统计的行数
    differ = []  # 统计不一样的数量

    for line1 in f1:
        line2 = f2.readline()

        count += 1
        if line1 != line2:  # 文件不同
            differ.append(count)
    f1.close()
    f2.close()

    return differ


differ = file_compare(file1, file2)
if len(differ) == 0:
    print('两个文件完全相同')
else:
    print('两个文件有%d不同' % len(differ))
    for each in differ:
        print('第%d行不一样' % each)

