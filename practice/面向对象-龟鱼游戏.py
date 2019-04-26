# class Ticket():
#     def __init__(self, weekend=False, child=False):
#         self.exp = 100
#         if weekend:
#             self.inc = 1.2
#         else:
#             self.inc = 1
#
#         if child:
#             self.discount = 0.5
#         else:
#             self.discount = 1
#
#     def cal_price(self, num):
#         return self.exp * self.inc * self.discount * num
#
#
# adult = Ticket()
# child = Ticket()
# print('两个成年人和一个小孩平日的价格是{}'.format(adult.cal_price(2) + child.cal_price(1)))
# import random as r
#
#
# class Turtle(object):
#     def __init__(self):
#         self.power = 100
#
#         # 初始化乌龟的位置
#         self.x = r.randint(0, 10)
#         self.y = r.randint(0, 10)
#
#     def move(self):
#         new_x = r.choice([1, 2, -1, -2]) + self.x
#         new_y = r.choice([1, 2, -1, -2]) + self.y
#
#         # 判断乌龟的移动是否超出了边界
#         if new_x < 0:
#             self.x = 0 - (new_x - 0)
#         elif new_x > 10:
#             self.x = 10 - (new_x - 10)
#         else:
#             self.x = new_x
#
#         if new_y < 0:
#             self.y = 0 - (new_y - 0)
#         elif new_y > 10:
#             self.y = 10 - (new_y - 10)
#         else:
#             self.y = new_y
#
#         self.power -= 1
#         return self.x, self.y
#
#     def eat(self):
#         self.power += 20
#         if self.power >= 100:
#             self.power = 100
#
#
# class Fish(object):
#     def __init__(self):
#         self.x = r.randint(0, 10)
#         self.y = r.randint(0, 10)
#
#     def move(self):
#         new_x = self.x + r.choice([1, -1])
#         new_y = self.y + r.choice([1, -1])
#         # 判断鱼的移动是否超出了边界
#         if new_x < 0:
#             self.x = 0 - (new_x - 0)
#         elif new_x > 10:
#             self.x = 10 - (new_x - 10)
#         else:
#             self.x = new_x
#
#         if new_y < 0:
#             self.y = 0 - (new_y - 0)
#         elif new_y > 10:
#             self.y = 10 - (new_y - 10)
#         else:
#             self.y = new_y
#
#         return self.x, self.y
#
#
# turtle = Turtle()
# fish = []
# for i in range(10):
#     new_fish = Fish()
#     fish.append(new_fish)
#
# while True:
#     if not len(fish):
#         print("鱼被吃光了，游戏结束")
#         break
#     if not turtle.power:
#         print('乌龟体力被耗尽了，游戏结束')
#         break
#     pos = turtle.move()
#
#     # 在迭代器中做列表的删除元素是非常危险的，经常会出现一些意向不到的问题，因为迭代器是直接
#     # 引用列表元素的数据做的操作，所以 我们智力吧列表拷贝一份传递给迭代器，然后再对原列表做操作
#     for each_fish in fish[:]:
#         if each_fish.move() == pos:
#             turtle.eat()
#             fish.remove(each_fish)
#             print('有一条鱼被吃掉了')
import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Line(object):
    def __init__(self, p1, p2):
        self.x = p1.get_x() - p2.get_x()
        self.y = p1.get_y() - p2.get_y()

        self.len = math.sqrt(self.x * self.x + self.y * self.y)

    def get_len(self):
        return self.len


p1 = Point(2, 3)
p2 = Point(5, 7)
line = Line(p1, p2)
print(line.get_len())
