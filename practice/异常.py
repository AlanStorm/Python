# def jianfa(a, b):
#     if a < b:
#         raise BaseException("被减数不能小于减数")
#     else:
#         return a - b
#
#
# try:
#     jianfa(3, 7)
# except BaseException as error:
#     print("好像出错了，出错的内容是{}".format(error))
# import os
#
#
# def func(filename):
#     try:
#         file = open(filename)
#     except Exception as error:
#         print("出错啦，出错的内容是{}".format(error))
#     else:
#         print(file.read())
#         file.close()
#
#
# func('12312.text')
class MyError(Exception):
    def __init__(self, stri):
        self.stri = stri

    def process(self):
        if len(self.stri) < 5:
            print("字符串的长度必须大于5")
        else:
            print('算你聪明')


try:
    er = MyError("sssss")
    er.process()
except MyError as error:
    print(error)
