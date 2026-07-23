try:

    file = open("test.txt", "r")

    print(file.read())


except FileNotFoundError:

    print("文件不存在")


finally:

    print("程序结束")