import random

secret = random.randint(1, 7)
while True:
    guess = int(input("请输入你需要猜的数:"))
    if guess > secret:
        print("大了")
    elif guess < secret:
        print("小了")
    else:
        print("恭喜你猜对了")
        break



