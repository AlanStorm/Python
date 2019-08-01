from urllib import request

if __name__ == '__main__':
    url = 'https://www.renren.com/965187997/profile'

    headers = {
        "Cookie": 'ick_login=bfd8dc44-8e44-4122-85dc-c217d92c25b0; anonymid=jyqxrt9mbleh4m; depovince=GW; _r01_=1; JSESSIONID=abcLYK3E18nC0basr9gXw; t=22eaf275208883b0f654918c0e038cd25; societyguester=22eaf275208883b0f654918c0e038cd25; id=971714855; xnsid=b904b0b4; jebecookies=b32edfd1-0b58-4f59-9d58-f683d361c6fc|||||; ver=7.0; loginfrom=null; jebe_key=c2d47026-2aed-421d-ac10-b4fb5ac59ff4%7Cb65ff731e42b66f4f8f8492e07232ef7%7C1564558972450%7C1%7C1564558970310; jebe_key=c2d47026-2aed-421d-ac10-b4fb5ac59ff4%7Cb65ff731e42b66f4f8f8492e07232ef7%7C1564558972450%7C1%7C1564558970313; wp_fold=0'
    }

    rep = request.Request(url, headers=headers)

    rsp = request.urlopen(rep)

    html = rsp.read().decode("utf-8")

    with open('rsp.html', "w", encoding="utf-8") as f:
        f.write(html)
