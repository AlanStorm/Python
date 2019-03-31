# # "小"函数举例
# def printA():
#     print("AAAAA")
#
#
# printA()
#
#
# lambda表达式的用法
# 1，以lambda开头
# 2，紧跟一定的参数（如果有的话）
# 3.参数后用冒号和表达式主体隔开
# 4.只是一个表达式，所以，没有return

# 计算一个数字的100倍数
# 因为就是一个表达式，所以没有return
# stm = lambda x: 100 * x
# # 使用上跟函数调用一模一样
# stm(89)
#
# stm2 = lambda x, y, z: x + y * 10 + z * 100
# stm2(1, 2, 3)
#
# # 变量可以赋值
# a = 100
# b = a
#
#
# # 函数名称就是一个变量
# def funA():
#     print('funcA')
#
#
# funcb = funA
# funcb()

# 高阶函数举例
# funA还普通函数，返回一个传入数字的100倍数字
#
#
# def funA(n):
#     return n * 100
#
#
# # 在写一个函数，把传入参数乘以200倍，利用高阶函数
# def funB(n):
#     # 最终是想返回300n
#     return funA(n) * 3
#
#
# funB(9)
#
#
# # 写一个高阶函数
# def funC(n, f):
#     # 假定函数式n扩大100倍
#     return f(n) * 3
#
#
# #
# # funC(9, funA)
# # 比较funC和funB，显然funC的写法优于funC
# # 例如
# def funD(n):
#     return n * 10
#
#
# # 需求变更，需要把n放大三十倍，此时funB则无法实现
# print(funC(7, funD))
