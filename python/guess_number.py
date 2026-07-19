secret_number = 7

while True:
    guess = int(input("请输入你猜的数字： "))

    if guess == secret_number:
        print("猜对了！")
        break

    elif guess < secret_number:
        print("猜小了")

    else:
        print("猜大了")