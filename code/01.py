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
#
#
# # 继承中的构造函数 -3
# class Animal:
#     def __init__(self):
#         print('Animal')
#
#
# class PaXingAni(Animal):
#     pass
#
#
# class Dog(PaXingAni):
#     pass
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
# c = Cat()
#
#
#
#
# print(type(super))
# help(super)
#
#
#
#
# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(B, A):
#     pass
#
#
# print(A.__mro__)
# print(B.__mro__)
# print(C.__mro__)
#
#
#
#
# # 多继承例子
# # 子类可以直接拥有父类的属性和方法，私有属性和方法除外
# class Fish:
#     def __init__(self, name):
#         self.name = name
#
#     def swim(self):
#         print("I am swimming...")
#
#
# class Bird:
#     def __init__(self, name):
#         self.name = name
#
#     def fly(self):
#         print("I am flying...")
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def work(self):
#         print("Working...")
#
#
# class SuperMan(Person, Bird, Fish):
#     def __init__(self, name):
#         self.name = name
#
#
# s = SuperMan("yueyue")
# s.fly()
# s.swim()
#
#
# # 单继承例子
# class Student(Person):
#     def __init__(self, name):
#         self.name = name
#
#
# stu = Student("yueyue")
# stu.work()
#
#
#
#
# # 菱形问题
# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     pass
#
#
# class D(B, C):
#     pass
#
#
#
#
# # 构造函数例子
# class Person:
#     # 对Person类进行实例化的时候
#     # 姓名要确定
#     # 年龄要确定
#     # 地址肯定有
#     def __init__(self):
#         self.name = "NoName"
#         self.age = 18
#         self.address = "Studentwhoneheim"
#         print("In Init func")
#
#
# # 实例化一个人
# p = Person()
#
#
#
#
# # Mixin案例
# class Person:
#     name = "liuyong"
#     age = 18
#
#     def eat(self):
#         print("EAT...")
#
#     def drink(self):
#         print("DRINK...")
#
#     def sleep(self):
#         print("SLEEP...")
#
#
# class Teacher(Person):
#     def work(self):
#         print("Work")
#
#
# class Student(Person):
#     def study(self):
#         print("Study")
#
#
# class Tutor(Teacher, Student):
#     pass
#
#
# t = Tutor()
#
# print(Tutor.__mro__)
# print(t.__dict__)
# print(Tutor.__dict__)
#
# print("*" * 20)
#
#
# class TeacherMixin:
#     def work(self):
#         print("Work")
#
#
# class StudentMixin:
#     def study(self):
#         print("Study")
#
#
# class TutorMixin(Person, TeacherMixin, StudentMixin):
#     pass
#
#
# tt = TutorMixin
# print(TutorMixin.__mro__)
# print(tt.__dict__)
# print(TutorMixin.__dict__)
#
#
#
#
# # issubclass
# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# class C:
#     pass
#
#
# print(issubclass(B, A))
# print(issubclass(C, A))
# print(issubclass(B, object))
#
#
#
#
# # isinstance
# class A:
#     pass
#
#
# a = A()
#
# print(isinstance(a, A))
# print(isinstance(A(), A))
#
#
#
#
# # hasattr
# class A:
#     name = "NoName"
#
#
# a = A()
#
# print(hasattr(a, "name"))
# print(hasattr(a, "age"))
#
#
#
#
# # help案例
# # 我想知道setattr的具体用法
# help(setattr)
#
#
#
#
# # dir 案例
# class A:
#     pass
#
#
# # dir(A)
# a = A()
# print(dir(a))
#
#
#
#
# # 属性案例
# # 创建Student类，描述学生类
# # 学生具有Student.name属性
# # 但name格式并不统一
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#         # 如果不想修改代码
#         self.set_name(name)
#
#     # 介绍下自己
#     def intro(self):
#         print("Hai, my name is {0}".format(self.name))
#
#     def set_name(self, name):
#         self.name = name.upper()
#
#
# s1 = Student("LIU Ying", 19)
# s2 = Student("michi stangle", 24)
# s1.intro()
# s2.intro()
#
#
#
#
# # property案例
# # 定义一个Person类，具有name，age属性
# # 对于任意输入的姓名，我们都希望用大写方式保存
# # 年龄，我们希望内部统一用整数保存
# # x = property(fget, fset, fdel, doc)
# class Person:
#     """
#     只是一个人，一个高尚的人，
#     属相啊
#     """
#     # 函数的名称可以随意
#     def f_get(self):
#         return self._name * 2
#
#     def f_set(self, name):
#         # 所有输入的姓名以大写形式保存
#         self._name = name.upper()
#
#     def f_del(self):
#         self._name = "NoName"
#
#     name = property(f_get, f_set, f_del, "对name进行下造作")
#
#
# p = Person()
# p.name = "TuLing"
# print(p.name)
#
#
# # 类的内置函数举例
# print(Person.__dict__)
# print(Person.__doc__)
# print(Person.__name__)
# print(Person.__bases__)
#
#
#
#
# # init 举例
# class A:
#     def __init__(self, name = 0):
#         print('哈哈，调用了')
#
#
# a = A()
# print(type(a))
#
#
#
#
# # __call__举例
# class A:
#     def __init__(self, name = 0):
#         print('哈哈，调用了')
#
#     def __call__(self, *args, **kwargs):
#         print(args)
#         print(kwargs)
#
#
# a = A()
# a()
#
#
#
#
# # __call__举例
# class A:
#     def __init__(self, name = 0):
#         print('哈哈，调用了')
#
#     def __call__(self, *args, **kwargs):
#         print(args)
#         print(kwargs)
#
#     def __str__(self):
#         return '例子'
#
#
# a = A()
# print(a)
#
#
#
#
# # __getattr__
# class A:
#     name = "NoName"
#     age = 18
#
#     def __getattr__(self, item):
#         return "NO"
#
#
# a = A()
# print(a.name)
# print(a.address)
#
#
#
#
# # __setattr__ 案例
# class Person:
#     def __init__(self):
#         pass
#
#     def __setattr__(self, key, value):
#         print("设置属性：{0}".format(key))
#         # 下面语句会导致问题，死循环
#         # self.name = value
#         # 此种情况，为了避免死循环，规定统一嗲用父类魔法函数
#         super(Person, self).__setattr__(key, value)
#
#
# p = Person()
# print(p.__dict__)
# p.age = 18
# print(p.__dict__)
#
#
#
#
# # __gt__
# class Student:
#     def __init__(self, name):
#         self._name = name
#
#     def __gt__(self, other):
#         print("哈哈，{0} 会比 {1} 大吗".format(self, other))
#         return self._name > other._name
#
#     def __str__(self):
#         return self._name
#
#
# stu1 = Student('onw')
# stu2 = Student('two')
# print(stu1 > stu2)
#
#
#
#
# # 三种方法的案例
# class Person:
#     # 实例方法
#     def eat(self):
#         print(self)
#         print("Eating...")
#
#     # 类方法
#     # 类方法的第一个参数，一般命名为cls，区别于self
#     @classmethod
#     def play(cls):
#         print(cls)
#         print("Playing...")
#
#     # 静态方法
#     # 不需要用第一个参数表示自身或者类
#     @staticmethod
#     def say():
#         print("Saying...")
#
#
# yueyue = Person()
#
# # 实例方法
# yueyue.eat()
# # 类方法
# Person.play()
# yueyue.play()
# # 静态方法
# Person.say()
# yueyue.say()
#
#
#
#
# # 抽象
# class Animal:
#     def say_hello(self):
#         pass
#
#
# class Dog(Animal):
#
#     def say_hello(self):
#         print('问一下对方')
#
#
# class Person(Animal):
#
#     def say_hello(self):
#         print('Kiss me')
#
#
# d = Dog()
# d.say_hello()
#
# p = Person()
# p.say_hello()
#
#
#
#
# # 抽象类的实现
# import abc
#
#
# # 声明一个类并且制定当前类的元类
# class Human(metaclass=abc.ABCMeta):
#     # 定义一个抽象方法
#     @abc.abstractmethod
#     def smoking(self):
#         pass
#
#     # 定义类抽象方法
#     def drink(self):
#         pass
#
#     # 定义静态抽象方法
#     @staticmethod
#     def play():
#         pass
#
#     def sleep(self):
#         pass
#
#
#
# # 函数名可以当变量使用
# def say_hello(name):
#     print("{0}你好，来一发嘛？".format(name))
#
#
# say_hello("月月")
#
# liuming = say_hello
#
# liuming("yueyue")
#
#
# # 自己组装一个类
# class A:
#     pass
#
#
# def say(self):
#     print("Saying...")
#
#
# class B:
#     def say(self):
#         print("Saying...")
#
#
# say(9)
#
# A.say = say
#
# a = A()
# a.say()
#
# b = B()
# b.say()
#
#
#
#
# # 组装类例子 2
# # 自己组装一个类
# from types import MethodType
#
#
# class A:
#     pass
#
#
# def say(self):
#     print("Saying...")
#
#
# a = A()
# a.say = MethodType(say, A)
# a.say()
# help(MethodType)
#
#
#
#
# help(type)
#
#
# # 利用type造一个类
# # 先定义类应该具有的成员函数
# def say(self):
#     print("Saying...")
#
#
# def talk(self):
#     print("Talking...")
#
#
# # 用type创建一个类
# A = type("AName", (object,), {"class_say": say, "class_talk": talk})
# # 然后可以像正常访问一样使用类
# a = A()
# a.class_say()
# a.class_talk()
#
#


# 元类演示
# 元类写法是固定的，必须继承自type
# 元类一般命名为MetaClass结尾
class TuLingMetaClass(type):
    # 注意一下写法
    def __new__(cls, name, args, kwargs):
        # 自己的业务逻辑
        print("哈哈，我是元类呀")
        kwargs['id'] = "00000"
        kwargs['addr'] = "北京海底拿去"
        return type.__new__(cls, name, args, kwargs)


# 元类定义完就可以使用，使用注意写法
class Teacher(object, metaclass=TuLingMetaClass):
    pass


t = Teacher()
print(t.id)
