# v2
# 小蜜蜂会动，从上往下慢慢的飞
# 能控制小蜜蜂左右移动
# 入场算法：y轴要求是负数，这样会形成吗那么入场的效果，y = 0 - bee.height
#           x轴要求是有一定的富余，即要求蜜蜂等移动物品不能贴边，基本上
#               x轴的值应该是50+bee.width起，最右边的计算方式是world.width-bee.width-50
# 移动速度问题：包含x，y两个值；对于绝大多数物体，则只考虑y值；但是，蜜蜂和影响是特例
#               蜜蜂是从上向下移动的同时具有横向移动；英雄的移动由上下左右键盘控制
#               速度应该是一个tuple=（x，y）
# 方向问题：具体移动方向有x，y控制；值只能是-1,0,1三个就好；应该是一个tuple；
#           例如（-1,0）表示水平向左移动，（0，1）表示向下垂直移动
import tkinter
import time
import random as rd

"""
蜜蜂从上向下运动
可以通过键盘左右控制
"""
step = 0
direction = (1, 1)
x = 0
y = 10


def set_right(e):
    global x
    x += 20


def set_left(e):
    global x
    x -= 20


root_window = tkinter.Tk()
root_window.title("飞机大战")
root_window.resizable(width=False, height=False)

root_window.bind('<Key-Left>', set_left)
root_window.bind('<Key-Right>', set_right)

# 创建画布
window_canvas = tkinter.Canvas(root_window, width=480, height=600)
window_canvas.pack()


def main():
    # 背景图片
    bg_img_name = "../img/background.gif"
    start_img = tkinter.PhotoImage(file=bg_img_name)
    # tags的作用是，以后我么使用创建的image可以通过tags使用
    window_canvas.create_image(240, 300, anchor=tkinter.CENTER, image=start_img,
                               tags="start")

    sp = "../img/smallplane.gif"
    sp_img = tkinter.PhotoImage(file=sp)
    window_canvas.create_image(50, 20, anchor=tkinter.CENTER, image=sp_img,
                               tags="sp")
    # 让小飞机动起来
    ap_move()
    tkinter.mainloop()


def ap_move():
    global step
    global x
    global y

    y += 20
    print(x, y)
    window_canvas.move("sp", x, y)

    step += 1
    window_canvas.after(500, ap_move)


if __name__ == '__main__':
    main()
