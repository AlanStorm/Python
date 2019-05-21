"""
利用request下载页面
自动检测页面编码
"""
import urllib
from urllib import request

if __name__ == '__main__':
    url = 'https://baike.baidu.com/item/CSS/5457?fr=aladdin'

    rsp = urllib.request.urlopen(url)
    print(type(rsp))
    print(rsp)

    print('Url:{0}'.format(rsp.geturl()))
    print('Info:{0}'.format(rsp.info()))
    print('Code:{0}'.format(rsp.getcode()))

    html = rsp.read()

    html = html.decode()
    # print(html)
