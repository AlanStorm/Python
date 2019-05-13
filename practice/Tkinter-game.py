# # 用thinter写一个小游戏，来随机生成我们需要的名字
#
# import tkinter
# import random
#
# window = tkinter.Tk()
#
#
# def random_1():
#     s1 = ['cats', 'hippos', 'cakes']
#     s = random.choice(s1)
#     return s
#
#
# def random_2():
#     s2 = ['eats', 'likes', 'hates', 'has']
#     s = random.choice(s2)
#     return s
#
#
# def button_click():
#     name = nameEntry.get()
#     verb = random_1()
#     noun = random_2()
#     sentence = name + "" + verb + "" + noun
#     result.delete(0, tkinter.END)
#     result.insert(0, sentence)
#
#
# nameLabel = tkinter.Label(window, text="Name:")
# nameEntry = tkinter.Entry(window)
# button = tkinter.Button(window, text='生成随机名称', command=button_click)
# result = tkinter.Entry(window)
#
# nameLabel.pack()
# nameEntry.pack()
# button.pack()
# result.pack()
#
# window.mainloop()
#
#
# # 是一个输入密码的小程序，我们自己设定一个密码，如果用户输入正确则显示 正确，否则，显示不正确
# import tkinter
#
# window = tkinter.Tk()
#
#
# def check_password():
#     password = '123456'
#     entered_password = passwordEntry.get()
#     if password == entered_password:
#         confirmLabel.config(text='正确')
#     else:
#         confirmLabel.config(text="不正确")
#
#
# passwordLabel = tkinter.Label(text='Password：')
# passwordEntry = tkinter.Entry(window, show="*")
# button = tkinter.Button(window, text="校验", command=check_password)
# confirmLabel = tkinter.Label(window)
#
# passwordLabel.pack()
# passwordEntry.pack()
# button.pack()
# confirmLabel.pack()
#
# window.mainloop()
#
#
# 一个猜数字的小游戏，让计算机随机生成一个整数，用户输入去猜这个整数，如果用户输入正确，
# 那么我们分数加1，并且显示计算机生成的数组，如果用户没有输入正确，那么我们的分数不变，还是
# 要显示计算机生成的数字
import random
import tkinter

window = tkinter.Tk()

maxNum = 10
score = 0
rounds = 0


def button_click():
    global score
    global rounds
    try:
        guess = int(guessBox.get())
        if 0 < guess <= maxNum:
            result = random.randrange(1, maxNum + 1)
            if guess == result:
                score += 1
            rounds += 1
        else:
            result = "输入不合法"
    except:
        result = "输入不合法"

    resultLabel.config(text=result)
    scoreLabel.config(text=str(score) + '/' + str(rounds))
    # guessBox.delete(0, tkinter.END)


guessBox = tkinter.Entry(window)
resultLabel = tkinter.Label(window)
scoreLabel = tkinter.Label(window)
guessLabel = tkinter.Label(window, text="请输入1到" + str(maxNum))
button = tkinter.Button(window, text="guess", command=button_click)

scoreLabel.pack()
resultLabel.pack()
guessBox.pack()
guessLabel.pack()
button.pack()

window.mainloop()
