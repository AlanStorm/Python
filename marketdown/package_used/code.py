import calendar
import time
import datetime
from datetime import datetime, timedelta
from datetime import datetime
import os
import os.path as op

# calendar: 获取一年的日历字符串
# 参数
# w = 每个日期之间的间隔字符数
# l = 每周所占用的行数
# c = 每个月之间的间隔字符数
cal = calendar.calendar(2017, l=0, c=3)

# isleap：判断某一年是否闰年
isleap = calendar.isleap(2007)

# leapdays：获取指定年份之间的闰年的个数
leapdays = calendar.leapdays(1998, 2018)

# mouth() 获取某个月的日历字符串
# 格式：calendar.mouth(年，月)
# 返回值：月日历的字符串
m3 = calendar.month(2018, 2)

# monthrange() 获取一个月的周几开始及总天数
# 格式：calendar.monthrange（年，月）
# 返回值：元组（周几开始，总天数）
# 注意：周默认 0-6，表示周一到周天
w, t = calendar.monthrange(2017, 3)

# monthcalendar() 返回一个月每天的矩阵列表
# 格式：calendar.monthcalendar(年，月)
# 返回值：二级列表
# 注意：矩阵中没有天数用0表示
m = calendar.monthcalendar(2018, 3)

# prcal：直接打印日历
# calendar.prcal(2018)
# help(calendar.prcal)

# prmonth() 直接打印整个月的日历
# 格式：calendar.permonth(年，月)
# 返回值：无
# calendar.prmonth(2018, 3)

# weekday() 获取周几
# 格式：calendar.weekday(年，月，日)
# 返回值：周几对应的数字
weekday = calendar.weekday(2018, 2, 2)

# 时间模块
# timezone：当期时区和UTC时间差的描述，在没有夏令时的情况下的间隔，东八区的是-28800
# altzone：获取当前时区与UTC时间差的秒数，在有夏令时的情况下
# daylight 测试当前是否是夏令时时间状态，
# print(time.timezone)

# 得到时间戳
t = time.time()

# localtime，得到当前时间的时间结构
# 可以通过点号操作符得到相应的属性元素的内容
t = time.localtime()

# asctime() 返回元组的正常字符串化之后的时间格式
# 格式：time.asctime（时间元组）
# 返回值：字符串 Tue Jun 6 11:11:00 2017
t = time.asctime()

# ctime：获取字符串化的当前时间
t = time.ctime()

# mktime() 使用时间元组获取对应的时间戳
# 格式：time.mktime(时间元组)
# 返回值：浮点数时间戳
lt = time.localtime()
ts = time.mktime(lt)

# clock：获取cpu时间，3.0 - 3.3版本直接使用，3.6调用有问题

# sleep：是程序进入睡眠，n秒后继续
time.sleep(1)

# 把时间表示称，2018年3月26日 21:05
t = time.localtime()
ft = time.strftime("%Y %m %d %H:%M", t)

# datetime常见属性
# datetime.date：一个理想的日期，提供year，mouth，day属性
# print(datetime.date(2018, 3, 26))

# datetime.time：提供一个理想的时间，提供hour，minute，sec，microsec等内容
# datetime.datetime：提供日期跟时间的组合
# datetime.timedelta：提供一个时间差，时间长度

# datetime.datetime

# 常用方法
# today：
# now
# utcnow
# fromtimestamp：从时间戳中返回本地时间
# dt = datetime(2018, 9, 26)
# print(dt.today())
# print(dt.now())
# print(dt.fromtimestamp(time.time()))


t1 = datetime.now()
# print(t1)
# print(t1.strftime("%Y-%m-%d %H:%M:%S"))
# td表示一小时的时间长度
td = timedelta(hours=1)


# 当前时间加上时间间隔后，得到一个小时后的时间
# print((t1 + td).strftime("%Y-%m-%d %H:%M:%S"))

# timeit-时间测量工具
# 测量测序运行时间间隔实验
def p():
    time.sleep(3.6)


t1 = time.time()
# p()
# print(time.time() - t1)
# 生成列表两种方法的比较
# 如果单纯比较生成一个列表的时间，可能很难实现
c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''
import timeit

# 利用timeit调用代码，执行100000，查看运行时间
# t1 = timeit.timeit(stmt="[i for i in range(1000)]", number=100000)
# 测量代码c执行100000次运行结果
# t2 = timeit.timeit(stmt=c, number=100000)
# print(t1)
# print(t2)
# timeit 可以执行一个函数，来测量一个函数的执行时间
# def doIt():
#     num = 3
#     for i in range(num):
#         print("Repeat for {0}".format(i))
#
#
# t = timeit.timeit(stmt=doIt, number=10)
# print(t)
s = """
def doIt(num):
    for i in range(num):
        print("Repeat for {0}".format(i))
"""
# 执行doIt(num)
# setup负责吧环境变量准备好
# 实际相当于给timi创再来个一个小环境
# 在创建的小环境中，代码执行的顺序大致是
#
"""
def doIt(num):
    ....
num = 3
doIt(num)
"""
# t = timeit.timeit("doIt(num)", setup=s + "num=3", number=10)

# getcwd() 获取当期的工作目录
# 格式： os.getcwd()
# 返回值：当前工作目录的字符串
# 当前工作目录就是程序在进行文件相关操作，默认查找文件的目录
mydir = os.getcwd()

# chdir() 改变当前的工作目录
# change directory
# 格式： os.chdir(路径)
# 返回值：无
# os.chdir('G:\Python\marketdown')
# mydir = os.getcwd()

# listdiir() 获取一个目录中所有子目录和文件的名称列表
# 格式： os.listdir（路径）
# 返回值：所有子目录和文件名称的列表
ld = os.listdir()

# makedir() 递归创建文件夹
# 格式：os.makedirs(递归路径)
# 返回值：无
# 递归路径：多个文件夹层层包换的路径就是递归路径，例如 a/b/c
# rst = os.makedirs('test')

# system() 运行系统shell命令
# 格式： os.system(系统命令)
# 返回值：打开一个shell或者终端界面
# 一般推荐使用subprocess代替
# rst = os.system("dir")

# getenv() 获取指定的系统环境变量值
# 格式：os.getenv('环境变量名')
# 返回值：指定环境变量名对应的值
rst = os.getenv('PATH')

# exit() 退出当前程序
# 格式：exit()
# 返回值：无

# abspath() 将路径转换成绝对路径
# abselute 绝对
# 格式：os.path.abspath('路径')
# 返回值：路径的绝对路径形式
# 在linux中
# . 点号，代表当前目录
# .. 双点，代表父目录
absp = op.abspath(".")

# basename() 获取路径中的文件名部分
# 格式：os.path.basename('路径')
# 返回值：文件名字符串

# join() 将多个路径拼合成一个路径
# 格式：os.path.join(路径1，路径2)
# 返回值：组合之后的新路径字符串

# split() 将路径切割成文件夹部分和当期文件部分
# 格式：os.path.split(路径)
# 返回值：路径和文件名组成的元祖

# isdir() 检测是否是目录
# 格式： os.path.isdir(路径)
# 返回值：布尔值

# exists() 检测文件或者目录是否存在
# 格式：os.path.exists(路径)
# 返回值：布尔值

# copy() 复制文件
# 格式： shutil.copy(来源路径，目标路径)
# 返回值：返回目标路径
# 拷贝的同时，可以给文件重命名

# copy2() 复制文件，保留元数据（文件信息）
# 格式：shutil.copy2(来源路径，目标路径)
# 返回值：返回目标路径
# 注意：copy和copy2的唯一区别在于copy2复制文件时尽量保留元数据

# copyfile() 将一个文件中的内容复制到另一个文件当中
# 格式：shutil.copyfile（'源路径','目标路径'）
# 返回值：无

# move() 移动文件/文件夹
# 格式： shutil.move('源路径','目标路径')
# 返回值：目标路径

# make_archive() 归档操作
# 格式：shutil.make_archive('归档之后的目录和文件名','后缀','需要归档的文件夹')
# 返回值：归档之后的地址


