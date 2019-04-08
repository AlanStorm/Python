def SayHello(name):
    print("T want to say hello with you,{0}".format(name))
    print("Hello,{0}".format(name))
    print("Done...")


if __name__ == "__main__":
    print("***" * 10)
    name = input('Please input your name:')
    print(SayHello(name))
    print("***" * 10)
