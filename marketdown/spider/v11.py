from urllib import request

if __name__ == '__main__':
    url = 'https://www.renren.com/965187997/profile'

    rsp = request.urlopen(url)

    html = rsp.read().decode("utf-8")
    print(html)
    with open('rsp.html', "w", encoding="utf-8") as f:
        f.write(html)
