# '''
# 定义一个学生类
# '''
#
#
# # 定义一个空的类
# class Student():
#     # 一个空类 pass代表直接跳过
#     # 此处pass必须有
#     pass
#
#
# # 定义一个对象
# mingyue = Student()
#
#
# # 再定义一个类，用来描述听Python的学生
# class PythonStudent():
#     # 用None给不确定的值赋值
#     name = None
#     age = 19
#     course = "Python"
#
#     def doHomework(self):
#         print("I 做作业")
#
#         # 推荐在函数末尾使用return语句
#         return None
#
#
# # 实例化
# yueyue = PythonStudent()
# print(yueyue.name)
# print(yueyue.age)
# # 注意成员函数的调用没有出传入参数
# yueyue.doHomework()
#
#
#
#
#
#
# class A():
#     name = "dana"
#     age = 8
#
#     # 注意say的写法，参数有一个self
#     def say(self):
#         self.name = 'aaa'
#         self.age = 200
#
# # 此案例说明
# # 类实例的属性和器对象的实例的属性在不对对象的实例属性赋值的前提下，
# # 指向同一个变量
#
# # 此时，A称为类实例
# print(A.name)
# print(A.age)
#
# print("*"*20)
#
# # id可以鉴别一个变量是否和另一个变量是同一个变量
# print(id(A.name))
# print(id(A.age))
#
# print("*"*20)
# a = A()
# print(a.name)
# print(a.age)
# print(id(a.name))
# print(id(a.age))
#
# # 查看A内的所有属性
# print(A.__dict__)
# print(a.__dict__)
# a.name = 'yaona'
# a.age = 16
# print(a.__dict__)
# print(a.name)
# print(a.age)
# print(id(a.name))
# print(id(a.age))
#
#
# class Student:
#     name = 'dana'
#     age = 18
#
#     def say(self):
#         self.name = 'aaa'
#         self.age = 200
#         print("My name is {0}".format(self.name))
#         print("My age is {0}".format(self.age))
#
#     def sayAgain(s):
#         print("My name is {0}".format(s.name))
#         print("My age is {0}".format(s.age))
#
#
# yueyue = Student()
# yueyue.say()
#
#
#
#
#
# class Teacher:
#     name = 'dana'
#     age = 19
#
#     def say(self):
#         self.name = 'aaa'
#         self.age = 200
#         print("My name is {0}".format(self.name))
#         # 调用类的成员变量需要用 __class__
#         print("My age is {0}".format(__class__.age))
#
#     def sayAgain():
#         print(__class__.name)
#         print(__class__.age)
#         print("Hello,nice to see you again")
#
#
# t = Teacher()
# t.say()
# # 调用绑定类含税使用类名
# Teacher.sayAgain()
#
#
#
#
# 关于self案例
#
#
# class A:
#     name = 'liuying'
#     age = 18
#
#     def __int__(self):
#         self.name = 'aaa'
#         self.age = 200
#
#     def say(self):
#         print(self.name)
#         print(self.age)
#
#
# class B:
#     name = "bbbb"
#     age = 90
#
#
# a = A()
# # 此时，系统会默认把a作为第一个参数传入函数
# a.say()
#
# # 此时，self被a替换
# A.say(a)
# # 同样可以把A对位参数传入
# A.say(A())
# # 此时，传入的是类实例B，因为B具有name和age属性，所以不会报错
# A.say(B())
# # 以上代码，利用了鸭子模型
#
#
#
#
#
#
# class Person:
#     # name是共有的成员
#     name = "liuying"
#     # __age是私有成员
#     __age = 18
#
#
# p = Person
# # name是共有变量
# print(p.name)
# # __age是私有变量
# # print(p.__age)
#
#
#
#
#
#
# # name mangling技术
# class Person:
#     # name是共有的成员
#     name = "liuying"
#     # __age是私有成员
#     __age = 18
#
#
# p = Person
# print(p._Person__age)
# print(Person.__dict__)
#
#
#
#
# # 继承的语法
# # 在Python中，任何类都有一个共同的父类叫Object
# class Person:
#     name = "NoName"
#     age = 0
#     __score = 0  # 考试成绩是秘密，只要自己知道
#     _petname = "sec"   # 小名，是受保护的，子类可以使用，但不能公用
#
#     def sleep(self):
#         print("Sleeping...")
#
#
# # 父类写在括号内
# class Teacher(Person):
#     teacher_id = "9527"
#
#     def make_pass(self):
#         print("attention")
#
#
# t = Teacher()
# print(t.name)
# # 受保护不能外部访问，
# print(t._petname)
#
# # 私有访问问题
# # 公考访问私有变量，报错
# # print(t.__score)
# print(Teacher.name)
#
# t.sleep()
# print(t.teacher_id)
#
#
#

#
# # 子类和父类定义同一个名称变量，则优先使用子类本身
# class Person:
#     name = "NoName"
#     age = 0
#     __score = 0  # 考试成绩是秘密，只要自己知道
#     _pet_name = "sec"   # 小名，是受保护的，子类可以使用，但不能公用
#
#     def sleep(self):
#         print("Sleeping...")
#
#     def work(self):
#         print("make some money")
#
# # 父类写在括号内
# class Teacher(Person):
#     name = "DaNa"
#     teacher_id = "9527"
#
#     def make_pass(self):
#         print("attention")
#
#
# t = Teacher()
# print(t.name)
#
#
#
#
# # 子类扩充父类功能
# # 人有工作的函数，老师也有工作的函数，但老师的工作需要讲课
# class Person:
#     name = "NoName"
#     age = 0
#     __score = 0  # 考试成绩是秘密，只要自己知道
#     _pet_name = "sec"  # 小名，是受保护的，子类可以使用，但不能公用
#
#     def sleep(self):
#         print("Sleeping...")
#
#     def work(self):
#         print("make some money")
#
#
# # 父类写在括号内
# class Teacher(Person):
#     name = "DaNa"
#     teacher_id = "9527"
#
#     def make_test(self):
#         print("attention")
#
#     def work(self):
#         # 扩充父类的功能只需要调用父类相应的函数
#         # Person.work(self)
#         # 扩充父类的另一种方法
#         # super 代表得到父类
#         super().work()
#         self.make_test()
#
#
# t = Teacher()
# t.work()
#
#
#
#
# # 构造函数的概念
# class Dog:
#     # __init__就是构造函数
#     # 每次实例化的时候，第一个被调用
#     # 因为主要工作是进行初始化，所以得名
#     def __init__(self):
#         print("I am init in dog")
#
# 实例化的时候，括号内的参数需要跟构造函数参数匹配
# kaka = Dog()
#
#
#
#
# # 继承中的构造函数 -1
# class Animal:
#     pass
#
#
# class PaXingAni(Animal):
#     pass
#
#
# class Dog(PaXingAni):
#     # __init__就是构造函数
#     # 每次实例化的时候，第一个被调用
#     # 因为主要工作是进行初始化，所以得名
#     def __init__(self):
#         print("I am init in dog")
#
# # 实例化的时候，自动调用了Dog的构造函数
# kaka = Dog()
#
#
#
#
# # 继承中的构造函数 -2
# class Animal:
#     def __init__(self):
#         print('Animal')
#
#
# class PaXingAni(Animal):
#     def __init__(self):
#         print('PaXing DongWu')
#
#
# class Dog(PaXingAni):
#     # __init__就是构造函数
#     # 每次实例化的时候，第一个被调用
#     # 因为主要工作是进行初始化，所以得名
#     def __init__(self):
#         print("I am init in dog")
#
#
# # 实例化的时候，自动调用了Dog的构造函数
# # 因为找到了构造函数，则不在查找服了的构造函数
# kaka = Dog()
#
#
# class Cat(PaXingAni):
#     pass
#
#
# # 此时应该自动调用构造函数，因为Cat没有构造函数，所以查找父类构造函数
# # 在PaXingAni中查找到了构造函数，则停止向上查找
# c = Cat()
#
#
#
#
# # 继承中的构造函数 -3
# class Animal:
#     def __init__(self):
#         print('Animal')
#
#
# class PaXingAni(Animal):
#     def __init__(self, name):
#         print('PaXing DongWu {0}'.format(name))
#
#
# class Dog(PaXingAni):
#     # __init__就是构造函数
#     # 每次实例化的时候，第一个被调用
#     # 因为主要工作是进行初始化，所以得名
#     def __init__(self):
#         print("I am init in dog")
#
#
# # 实例化Dog时，查找Dog的构造函数，参数匹配，不报错
# d = Dog()
#
#
# class Cat(PaXingAni):
#     pass
#
#
# # 此时，由于Cat没有构造函数，则向上查找
# # 因为PaXingAni的构造函数需要两个参数，实例化的时候给了一个，报错
# c = Cat("Cat")
#
#


# 继承中的构造函数 -3
class Animal:
    def __init__(self):
        print('Animal')


class PaXingAni(Animal):
    pass


class Dog(PaXingAni):
    pass


# 实例化Dog时，查找Dog的构造函数，参数匹配，不报错
d = Dog()


class Cat(PaXingAni):
    pass


# 此时，由于Cat没有构造函数，则向上查找
# 因为PaXingAni的构造函数需要两个参数，实例化的时候给了一个，报错
c = Cat()
