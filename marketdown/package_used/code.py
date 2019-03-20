import calendar
import time

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

#
t = time.localtime()
print(t)
