# # 链接操作
# s1 = "I love"
# s2 = "wangxiaojiang"
#
# s3 = s1 + " " + s2
# print(s3)
#
# # 字符串的乘法
# s = "I love wangxiangjing"
# print(s * 12)
#
# 字符串当成列表
# s = "I love wangxiangjia"
# print(s[0])
# # 切片返回的是一个新的字符串吗？
# # 如果切去一部分，则返回全新字符串
# # 如果取完整切片，可以返回内容指向同一字符串
# print(s[-1])
# print(s[2:6])
# print(s[:])
# print((id(s)))
# print((id(s[:])))
#
# s1 = s[:]
# print(s1)
# s1[0] = 'aaa'
# print(s1)
# print(id(s1))
# print(s)
# print(id(s))
#
# # 用实验证明部分切片和完整切片的区别
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# l1 = l[:6]
# print(l1)
# print(id(l))
# print(id(l1))
#
# # capitalize首字母大写，其余小写，返回字符串
# s = "i  LOVE  ZHang"
# print(s.capitalize())
#
# # title() 将每个单词的手机木变为大写 ，返回字符串
# s = "i love WangSSDASD"
# s1 = s.title()
# print(s1)
#
# # upper() 将所有字母变为大写字母，返回字符串
# s = "I like dog"
# print(s.upper())
#
# # lower() 将所有字母变为大写字母，返回字符串
# s = "I like dog"
# print(s.lower())
#
# # swapcase() 大小写互换 返回的是字符串
# s = "I like Dog"
# print(s.swapcase())
#
# # len() 计算字符串长度，不属于字符串的内建函数
# len统计长度是按照字符格式统计，一个汉字的长度为一
# s = "I 够like dog"
# s1 = "I like dog"
# print(len(s))
# print(len(s1))
#
# # find() 查找指定字符串，找不到返回-1，第一次返回第一索引值
# # index() 查找制定字符串，找不到报错
# s = 'asdasdasasdasdasd'
# s1 = s.find('s', 3)
# s2 = s.index('a')
# print(s1)
# print(s2)
#
# # count() 计算字符串出现次数 返回整型
# s = 'asdjhabfkjhds'
# print(s.count('s'))
#
# # startswith() 检查是否以制定字母开头 返回布尔值
# # endswith() 检查是否以指定字母结束
# s = "I like dog"
# print(s.startswith("i"))
# print(s.startswith("I"))
# print(s.endswith('s'))
# print(s.endswith('g'))

# isupper() 检测所有字母是否是大写字母，返回布尔值
# islower() 检测所有字母是否是小写字母，返回布尔值
# istitle() 检测是否已指定标题显示（每个单词首字母大写）
# isspace() 检测字符串是否是空字符串
# isalpha() 检测字符串是否是字母组成 返回布尔值 说明，汉字在英文字符包裹中被当做字符处理
# isalnum() 检测字符串是否有字母加数组组成 返回布尔值
# isdigit() 检测字符串是否由数字组成
# isdecimal() 检测字符串是否由数字组成
# isnumeric() 检测字符串是否由数字组成
# split() 用指定字符切割字符串，返回字符串组成的列表
# splitlines() 以换行切割字符串
# join() 将列表按照指定字符串链接 返回的是字符串
# ljust() 指定字符串的长度，内容靠左边，不足的位置用指定字符串填充，默认空格，返回字符串
# center() 指定字符串长度，内容居中，不足的位置用指定字符串填充，默认空格，返回字符串
# rjust() 指定字符串长度，内容靠右边，不足的位置用指定字符串填充，默认空格，返回字符串
# strip() 去掉左右两边指定字符串，默认是去掉空格
# lstrip() 去掉左两边指定字符串，默认是去掉空格
# rstrip() 去掉右两边指定字符串，默认是去掉空格
# zfill() 指定字符串长度，内容靠右，不足的位置用0填充
# maketrans() 生册亨用于字符串替换的映射表
# translate() 进行字符串替换



