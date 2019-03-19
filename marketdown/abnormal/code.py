# 简单异常案例
# try:
#     num = int(input("Plz input your number:"))
#     print(123)
#     rst = 100 / num
#     print("计算结果是：{0}".format(rst))
# except:
#     print('出错了')
#     # exit是退出程序的意思
#     exit()
#
# # 简单异常案例
# # 给出提示信息
# try:
#     num = int(input("Plz input your number:"))
#     print(123)
#     rst = 100 / num
#     print("计算结果是：{0}".format(rst))
# # 捕获异常后，把异常实例化，出错信息会在实例里
# # 注意一下写法
# # 以下语句是捕获ZeroDivisionError异常并实例化实例e
# # 如果是多种error的情况
# # 需要把越具体的错误，越往后放
# # 在异常类继承关系中，越是子类的异常，越要往前放，
# # 越是父亲类的异常，越要往后放
#
# # 在处理异常的时候，一旦拦截到某一个异常，则不在继续往下查看，直接进行下一个代码，
# # 即有finally则执行finally语句块，否则就执行下一个大的语句
# except ZeroDivisionError as e:
#     print('出错了')
#     print(type(e))
#     print(e)
#     # exit是退出程序的意思
#     exit()
# except NameError as e:
#     print("名字起错了")
#     print(e)
#     exit()
# except AttributeError as e:
#     print("好像属性有问题")
#     print(e)
#
# # 所以异常都是继承自Exception
# # 如果写上下面这句话，任何异常都会拦截到
# # 而且，下面这句话一定是最后一个exception
# except Exception as e:
#     print("我也不知道就出错了")
#     print(e)
#
# print('123123')

# # raise 案例
# try:
#     print('我爱王晓静')
#     print("3.14152115")
#     # 手动引发一个类
#     # 注意语法： raise ErrorClassName
#     raise ValueError
#     print("没完呢")
# except NameError as e:
#     print('NameError')
# except ValueError as e:
#     print("ValueError")
# except Exception as e:
#     print("有异常")
#
#
# # raise 案例-2
# # 自己定义异常
# # 需要注意：自定义异常必须是系统异常的子类
# class DanaValueError(ValueError):
#     pass
#
#
# try:
#     print('我爱王晓静')
#     print("3.14152115")
#     # 手动引发一个类
#     # 注意语法： raise ErrorClassName
#     raise DanaValueError
#     print("没完呢")
# except NameError as e:
#     print('NameError')
# except DanaValueError as e:
#     print("DanaValueError")
# except ValueError as e:
#     print("ValueError")
# except Exception as e:
#     print("有异常")
#
#
# # else语句案例
# try:
#     num = int(input("Plz input your number:"))
#     rst = 100 / num
#     print("计算结果是：{0}".format(rst))
# except Exception as e:
#     print("Exception")
#
# else:
#     print("No Exception")
# finally:
#     print("反正我会被执行")
#
#
