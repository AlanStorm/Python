# 常用模块
- calendar
- time
- datetime
- timeit
- os
- shutil
- zip
- math
- string
- 上述所有模块使用理论上都应该先导入，string是特例
- calendar，time，datetime的区别参考中文意思
# calendar
- 跟日历相关的模块

# time模块
### 时间戳
    - 一个时间表示，根据不同语言，可以试整数后者浮点数
    - 是从1970年1月1日0时0分0秒到现在经历的秒数
    - 如果表示的时间是1970年以前或者太遥远的未来，可能出现异常
    - 32位操作系统能知道到2038年
### UTC时间
    - UTC又称为世界协调时间，以英国的格林尼治天文所所在的地区的时间
    作为参考的时间，也叫做世界标准时间。
    - 中国时间是 UTC+8 东八区
### 夏令时
    - 夏令时就是在夏天的时候将时间调快一小时，本意是督促大家早睡早起
    节省蜡烛！每天变成25个小时，本质没变好事24小时
### 时间元组
    - 一个包含时间内容的普通元组
            
                
                索引      内容      属性      值
                0         年        tm_year  2015
                1         月        tm_mon   1-12
                2         日        tm_hour  1-31
                3         时        tm_hour  0-23
                4         分        tm_min   0-59
                5         秒        tm_sec   0-61 60表示闰秒 61保留值
                6         周几      tm_wday  0-6 
                7         第几天    tm_yday  1-366  
                8         夏令时    tm_isdst 0,1，-1 （表示夏令时）
        

# strftime：将时间元组转换成自定义的字符串格式
# datetime模块
- datetime 提供日期和时间的运算和表示
# datetime.datetime 模块
- 提供比较好用的时间而已
# OS - 操作系统相关
- 跟操作系统相关，主要是文件操作
- 与系统相关的操作，主要包含在三个模块里
    - os ，操作系统目录相关
    - os.path，系统路径相关操作
    - shutil，高级文件操作，目录树的操作，文件赋值，删除，移动
- 路径 
    - 绝对路径：总是从根目录上开始
    - 相对路径：基本以当前环境为开始的一个相对的地方
# 值部分
- os.cudir：curretn dir,当前目录
- os.pardir: parent dir,父目录
- os.sep：当前系统的路径分隔符
    - windows："\"
    - linux："/"
- os.linesep：当期系统的换行符
    - windows："\r\n"
     - unix,linux,macos："\n"
- os.name：当前系统名称    
    - windows：nt
    - mac，unix，linux：posix
# shutil 模块
# 归档和压缩
- 归档：把多个文件或者文件夹合并到一个文件当中
- 压缩：用算法吧过个文件或者文件夹无损或者有损合并到一个文件当中
    
