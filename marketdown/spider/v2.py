"""
利用request下载页面
自动检测页面编码
"""
import urllib
from urllib import request
import chardet

if __name__ == '__main__':
    url = 'https://baike.baidu.com/item/CSS/5457?fr=aladdin'

    rsp = urllib.request.urlopen(url)

    html = rsp.read()

    # 利用chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)
