import json

try:

    file = open("tasks.json", "r", encoding="utf-8")

    tasks = json.load(file)

    file.close()

except FileNotFoundError:

    tasks = []

    file = open("tasks.json", "w", encoding="utf-8")

    json.dump(tasks, file, ensure_ascii=False)

    file.close()

while True:

    print("==========任务管理器==========")
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 删除任务")
    print("4. 退出")

    choice = input("请选择：")

    if choice == "1":

        print("当前任务：")

        for index, task in enumerate(tasks):
            print(index, task)

    elif choice == "2":

        task = input("请输入新任务：")

        tasks.append(task)


        file = open("tasks.json", "w", encoding="utf-8")

        json.dump(tasks, file, ensure_ascii=False)

        file.close()


        print("添加成功")

    elif choice == "3":

        try:

            index = int(input("请输入删除任务编号："))


        except ValueError:

            print("请输入数字")

            continue


        if index >= 0 and index < len(tasks):

            removed_task = tasks.pop(index)

            file = open("tasks.json", "w", encoding="utf-8")

            json.dump(tasks, file, ensure_ascii=False)

            file.close()

            print("删除成功：", removed_task)

        else:

            print("任务编号不存在")

    elif choice == "4":

        print("程序退出")

        break

    else:
        
        print("请输入正确选项")