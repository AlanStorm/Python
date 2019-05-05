# JSON
- 在线工具
    - https://www.sojson.com/
    - http://www.w3school.com.cn/json/
    - http://www.runoob.com/json/json-tutorial.html
- JOSN（JavaScriptObjectNotation）
- 轻量级的数据交换格式，局域ECMAScipt
    - key：字符串
    - value：字符串，数组，列表，json
    - json使用大括号包裹
    - 键值对之间用逗号隔开
    
            student={ "name": "wangdapeng", "age": 18, "mobile":"13260446055" }
            
    - json和python格式的对应
        - 字符串：字符串
        - 数字：数字
        - 队列：list
        - 对象：dict
        - 布尔值：布尔值
- python  for json
    - json包
    - json和python对象的转换
        - json.dumps()：对数据编码，把python格式表示称json格式
        - json.loads()：对数据解码，吧json格式转换成python格式
    - python读取json文件：
        - json.dump(): 把内容写入文件
        - json.load(): 把json文件内容读入python
        - 案例v07
        - 案例v08读取文件