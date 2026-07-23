def show_tasks(tasks):

    print("当前任务：")

    for index, task in enumerate(tasks):

        print(index, task)



def add_task(tasks, task):

    tasks.append(task)

    print("添加成功")



def delete_task(tasks, index):

    if index >= 0 and index < len(tasks):

        removed_task = tasks.pop(index)

        print("删除成功：", removed_task)

        return True


    else:

        print("任务编号不存在")

        return False