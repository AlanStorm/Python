from urllib import request, parse
from http import cookiejar

# 创建 cookiejar的实例
cookie = cookiejar.MozillaCookieJar()
cookie.load("cookie.txt", ignore_expires=True, ignore_discard=True)
# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(https_handler, https_handler, cookie_handler)


def get_home_page():
    url = 'https://www.testin.cn/user/personal_info.htm'

    # 如果已经执行了login函数，到opener自动已经包含相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode("utf-8")

    with open('rsp.html', "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == '__main__':
    get_home_page()
