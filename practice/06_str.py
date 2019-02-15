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

# 用实验证明部分切片和完整切片的区别
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l1 = l[:6]
print(l1)
print(id(l))
print(id(l1))
