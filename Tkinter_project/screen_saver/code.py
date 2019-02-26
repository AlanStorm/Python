# Tkinter项目实战-屏保
# 项目分析：屏保可以自己启动，也可以手动启动
#           一旦敲击键盘后者移动鼠标后，或者其他的已发事件，则停止
#           如果屏保是一幅画的话，则没有画框
#           图像的动作是随机的，具有随机性，可能包括颜色、大小、多少、运动方向、变形等
#           整个世界的构成是：
#               - ScreenSaver：需要一个cancas，大小与屏幕一致，没有边框；
#               - Ball：颜色、大小、多少、运动方向、变形等随机；球能动，可以被调用
import random
import tkinter


class RandomBall:
    """
    定义运动的球的类
    """

    def __init__(self, canvas, screen_width, screen_height):
        """
        :param canvas:画布，所有内容都应该在糊不上呈现出来，此处通过次变量传入
        :param screen_width: 屏幕宽
        :param screen_height: 屏幕高
        """
        # 球出现那的出事位置要随机，此处表示球的圆心
        # xpos表示位置的x坐标
        self.xpos = random.randint(10, int(screen_width) - 20)
        # ypos表示位置的y坐标
        self.ypos = random.randint(10, int(screen_height) - 10)

        # 定义球运动的速度
        # 模拟运动：不断的擦掉原来的画，然后在一个新的地方在重新绘制
        # 此处xvelocity模拟x轴方向运动
        self.xvelocity = random.randint(4, 20)
        # 同理，yvelocity模拟y轴方向运动
        self.yvelocity = random.randint(4, 20)

        # 定义屏幕的大小
        self.screen_width = screen_width
        # 定义屏幕的高度
        self.screen_height = screen_height

        # 球的大小随机
        # 此处球的大小用半径表示
        self.radius = random.randint(20, 120)

        # 定义颜色
        # RGB表示法：三个数组，每个数组的值是0-255之间，表示红绿蓝三个颜色的大小
        # 在某些系统中，之间用英文代词表示也可以，比如red，green
        # 此处用lambda表达式

        c = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x' % (c(), c(), c())

    def create_ball(self):
        """
        用构造函数定义的变量值，在canvas上画一个球
        :param self:
        :return:
        """
        # tkinter没有画形函数
        # 只有一个画椭圆函数，画椭圆需要定义两个坐标
        # 在一个长方形内画椭圆，我们只需要定义长方形左上角和右下角就好
        # 求两个坐标的方法是，已知圆心的坐标，则圆心坐标减去半径能求出
        # 左上角坐标，加上半径能求出右下角坐标
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.xpos + self.radius

        # 再有两个对角坐标的前提下，可以进行画圆
        # fill表示填充颜色
        # outline是外围边框颜色
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def move_ball(self):
        # 移动球的时候，需要控制球的方向
        # 每次移动后，球都有一个新的坐标
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity

        # 以下判断是否撞墙
        # 撞了墙就要回头
        # 注意撞墙的算法判断
        if self.xpos + self.radius >= self.screen_width:
            # 撞到了右边墙
            self.xvelocity = -self.xvelocity
            # self.xvelocity *= -1
        if self.xpos - self.radius <= 0:
            # 撞到了左边墙
            self.xvelocity = -self.xvelocity
            # self.xvelocity *= -1
        if self.ypos + self.radius >= self.screen_height:
            # 撞了下边墙
            self.yvelocity = -self.yvelocity
            # self.yvelocity *= -1
        if self.ypos - self.radius <= 0:
            # 撞了上边墙
            self.yvelocity = -self.yvelocity
            # self.yvelocity *= -1

        # 在画布上挪动图画
        self.cavas.move(self.item, self.xvelocity, self.yvelocity)


class ScreenSaver:
    """
    定义屏保的类
    可以被启动
    """
    # 如何装随机产生的球？
    balls = list()

    def __init__(self):
        # 每次启动球的数量随机
        self.num_balls = random.randint(6, 10)

        self.root = tkinter.Tk()
        # 取消边框
        self.root.overrideredirect(1)

        # 任何鼠标移动都需要取消
        self.root.bind("<Motion>", self.myquit)
        # 同理，按动任何键盘都需要退出屏保 todo

        # 得到屏幕大小规格
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        # 创建画布，包括画布的归属，规格
        self.canvas = tkinter.Canvas(self.root, width=w, heigh=h)
        self.canvas.pack()

        # 在画布上画球
        for i in range(self.num_balls):
            ball = RandomBall(self.canvas, screen_width=2, screen_height=h)
            ball.create_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()

        # after是200毫秒后启动一个函数，需要启动的函数是第二个参数
        self.canvas.after(200, self.run_screen_saver())

    def myquit(self, e):
        # 此处只是利用了事件处理机制
        # 实际上并不关心事件的类型
        # 作业：次屏保扩展成，一旦捕获实践，则判断屏保不退出
        # 系那是一个Button，Button上显示事件类型，点击Button实现屏保退出
        self.root.destroy()


ss = ScreenSaver()
