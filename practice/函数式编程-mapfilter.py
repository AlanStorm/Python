# def standard(s):
#     t = "0"
#     t = s.lower()  # 字符串小写
#     t = t.capitalize()  # 将首字母大写
#     print(t)
#     return t
#
#
# list(map(standard, ['DMind', 'JASD']))
# def equal(a, b):
#     return a == b
#
#
# def is_palindrone(n):
#     s = str(n)  # 先转换成字符串
#     for i in range(len(s) - 1):
#         if equal(s[i], s[len(s) - i - 1]):
#             continue
#         else:
#             return False
#     return True
#
#
# output = filter(is_palindrone, range(1, 1000))
# print('1-1000', list(output))
L = [("Bob", 75), ("Adam", 93), ('Bart', 66), ('List', 88)]


def by_name(t):
    t = sorted(t[0], key=str.lower)
    return t


L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    t = sorted(range(t[1]), key=abs)
    return t


L2 = sorted(L, key=by_score)
print(L2)
