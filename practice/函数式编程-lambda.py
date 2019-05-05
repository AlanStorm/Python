# ls = ["ADMAm", "LISA", "JACk"]
#
# new_ls = map(lambda x: x.lower().capitalize(), ls)
#
# print(list(new_ls))
#
#
# 打印1到1000之间的回数
# ls = range(1000)
#
# new_ls = filter(lambda x: str(x)[0] == str(x)[len(str(x)) - 1], ls)
#
# print(list(new_ls))
#
#
ls = [("Bob", 75), ("Adam", 93), ('Bart', 66), ('List', 88)]

new_ls = sorted(ls, key=lambda x: x[0], reverse=True)
print(list(new_ls))

new_ls = sorted(ls, key=lambda x: x[1])
print(list(new_ls))
