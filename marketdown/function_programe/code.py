# # map举例
# # 有一个列表，想对列表李的每一个元素乘以10，并得到新的礼列表
# l1 = [i for i in range(10)]
#
#
# # print(l1)
# # l2 = []
# # for i in l1:
# #     l2.append(i * 10)
#
#
# # print(l2)
#
#
# # 利用map实现
# def mulTen(n):
#     return n * 10
#
#
# l3 = map(mulTen, l1)
# # map类型是一个可迭代的结构，所以可以使用for遍历
# for i in l3:
#     print(i)
# # 以下列表生成式得到的结果为空，why？
# l4 = [i for i in l3]
# print(l4)
#
#
from functools import reduce


# 定义一个操作函数
# 加入操作函数只是想家
def myAdd(x, y):
    return x + y


# 对于列表[1,2,3,4,5,6]执行myAdd的reduce操作
rst = reduce(myAdd, [1, 2, 3, 4, 5, 6])
print(rst)
