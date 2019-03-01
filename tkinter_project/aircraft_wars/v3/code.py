# v3
# 重构代码，使用oop方法
#   世界的构成：小飞机；打飞机；小蜜蜂；子弹；英雄机；天空
#   配置文件：可以通过一次性配置来让程序正确运行；降低了代码软件冲程方面的成本；
#               python的配置文件包：configparse，以前就叫ConfigParser；
#               配置文件一般已cfg或者ini结尾
#               语法：中括号：白哦是是section；每个section是键值对；价值对用等号或者冒号链接
#               get(section_name, key_name),返回相应的值
#               getint(selection_name, key_name),返回相应的整数值
# 在oop的基础上创建小飞机、蜜蜂等，相对简单很多
# 程序可以正常产生飞行物，包括英雄机、子弹、云层

import configparser

# 第一步生成实例
cfg = configparser.ConfigParser()

# 生成实例后需要读入相应的配置文件
cfg.read("cfg_test.cfg")

sp_name = cfg.get("SmallPlane", "name")
print(sp_name)
sp_width = cfg.getint("SmallPlane", "width")
print(sp_width)
