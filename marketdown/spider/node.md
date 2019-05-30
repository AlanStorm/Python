# 0 爬虫准备工作
- 参考资料
    - python网络数据采集 · 图灵工业出版
    - 精通Python爬虫框架Scrapy · 人民邮电出版社
    - [Python3网络爬虫]（http://blog.csdn.net/c406495762/article/details/72858983）
    - [Scrapy官方教程]（https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html）
- 前提知识
    - url
    - http协议
    - web前端·html，css，js
    - ajax
    - re，xpath
    - xml
# 1. 爬虫简介
- 爬虫定义：网络爬虫（又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），
 是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。 另外一些不常使用的名字还有蚂蚁、
 自动索引、模拟程序或者蠕虫。
- 两大特征：
    - 能按作者要求下载数据或者内容
    - 能自动在网络上流窜
- 三大步骤：
    - 下载信息
    - 提取正确的信息
    - 根据一定规则自动跳转待另外的网页上执行上两步内容
- 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）
- Python网络包简介
    - Python2.x：urllib, urllib2, urllib3, httplib, httplib2, requests
    - Python3.x: urllib, urllib3, httplib2, requests
    - Python2: urllib和urllib2配合使用，或者requests
    - Python3： urllib，requests
# 2. urllib
- 包含模块
    - urllib.request：打开和读取urls
    - urllib.error：包含urllib.request产生的常见的错误·使用try捕获
    - urllib.parse：包含解析urls的方法
    - urllib.robotparse：解析robots.txt文件
    - 案例v1

- 网页编码问题解决
    - chardet 可以自动检测页面文件的编码格式，但是，可能有误
    - 需要安装, canda install chardet
    - 案例v2
    
- urlopen 的返回对象
    - 案例v3
    - geturl：返回请求对象的url
    - info：请求返回对象的meta信息
    - getcode：返回的http code
- request data 的使用
    - 访问网络的两种方法
        - get：
            - 利用参数给服务器传递信息
            - 参数为dict，然后用parse编码
            - 案例v4
        - post
            - 一般想服务器传递参数使用
            - post是把信息自动加密处理
            - 我们如果想使用post信息，需要用到data参数
            - 使用post，意味着http的请求头可能需要更改：
                - Content-Type: application/x-www.form-urlencode
                - Content-Length：数据长度
                - 简而言之，一旦更改请求方法，请注意其他请求头信息相适应
            - urllib.parse.urlencode可以将字符串自动转换成上面的                
            - 案例v5
            - 为了更多的设置请求信息，单纯的通过urkopen函数已经不太好用了
            - 需要利用request.Request 类
            - 案例v6
   
    