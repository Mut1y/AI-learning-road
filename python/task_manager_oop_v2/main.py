from services.task_manager import TaskManager

from storage.json_storage import JsonStorage



storage = JsonStorage(
    "data/tasks.json"
)


manager = TaskManager(storage)



while True:

    print("==========任务管理器==========")

    print("1. 查看任务")

    print("2. 添加任务")

    print("3. 删除任务")

    print("4. 完成任务")

    print("5. 退出")


    choice = input("请选择：")



    if choice == "1":

        manager.show_tasks()



    elif choice == "2":

        title = input("请输入任务：")

        manager.add_task(title)



    elif choice == "3":

        try:

            index = int(
                input("请输入删除编号：")
            )

            manager.delete_task(index)


        except ValueError:

            print("请输入数字")

    elif choice == "4":

        index = int(input("请输入完成任务编号："))

        manager.complete_task(index)

    elif choice == "5":

        print("程序退出")

        break



    else:

        print("请输入正确选项")