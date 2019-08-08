'''
破解有道词典
v1
'''
from urllib import request, parse


def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15652295957532",
        "sign": "219c6502a7c5a955e6c1fc17a8045085",
        "ts": "1565229595753",
        "bv": "3472363b73c04482c6387f36c338e504",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    # 参数data需要是btyes格式
    data = parse.urlencode(data).encode()
    print(len(data))
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
    youdao("girl")
