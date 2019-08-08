'''
破解有道词典
'''
'''
v2
处理js加密代码中操作代码
1.计算salt公式 r = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10);
2.计算sign公式   n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
md5一共需要四个参数，，第一个和第四个都是固定的字符串，第三个是所谓的salt，第二个参就是输入的要查找的单词
'''
from urllib import request, parse


def getSalt():
    '''
    salt公式是： "" + (new Date).getTime() + parseInt(10 * Math.random(), 10);
    把他翻译成python代码
    :return:
    '''
    import time, random

    salt = int(time.time() * 1000) + random.randint(0, 10)

    return salt


def getMD5(v):
    import hashlib
    md5 = hashlib.md5()

    md5.update(v.encode('utf-8'))

    sign = md5.hexdigest()

    return sign


def getSign(key, salt):
    sign = "fanyideskweb" + key + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
    sign = getMD5(sign)
    return sign


def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    salt = str(getSalt());
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": getSign(key, salt),
        "ts": "1565229595753",
        "bv": "3472363b73c04482c6387f36c338e504",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    # 参数data需要是btyes格式
    data = parse.urlencode(data).encode()

    headers = {
        "Accept": "application/json,text/javascript,*/*;q=0.01",
        # "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-1833580039@10.168.8.76; JSESSIONID=aaa8BYGxU4IsBaPD2ZUXw; OUTFOX_SEARCH_USER_ID_NCOO=1713848572.2436023; ___rl__test__cookies=1565229595747",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode('utf-8')

    print(html)


if __name__ == '__main__':
    youdao("boy")
