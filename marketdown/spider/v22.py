"""
使用参数headers和params
研究返回结果
"""
import requests

url = "http://www.baidu.com"

kw = {
    "wd": "测试"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}
rsp = requests.get(url, params=kw, headers=headers)
print(rsp.text)
print(rsp.content)
print(rsp.url)
