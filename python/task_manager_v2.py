tasks = []

def show_menu():
    print("====任务管理器====")
    print("1.查看任务")
    print("2.添加任务")
    print("3.删除任务")
    print("4.退出")

def show_tasks():
    if len(tasks) == 0:
        print("暂无任务")

    else:
        for task in tasks:
            print(task)

def add_task():
    task = input("请输入任务： ")

    tasks.append(task)

    print("添加成功")

def delete_task():
    task = input("请输入删除的任务： ")

    if task in tasks:
        tasks.remove(task)
        print("删除成功")

    else:
        print("没有找到这个任务")

while True:

    show_menu()

    choice = input("请选择： ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("程序结束")
        break