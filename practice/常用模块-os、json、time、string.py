# import random
# import string
#
# code = []
# code.append(random.choice(string.ascii_lowercase))  # 保证验证码中有一个小写字母
# code.append(random.choice(string.ascii_uppercase))  # 保证验证码中有一个大写字母
# code.append(random.choice(string.digits))  # 保证验证码中有一个数字
# while len(code) < 6:
#     code.append(random.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase))
# print(code)
# q_code = "".join(code)
# print(q_code)
import os
import time
import json

count = 0
exit_flag = False

while count < 3:
    user = input('请输入用户名')
    f = user.strip() + ".json"
    if os.path.exists(f):
        fp = open(f, 'r+', encoding='utf - 8')
        j_user = json.load(fp)
        if j_user['status'] == 1:
            print('账号已经锁定')
            break
        else:
            expire_dt = j_user['expire_date']
            current_st = time.time()
            expire_st = time.mktime(time.strptime(expire_dt, '%Y-%m-%d'))
            if current_st > expire_st:
                print('用户已过期')
                break
            else:
                while count < 3:
                    pwd = input('请输入密码：')
                    if pwd.strip() == j_user['password']:
                        print('登陆成功')
                        exit_flag = True
                        break
                    else:
                        if count == 2:
                            print("用户登陆已经超过3次，锁定账号")
                            j_user['status'] = 1
                            fp.seek(0)
                            fp.truncate()  # 清空文件内容
                            json.dump(j_user, fp)
                    count += 1

    if exit_flag:
        break
    else:
        print("用户不存在")
        count += 1
