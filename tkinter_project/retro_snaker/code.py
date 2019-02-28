# Tkinter项目实战-贪吃蛇
# 项目分析：
#   构成：蛇 Snake；食物 food；世界 World
#   蛇和食物属于整个世界：
#           class World:
#                self.snake
#                self.food
#       上面不太友好，我们用另一个思路来分析
#   我们的分析思路：食物是一个独立的事物；蛇也可以认为是一个独立的事物；世界也是，但世界负责显示
import random
import threading
import time
from tkinter import *
import queue


class Food:
    """
    功能:1.出现在画面的某一个地方；2.一旦被吃，则增加蛇的分数
    """

    def __init__(self, queue):
        """
        自动产生一个食物
        """
        self.queue = queue
        self.new_foods()

    def new_foods(self):
        """
        功能：产生一个食物
        产生一个食物的过程就是随机产生一个食物坐标的过程
        :return:
        """
        # 注意横纵坐标产生的范围
        x = random.randrange(50, 480, 10)
        y = random.randrange(50, 280, 10)
        # 需要注意的是，我们的游戏屏幕一般不需要把他设置成正方形

        self.position = x, y  # position存放食物的位置

        # 队列，就是一个不能随意访问内部元素，只能从头弹出一个元素并只能从队尾追加元素的list
        # 把一个食物产生的消息放入队列
        # 消息的格式，自己定义
        # 我的定义是：消息是一个dict，k代表消息类型，v代表此类型的数据
        self.queue.put({"food": self.position})


class Snake(threading.Thread):
    """
    蛇的功能：1.蛇能动，由我们的上下左右按键控制
              2.蛇每次动，都需要重新计算蛇头的位置
              3.检测是否有事完事的功能
    """

    def __init__(self, world, queue):
        threading.Thread.__init__(self)

        self.world = world
        self.queue = queue
        self.point_earned = 0  # 游戏分数
        self.food = Food(self.queue)
        self.snake_points = [(490, 50), (480, 50), (470, 50), (460, 50)]
        self.direction = 'Left'  # 定义蛇开始向左边走
        self.start()

    def run(self):
        """
        一旦启用多线程调用此函数
        要求蛇一直都在跑
        :return:
        """
        if self.world.is_game_over:
            self._delete()
        while not self.world.is_game_over:
            self.queue.put({"move": self.snake_points})
            time.sleep(0.2)  # 控制蛇的速度
            self.move()

    def move(self):
        """
        负责蛇的移动：1.重新计算的蛇头的坐标
                      2.当蛇头跟实物相遇，则加分，重新生成食物，通知world，加分
                      3.否则，蛇头需要动
        :return:
        """
        new_snake_point = self.cal_new_pos()  # 重新计算蛇头位置

        # 蛇头位置跟食物位置相同
        if self.food.position == new_snake_point:
            self.point_earned += 1  # 得分加1
            self.queue.put({"points_earned": self.point_earned})
            self.snake_points.append(new_snake_point)
            self.food.new_foods()  # 食物被吃掉，产生新的食物
        else:
            # 需要注意蛇的信息的保存方式
            # 每次移动是删除存放蛇的最前位置，并在后面追加
            self.snake_points.pop(0)
            # 判断程序是否退出，因为新的蛇可能撞墙
            self.check_game_over(new_snake_point)
            self.snake_points.append(new_snake_point)

    def cal_new_pos(self):
        """
        计算新的 蛇头的位置
        :return:
        """
        last_x, last_y = self.snake_points[-1]
        if self.direction == "Up":  # direction负责存储蛇移动的方向
            new_snake_point = last_x, last_y - 10  # 每次移动的跨度是10像素
        elif self.direction == "Down":
            new_snake_point = last_x, last_y + 10
        elif self.direction == "Right":
            new_snake_point = last_x + 10, last_y
        elif self.direction == "Left":
            new_snake_point = last_x - 10, last_y
        return new_snake_point

    def key_pressed(self, e):
        # keysym是按键名称
        self.direction = e.keysym

    def check_game_over(self, snake_point):
        """
         判断的依据是蛇头是否墙相撞
        :param snake_point:
        :return:
        """
        # 把蛇头的坐标拿出来，跟墙的坐标进行判断
        x, y = snake_point[0], snake_point[1]
        if not -5 < x < 505 or not -5 < y < 315 or snake_point in self.snake_points:
            self.queue.put({"game_over": True})


class World(Tk):
    """
    用来模拟整个游戏画板
    """

    def __init__(self, queue):
        Tk.__init__(self)

        self.queue = queue
        self.is_game_over = False

        # 定义画板
        self.canvas = Canvas(self, width=500, height=300, bg="red", bd="1")
        self.canvas.pack()
        # 画出蛇和食物
        self.snake = self.canvas.create_line((10, 10), (20, 10), fill="black", width=10)
        self.food = self.canvas.create_rectangle(0, 0, 0, 0, fill="#FFCC4C", outline='#FFCC4C')

        self.points_earned = self.canvas.create_text(450, 20, fill='white', text='SCORE: 0', tags='point_earned')

        self.queue_handler()

    def queue_handler(self):
        try:
            # 需要不断从消息队列拿到消息，所以使用死循环
            while True:
                task = self.queue.get(block=False)

                if task.get("game_over"):
                    self.game_over()
                if task.get("move"):
                    points = [x for point in task['move'] for x in point]
                    # 重新绘制蛇
                    self.canvas.coords(self.snake, *points)
                if task.get("food"):
                    # 处理食物
                    self.canvas.coords(self.food, (task['food'][0] - 5, task['food'][1] - 5,
                                                   task['food'][0] + 5,
                                                   task['food'][1] + 5))
                if task.get("points_earned"):
                    # 处理得分
                    self.canvas.delete('point_earned')
                    self.canvas.create_text(450, 20, fill='white',
                                            text='SCORE: ' + str(task['points_earned']), tags='point_earned')
        except queue.Empty:  # 爆出队列为空异常
            if not self.is_game_over:
                # after的含义是，在多少毫秒后调用后面的函数
                self.canvas.after(10, self.queue_handler)

    def game_over(self):
        """
        游戏结束，清理现场
        :return:
        """
        self.is_game_over = True
        self.canvas.create_text(250, 150, text="Game over")
        qb = Button(self, text="Quit", command=self.destroy, relief='raised', width=8, height=2)
        qb.pack(fill='x', anchor='center')
        rb = Button(self, text="Again", command=lambda: Start(self), relief='raised', width=8, height=2)
        rb.pack(fill='x', anchor='center')


class Start:
    def __init__(self, world):
        if world != "":
            world.destroy()
        q = queue.Queue()
        world = World(q)

        snake = Snake(world, q)
        world.bind("<Key-Left>", snake.key_pressed)
        world.bind("<Key-Right>", snake.key_pressed)
        world.bind("<Key-Up>", snake.key_pressed)
        world.bind("<Key-Down>", snake.key_pressed)

        world.mainloop()


Start('')
