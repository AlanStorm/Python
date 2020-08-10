# print("*" * 5)

# 利用for循环
# for i in range(0, 4):
#     print("*" * 5)


# 利用双层for循环
# for i in range(0, 4):
#     # 利用for循环打印一行星号
#     for j in range(5):
#         # print默认自动换行
#         # 可以通过end参数控制
#         print("* ", end="")
#
#     print()


# 利用for循环
# for i in range(0, 4):
#     print("* " * 5)
#


# 简单图形打印
"""
打印一下图形在输出上面
* * * * *
*       *
*       *
* * * * *
"""
# 外层循环控制行
# for i in range(4):
#     if i == 0:
#         print("* " * 5)
#
#     if i == 3:
#         print("* " * 5)
#
#     if i == 1:
#         print("*       *")
#
#     if i == 2:
#         print("*       *")

# 更改上面写法
# 外层循环控制行
# for i in range(4):
#     if i == 0 or i == 3:
#         print("* " * 5)
#
#     if i == 1 or i == 2:
#         print("*       *")

# 更改上面写法
# 外层循环控制行
for i in range(4):
    if i == 0 or i == 3:
        print("* " * 5)

    if i == 1 or i == 2:
        for j in range(5):
            if j == 0 or j == 4:
                print("* ", end="")
            else:
                print('  ', end="")
        print()



