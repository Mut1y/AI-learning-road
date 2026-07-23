import storage

import task


tasks = storage.load_tasks()


while True:

    print("==========任务管理器==========")
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 删除任务")
    print("4. 退出")


    choice = input("请选择：")


    if choice == "1":

        task.show_tasks(tasks)


    elif choice == "2":

        new_task = input("请输入新任务：")

        task.add_task(tasks, new_task)

        storage.save_tasks(tasks)


    elif choice == "3":

        try:

            index = int(input("请输入删除任务编号："))

            result = task.delete_task(tasks, index)


            if result:

                storage.save_tasks(tasks)


        except ValueError:

            print("请输入数字")


    elif choice == "4":

        print("程序退出")

        break


    else:

        print("请输入正确选项")