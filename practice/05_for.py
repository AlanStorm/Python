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
# # for循环
# for i in range(5):
#     # 打印一行
#     # 每一行打印机几个星号，跟行号相关
#     for j in range(i + 1):
#         if i == 1 or i == 4:
#             print("* ", end="")
#         else:
#             if j == 0 or j == i:
#                 print("* ", end="")
#             else:
#                 print("  ", end="")
#     print()

# 打印倒立三角
"""
* * * * *
* * * * 
* * * 
* * 
*   
"""
# # i-for控制行号
# # j-for控制列号
# for i in range(5):
#     for j in range(5 - i):
#         print("* ", end="")
#     print()

# 打印空三角
"""
* * * * *
*     * 
*   * 
* * 
*   
"""
# # i-for控制行号
# # j-for控制列号
# for i in range(5):
#     for j in range(5 - i):
#         if i == 0:
#             print("* ", end="")
#             continue
#         if j == 0 or j == 4 - i:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()
# 打印三角形，正三角形
"""
     *
    * *
   * * *
  * * * * *
 * * * * * * 
"""
# # i-for控制行
# # j-for控制列
# for i in range(6):
#     # 总体思路是，先但因一行空格，代表每一行星星的空格
#     # 再不换行，打印星号
#     for j in range(6 - i):
#         print(" ", end="")
#     for m in range(i + 1):
#         print("* ", end="")
#
#     # 打印一行后换行
#     print()

# 打印空三角
"""
     *
    * *
   *   *
  *      *
 * * * * * * 
"""
# for i in range(5):
#     for k in range(5 - i):
#         print(" ", end="")
#     for j in range(5 - i, 6):
#         if i == 4 or j == 5 - i or j == 5:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()
