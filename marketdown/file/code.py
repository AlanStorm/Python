# # 打开文件，用写的方式
# # r表示后面的字符串内容不需要转义
# # f 称之为文件句柄
# f = open(r"text01.txt", 'w')
#
# # 文件打开后必须关闭
# f.close()
#
# # 此案例说明，已写方式打开文件，默认是如果没有文件，则创建
#
#
# # with语句案例
# with open(r"test01.txt", 'r') as f:
#     pass
#     # 下面语句块开始对文件f进行操作
#     # 在本模块中不需要在使用close关闭文件f
#
#
# with open(r"test01.txt", 'r') as f:
#     # 按行读取内容
#     strline = f.readline()
#     # 此结构保证能够完整去读文件直到结束
#     while strline:
#         print(strline)
#         strline = f.readline()
#
#
# list能用打开的文件作为参数，把文件内每一行内容作为一个元素
# with open(r"test01.txt", 'r') as f:
#     # 已打开的文件饭作为参数，创建列表
#     l = list(f)
#     for i in l:
#         print(i)
#
#
# # read是按字符读取文件内容
# # 允许输入参数决定读取几个字符，如果没有指定，从当前位置读取到结尾
# # 否则，从当前位置读取指定个数字符
# with open(r"test01.txt", 'r') as f:
#     strChar = f.read()
#     print(len(strChar))
#     print(strChar)
#
#
# # seek案例
# # 打开文件后，从第5个字节处开始读取
# # 打开读写指针在0处，即文件的开头
# with open(r"test01.txt", 'r') as f:
#     # seek移动单位是字节
#     f.seek(4, 0)
#     strChar = f.read()
#     print(strChar)
#
#
# # 关于读取文件的联系
# # 打开文件，三个字符一组独处内容，然后显示在屏幕上
# # 每读一次，休息疫苗
#
# # 让程序暂停，可是使用time下的sleep函数
# import time
#
# with open(r"test01.txt", 'r') as f:
#     # read参数的单位是字符，可以理解称一个汉字就是一个字符
#     strChar = f.read(3)
#     while strChar:
#         print(strChar)
#         # sleep参数单位是秒
#         time.sleep(1)
#         strChar = f.read(3)
#
#
# # tell函数：用来显示文件读写指针的当前位置
# with open(r"test01.txt", 'r') as f:
#     strChar = f.read(3)
#     pos = f.tell()
#     while strChar:
#         print(pos)
#         print(strChar)
#         strChar = f.read(3)
#         pos = f.tell()
# # 以上结果说明：
# # tell的返回数字的单位是byte
# # read是已字符为单位
#
#
# # write案例
# # 1.向文件追加一句诗
# # a代表追加方式打开
# with open(r"test01.txt", 'a') as f:
#     # 注意字符串内含有换行符
#     f.write('\n生活不仅有眼前的苟且,\n还有远方的苟且')
#
#
# # 可以直接写入行，用writelines
# # writelines表示写入很多行，参数可以是list格式
# # a代表追加方式打开
# with open(r"test01.txt", 'a') as f:
#     # 注意字符串内含有换行符
#     l = ['I', 'love', 'wang']
#     f.writelines(l)
#
#
# # 序列化案例
# import pickle
#
# age = 19
#
# with open(r'test01.txt', 'wb') as f:
#     pickle.dump(age, f)
#
# # 反序列化案例
# import pickle
#
# with open(r'test01.txt', 'rb') as f:
#     age = pickle.load(f)
#     print(age)
#
#
# # 序列化案例
# import pickle
#
# age = [19, 'lida0', '1i love asd ', [123, 13]]
#
# with open(r'test01.txt', 'wb') as f:
#     pickle.dump(age, f)
#
#
# # 使用shelve创建文件并使用
# import shelve
#
# # 打开文件
# # shv相当于一个字典
# shv = shelve.open(r"shv.db")
# shv['one'] = 1
# shv['two'] = 2
# shv['three'] = 3
#
# shv.close()
# # 通过以上案例发现，shelve自动创建的不仅仅是一个shv.代表文件，还包括其他文件
#
#
# # shelve读取案例
# import shelve
#
# shv = shelve.open(r'shv.db')
#
# try:
#     print(shv['one'])
#     print(shv['theree'])
# except Exception as e:
#     print("烦死额")
# finally:
#     shv.close()
#
#
# # shelve 只读方式打开
# import shelve
#
# shv = shelve.open(r'shv.db', flag='r')
#
# try:
#     k1 = shv['one']
#     print(k1)
# finally:
#     shv.close()
#
#
# import shelve
#
# shv = shelve.open(r'shv.db')
#
# try:
#     shv['one'] = {'eins': 1, 'zwei': 2, 'drei': 3}
#     shv["name"] = 'lidana'
# finally:
#     shv.close()
#
# shv = shelve.open(r'shv.db')
#
# try:
#     one = shv['one']
#     print(one)
# finally:
#     shv.close()
#
# # shelve 忘记写回，需要强制写回
# import shelve
# # shelve忘记写回，需要使用强制写回
# shv = shelve.open(r'shv.db', writeback=True)
# try:
#     k1 = shv['one']
#     print(k1)
#     # 此时，一旦shelve关闭，则内容还是存在与内存中，没有写回数据库
#     k1['eins'] = 100
# finally:
#     shv.close()
#
# shv = shelve.open(r'shv.db')
#
# try:
#     one = shv['one']
#     print(one)
# finally:
#     shv.close()
#
#
# shelve 使用with管理上下文环境
# import shelve
#
# with shelve.open(r'shv.db', writeback=True) as shv:
#     k1 = shv['one']
#     print(k1)
#     # 此时，一旦shelve关闭，则内容还是存在与内存中，没有写回数据库
#     k1['eins'] = 100
#
# with shelve.open(r'shv.db', writeback=True) as shv:
#     print(shv['one'])
