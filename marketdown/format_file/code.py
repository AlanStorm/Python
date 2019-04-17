import re

#
# p = re.compile(r'\d+')
#
# m = p.match('one12towthress33456four78', 3, 90)
# print(m)
#
#
# # re.I 表示忽略大小写
# p = re.compile(r'([a-z]+) ([a-z]+)', re.I)
# m = p.match('I am really love wangxiaojing')
# print(m.group(0))
# print(m.start(0))
# print(m.end(0))
#
# print(m.group(1))
# print(m.start(1))
# print(m.end(1))
#
# print(m.group(2))
# print(m.start(2))
# print(m.end(2))
#
# print(m.groups())
#
#
# # 查找
# p = re.compile(r"\d+")
# m = p.search('one12two34three567four')
# print(m.group())
#
# rst = p.findall('one12two34three567four')
# print(type(rst))
# print(rst)
#
#
# # sub替换
# p = re.compile(r"(\w+) (\w+)")
# s = "hello 123 wang 456 xiaojing, i love you"
# rst = p.sub(r"Hello world", s)
# print(rst)
#
#
# # 匹配中文
# # 大部分中文内容表示范围是[u4c00-u9fa5]，不包括全角标点
# title = u"世界 你好， hello moto"
# p = re.compile(u"[\u4c00-\u9fa5]+")
# rst = p.findall(title)
#
# print(rst)
#
#
# 贪婪和非贪婪
# 贪婪：尽可能多的匹配，（*）表示贪婪匹配
# 非贪婪：找到符合条件的最小内容即可，（?）表示非贪婪
# 正则默认使用贪婪匹配
title = u"<div>name</div><div>age</div>"

p1 = re.compile(r"<div>.*</div>")
p2 = re.compile(r"<div>.*?</div>")

m1 = p1.search(title)
print(m1.group())

m2 = p2.search(title)
print(m2.group())
