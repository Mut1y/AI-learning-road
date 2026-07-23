import json

class TaskManager:


    def __init__(self):

        self.tasks=[]

        self.load()

    def load(self):

        try:

            file = open("tasks.json","r",encoding="utf-8")

            self.tasks = json.load(file)

            file.close()


        except FileNotFoundError:

            self.tasks=[]

    def save(self):

        file=open("tasks.json","w",encoding="utf-8")

        json.dump(self.tasks,file,ensure_ascii=False)

        file.close()

    def show_tasks(self):

        print("当前任务:")

        for index, task in enumerate(self.tasks):

            print(index, task)


    def add_task(self, task):

        self.tasks.append(task)

        self.save()

        print("添加成功")

    def delete_task(self, index):

        if index >= 0 and index < len(self.tasks):

            removed_task = self.tasks.pop(index)

            self.save()

            print("删除成功：", removed_task)

        else:

            print("任务编号不存在")