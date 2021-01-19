# =============================================
# --*-- coding: utf-8 --*--
# @Time    : 2020-05-20
# @Author  : AXYZdong
# @CSDN    : https://blog.csdn.net/qq_43328313
# @FileName: 520.py
# @Software: Python3.7
# =============================================
import turtle as T
import random
import time


# 画樱花的躯干(60,t)
def Tree(branch, t):
    time.sleep(0.0005)
    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')  # 白
            else:
                t.color('lightcoral')  # 淡珊瑚色
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')  # 淡珊瑚色
            t.pensize(branch / 2)
        else:
            t.color('sienna')  # 赭(zhě)色
            t.pensize(branch / 10)  # 6
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()


# 掉落的花瓣
def Petal(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral')  # 淡珊瑚色
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


# 爱心
def Love(x, y):
    t.up()
    t.home()
    t.goto(x, y)
    t.pensize(4)
    t.color('pink', 'pink')  # 粉
    t.left(90)
    t.forward(100)
    t.down()
    t.begin_fill()
    t.circle(70, 230)
    t.forward(140)
    t.end_fill()
    t.begin_fill()
    t.seth(40)
    t.forward(135)
    t.right(5)
    t.circle(70, 235)
    t.end_fill()
    t.up()


# 文字
def Font():
    t.penup()
    t.goto(-500, -300)
    t.pencolor('black')
    t.write("By Alan,不一样的樱花+爱心送给不一样的你，520", font=('方正行黑简体', 30, 'normal'))


# 绘图区域
t = T.Turtle()
# 画布大小
w = T.Screen()
t.hideturtle()  # 隐藏画笔
t.getscreen().tracer(5, 0)
w.screensize(1000, 800, 'wheat')  # wheat小麦
w.setup(width=1.0, height=1.0)
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('sienna')

# 画樱花的躯干
Tree(60, t)
# 掉落的花瓣
Petal(300, t)
# 爱心
Love(-400, 100)
Love(400, 100)
Love(-400, -150)
Love(400, -150)
# 文字
Font()

w.exitonclick()
