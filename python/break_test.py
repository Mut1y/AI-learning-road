expected_password = input("请先设置练习密码：")

while True:
    password = input("请输入密码： ")

    if password == expected_password:
        print("登录成功")
        break

    else:
        print("密码错误，请重新输入")
