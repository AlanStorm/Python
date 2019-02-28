# Tkinter-计算器
# 模拟系统的计算器功能
# 实现一个简单的具有加减法等操作的计算器
# 使用tkinter
# 操作步骤：画GUI；给每个控件配置相应的事件；写逻辑代码
#
import tkinter

"""
考虑以下几种情况：
1.按下数字
2.按下操作符号
3.只考虑两个操作数操作，不考虑复杂情况
"""
num1 = ''
num2 = ''
operator = ""


# 逻辑操作
def delete():
    print('我被删除了')


def clear():
    print('清空')


def fan():
    print('fan')


def ce():
    print('ce')


def change(num):
    """
    按下一个数字需要考虑两种情况
    1.数字属于第一个操作数
    2.数组属于第二个操作数
    3.判断是否属于第一个操作数，可以通过operator判断
    :param num:
    :return:
    """
    global num1
    global num2
    # 加入操作数是None，表明肯定是第一个操作数
    if not operator:
        num1 = num1 + num
        # 如果是第一个操作数，则直系那是第一个操作数
        sv.set(num1)
    else:
        num2 = num2 + num
        sv.set(num1 + operator + num2)


def symbol(symbol):
    global operator
    if symbol in ['+', '-', '*', '/']:
        operator = symbol
        sv.set(num1 + operator)
    else:  # 认为是按下的等于号
        if operator == '=':
            rst = int(num1) + int(num2)
        if operator == '-':
            rst = int(num1) - int(num2)
        if operator == '*':
            rst = int(num1) * int(num2)
        if operator == '/':
            rst = int(num1) / int(num2)
        sv.set(int(rst))


def spot(spot):
    print(spot)


root = tkinter.Tk()
# 定义面板的大小
root.geometry('250x380')
root.title('计算器')

# 定义面板
# bg代表背景颜色（background）
frame_show = tkinter.Frame(width=400, height=150, bg='#dddddd')
frame_show.pack()

# 定义顶部区域
sv = tkinter.StringVar()
sv.set('0')

# anchor：定义控件的锚点，e代表右边
# font代表字体
show_label = tkinter.Label(frame_show, textvariable=sv, bg='white',
                           width=12, height=1, font=("黑体", 20, 'bold'),
                           justify='left', anchor='e')
show_label.pack(padx=10, pady=10)

# 定义图形下半部分（按键区域）
frame_bord = tkinter.Frame(width=400, height=350, bg='#cccccc')
frame_bord.pack()

button_del = tkinter.Button(frame_bord, text="←", width=5, height=1,
                            command=delete).grid(row=0, column=0)
button_clear = tkinter.Button(frame_bord, text='C', width=5, height=1,
                              command=clear).grid(row=0, column=1)
button_fan = tkinter.Button(frame_bord, text='±', width=5, height=1,
                            command=fan).grid(row=0, column=2)
button_ce = tkinter.Button(frame_bord, text='CE', width=5, height=1,
                           command=clear).grid(row=0, column=3)

button_1 = tkinter.Button(frame_bord, text='1', width=5, height=2,
                          command=lambda: change("1")).grid(row=1, column=0)
button_2 = tkinter.Button(frame_bord, text='2', width=5, height=2,
                          command=lambda: change("2")).grid(row=1, column=1)
button_3 = tkinter.Button(frame_bord, text='3', width=5, height=2,
                          command=lambda: change("3")).grid(row=1, column=2)
button_except = tkinter.Button(frame_bord, text='/', width=5, height=2,
                               command=lambda: symbol("/")).grid(row=1, column=3)

button_4 = tkinter.Button(frame_bord, text='4', width=5, height=2,
                          command=lambda: change("4")).grid(row=2, column=0)
button_5 = tkinter.Button(frame_bord, text='5', width=5, height=2,
                          command=lambda: change("5")).grid(row=2, column=1)
button_6 = tkinter.Button(frame_bord, text='6', width=5, height=2,
                          command=lambda: change("6")).grid(row=2, column=2)
button_ride = tkinter.Button(frame_bord, text='*', width=5, height=2,
                             command=lambda: symbol("*")).grid(row=2, column=3)

button_7 = tkinter.Button(frame_bord, text='7', width=5, height=2,
                          command=lambda: change("7")).grid(row=3, column=0)
button_8 = tkinter.Button(frame_bord, text='8', width=5, height=2,
                          command=lambda: change("8")).grid(row=3, column=1)
button_9 = tkinter.Button(frame_bord, text='9', width=5, height=2,
                          command=lambda: change("9")).grid(row=3, column=2)
button_reduce = tkinter.Button(frame_bord, text='-', width=5, height=2,
                               command=lambda: symbol("-")).grid(row=3, column=3)

button_0 = tkinter.Button(frame_bord, text='0', width=12, height=2,
                          command=lambda: change("0")).grid(row=4, column=0, columnspan=2)
button_spot = tkinter.Button(frame_bord, text='.', width=5, height=2,
                             command=lambda: spot(".")).grid(row=4, column=2)
button_plus = tkinter.Button(frame_bord, text='+', width=5, height=2,
                             command=lambda: symbol("+")).grid(row=4, column=3)

button_equal = tkinter.Button(frame_bord, text='=', width=25, height=2,
                              command=lambda: symbol("=")).grid(row=5, column=0, columnspan=4)

root.mainloop()
