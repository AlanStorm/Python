# import p01
#
# stu = p01.Student("Xiao jing", 19)
# stu.say()
#
# p01.say_hello()

# 借助于importlib包也可以实现导入已数字开头的模块名称
import importlib

tuling = importlib.import_module("01")

tuling.say_hello()
