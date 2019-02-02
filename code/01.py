'''
定义一个学生类
'''


# 定义一个空的类
class Student():
    # 一个空类 pass代表直接跳过
    # 此处pass必须有
    pass


# 定义一个对象
mingyue = Student()


# 再定义一个类，用来描述听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 19
    course = "Python"

    def doHomework(self):
        print("I 做作业")

        # 推荐在函数末尾使用return语句
        return None


# 实例化
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有出传入参数
yueyue.doHomework()
