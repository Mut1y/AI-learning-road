users = []

def show_menu():
    print("====用户管理器====")
    print("1.查看用户")
    print("2.添加用户")
    print("3.修改年龄")
    print("4.删除用户")
    print("5.退出")

def show_users():
    if len(users) == 0:
        print("暂无用户")

    else:
        for user in users:
            print(user)

def add_user():
    name = input("请输入姓名： ")
    age = int(input("请输入年龄： "))

    user = {
        "name": name,
        "age": age
    }

    users.append(user)

    print("添加成功")

def update_user():
    name = input("请输入修改的用户名： ")

    for user in users:

        if user["name"] == name:

            age = int(input("请输入新的年龄： "))

            user["age"] = age

            print("修改成功")
            return

    print("没有找到这个用户")

def delete_user():
    name = input("请输入删除的用户名： ")

    for user in users:

        if user["name"] == name:
            users.remove(user)

            print("删除成功")
            return

    print("没有找到这个用户")

while True:

    show_menu()

    choice = input("请选择： ")

    if choice == "1":
        show_users()

    elif choice == "2":
        add_user()

    elif choice == "3":
        update_user()

    elif choice == "4":
        delete_user()

    elif choice == "5":
        print("程序结束")
        break