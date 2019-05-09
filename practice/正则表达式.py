import re

# # 匹配一行文字中所有开头的文字
# s = 'i love you but you don\'t love me'
# content = re.findall(r'\b\w', s)
# print(content)
#
#
# # 匹配一行文字中所有数字开头的内容
# s1 = 'i 22love 33you 44but 55you don\'t66 love 77me'
# content = re.findall(r'\b\d', s1)
# print(content)
#
#
# # 匹配只含数字和字符的行
# s2 = 'i love you \n2222kkk but \n kjldasbnf1234 you dont love \n12312'
# content = re.findall(r'\w+', s2, re.M)
# print(content)
#
#
# # 写一个正则表达式，使其能匹配一下字符‘bit’，‘bat’，‘but’，‘hit’，‘hat’，‘but’
# s3 = "'bit','bat','but','hat','hit','hut'"
# content = re.findall(r'..t', s3)
# print(content)
#
#
# # 提取每行中完整的年月日和时间段
# s3 = 'se13312 1987-10-10 22:44:55 akldnfsg;l aknsdfl;k 2018-10-20 09:47:20'
# content = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', s3)
# print(content)
#
#
# # # 提取电子邮件格式
# s4 = """xxxxx@gamail.com xxxx@qq.com baidu.com 999.com ksks@134.com"""
# # content = re.findall(r'\w+@\w+.com', s4)
# # print(content)
# # 把以上合法的电子邮件地址替换成我自己的电子邮件地址
# content = re.sub(r'\w+@\w+.com', '瓦楞曼德拉看什么@.com', s4)
# print(content)
#
#
# 使用正则提取字符串中的单词
s5 = 'i love you not because who 344 of 324sda not'
content = re.findall(r'\b[a-zA-Z]+\b', s5)
print(content)
