# # 编写一个程序，当用户输入文件名和行数的时候，将该文件的前N行内容答应到屏幕上
# file_name = input('请输入你要打开的文件名：')
# line_number = input('请输入你要显示的前几行：')  # 是一个str
#
#
# def file_view(file_name, line_number):
#     print('\n文件%s的前%s行内容如下' % (file_name, line_number))
#
#     # 去打开file_name的文件
#     f = open(file_name)
#     for i in range(int(line_number)):
#         print(f.readline())
#     f.close()
#
#
# file_view(file_name, line_number)
#
#
# # 我们在上一道题的基础上，增加一点功能，使用户可以随意的输入显示的行数
# # 12:48 : :9
# # 用以上的形式表示我们想要打印的其实和结束的行数
# file_name = input('请输入你要打开的文件名：')
# line_number = input('请输入你要显示的行数，格式为1:9或者:')  # 是一个str
#
#
# def print_line(file_name, line_number):
#     f = open(file_name)
#
#     begin, end = line_number.split(":")
#     if begin == "":
#         begin = "1"
#     if end == "":
#         end = "-1"
#     begin = int(begin) - 1
#     end = int(end)
#
#     lines = end - begin
#     print(lines)
#     # 消耗掉begin之前的行数
#     for i in range(begin):
#         f.readline()
#     if lines < 0:
#         print(f.read())
#     else:
#         for j in range(lines):
#             print(f.readline())
#
#     f.close()
#
#
# print_line(file_name, line_number)
#
#
# 编写一个程序，实现“全部替换”的功能
# 打开一个文件
# 把文件中xxx这样额字符串，替换成sss
# open 打开文件
# readline() 读取文件北荣
# replace 替换
file_name = input('请输入你要打开的文件名：')
rep_world = input('请输入你要替换的字符：')
new_world = input('请输入替换的新的字符串：')


def file_replace(file_name, rep_world, new_world):
    f = open(file_name)
    content = []
    for each_line in f:
        if rep_world in each_line:
            each_line = each_line.replace(rep_world, new_world)
        content.append(each_line)

    decide = input('你确定要这样子做吗？请输入YES/NO')
    if decide in ["YES", "Yes", 'yes']:
        f_write = open(file_name, 'w')
        f_write.write("".join(content))
        f_write.close()


file_replace(file_name, rep_world, new_world)
