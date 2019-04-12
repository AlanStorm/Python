# # 可迭代
# l = [i for i in range(10)]
#
# # l是可迭代的，但是不是迭代器
# for idx in l:
#     print(idx)
#
# # range是个迭代器
# for i in range(5):
#     print(i)
#
#
# # isinstance案例
# # 判断某个变量是否是一个实例
#
# # 判断是否可迭代
# from collections.abc import Iterable
#
# ll = [1, 2, 3, 4, 5]
#
# print(isinstance(ll, Iterable))
#
# from collections.abc import Iterator
#
# print(isinstance(ll, Iterator))
#
#
# # iter函数
# s = 'i love zhang'
# from collections.abc import Iterator
# from collections.abc import Iterable
#
# print(isinstance(s, Iterator))
# print(isinstance(s, Iterable))
#
# s_iter = iter(s)
# print(isinstance(s_iter, Iterator))
# print(isinstance(s_iter, Iterable))
#
#
# # 直接使用生成器
# # 放在中括号中是列表生成器
# L = [x * x for x in range(5)]
# # 放在小括号中就是生成器
# g = (x * x for x in range(5))
# print(type(L))
# print(type(g))
#
#
# # 函数案例
# def odd():
#     print('Stop 1')
#     yield 1
#     print('Stop 2')
#     yield 2
#     print('Stop 3')
#     yield 3
#     return None
#
#
# # odd() 是调用生成器
# g = odd()
# one = next(g)
# print(one)
# two = next(g)
# print(two)
# for i in odd():
#     print(i)
#
#
# # for循环调用生成器 斐波那契数列
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n += 1
#     return 'Done'
#
#
# fib(5)
#
#
# #  斐波那契数列
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n += 1
#     # 需要注意，爆出异常时的返回值是return的返回值
#     return 'Done'
#
#
# g = fib(5)
# for i in range(6):
#     rst = next(g)
#     print(rst)
#
# ge = fib(10)
# '''
# 生成器的典型用法是在for中使用
# 比较常用的典型生成器就是range
# '''
# # 在for循环中使用生成器
# for i in ge:
#     print(i)
#
#
