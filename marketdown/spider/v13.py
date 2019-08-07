from urllib import request, parse
from http import cookiejar

# 创建 cookiejar的实例
cookie = cookiejar.CookieJar()
# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建爱你http请求管理器
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
        "pwd": ""
    }
    # 吧数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)

    rsp.read().decode("utf-8")


def get_home_page():
    url = 'https://www.testin.cn/user/personal_info.htm'

    # 如果已经执行了login函数，到opener自动已经包含相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode("utf-8")

    with open('rsp.html', "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == '__main__':
    login()
    get_home_page()
