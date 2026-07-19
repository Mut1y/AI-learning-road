tasks = []

while True:
    print("====任务管理器====")
    print("1.查看任务")
    print("2.添加任务")
    print("3.删除任务")
    print("4.退出")

    choice = input("请选择： ")

    if choice == "1":
        for task in tasks:
            print(task)

    elif choice == "2":
        task = input("请输入新任务： ")
        tasks.append(task)
        print("添加成功")

    elif choice == "3":
        task = input("请输入删除的任务： ")
        tasks.remove(task)
        print("删除成功")

    elif choice == "4":
        print("程序结束")
        break           