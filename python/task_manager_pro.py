tasks = []

def show_menu():
    print("====任务管理器Pro====")
    print("1.查看任务")
    print("2.添加任务")
    print("3.完成任务")
    print("4.删除任务")
    print("5.退出")

def show_tasks():
    if len(tasks) == 0:
        print("暂无任务")

    else:
        for task in tasks:
            print(task)

def add_task():
    name = input("请输入任务： ")

    task = {
        "name": name,
        "status": "未完成"
    }

    tasks.append(task)

    print("添加成功")

def complete_task():
    name = input("请输入完成的任务： ")

    for task in tasks:

        if task["name"] == name:

            task["status"] = "已完成"

            print("完成成功")
            return

    print("没有找到这个任务")

def delete_task():
    name = input("请输入删除的任务： ")

    for task in tasks:

        if task["name"] == name:

            tasks.remove(task)

            print("删除成功")
            return

    print("没有找到这个任务")

while True:

    show_menu()

    choice = input("请选择： ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("程序结束")
        break