from urllib import request, parse
from http import cookiejar

# 创建 cookiejar的实例
cookie = cookiejar.CookieJar()
# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(https_handler, https_handler, cookie_handler)


def login():
    '''
    负责首次登录
    需要输入用户名密码，用来获取cookie凭证
    :return:
    '''
    # url需要从登录form的action属性中提取
    url = 'https://www.testin.cn/account/login/commit.htm'
    # 此键值需要从登录form的两个对用input中提取name属性
    data = {
        "email": "826041522@qq.com",
        "pwd": "826sunhao"
    }
    # 吧数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)

    rsp.read().decode("utf-8")


if __name__ == '__main__':
    '''
    执行完login之后，会得到授权之后的cookie
    我们尝试把cookie打印出来
    '''
    login()
    print(cookie)
    for item in cookie:
        print(type(item))
        print(item)
        for i in dir(item):
            print(i)
