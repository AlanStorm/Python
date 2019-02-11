# 逐次按行打印
# for i in range(5):
#     # 打印一行
#     # 每一行打印几个星号，跟行号相关
#     for j in range(i + 1):
#         print("* ", end="")
#     print()

"""
打印空心三角形
*
* *
*   *
*     *
* * * * *
"""
# for循环
for i in range(5):
    # 打印一行
    # 每一行打印机几个星号，跟行号相关
    for j in range(i + 1):
        if i == 1 or i == 4:
            print("* ", end="")
        else:
            if j == 0 or j == i:
                print("* ", end="")
            else:
                print("  ", end="")
    print()
