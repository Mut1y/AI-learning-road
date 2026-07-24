from utils.logger import logger

from models.task import Task


class TaskManager:


    def __init__(self, storage):

        self.storage = storage

        self.tasks = []

        self.load_tasks()



    def add_task(self, title):

        task = Task(title)

        self.tasks.append(task)

        self.storage.save(self.tasks)

        logger.info(f"添加任务: {title}")

        print("添加成功")



    def show_tasks(self):

        print("当前任务:")

        for index, task in enumerate(self.tasks):

            status = "已完成" if task.completed else "未完成"

            print(
                index,
                task.title,
                "-",
                status
        )

    def load_tasks(self):

        data = self.storage.load()

        logger.info(f"加载任务数量: {len(data)}")


        for item in data:

            task = Task(item["title"])

            task.completed = item["completed"]

            self.tasks.append(task)

    def delete_task(self, index):

        if index >= 0 and index < len(self.tasks):

            removed_task = self.tasks.pop(index)

            self.storage.save(self.tasks)

            logger.info(
                f"删除任务: {removed_task.title}"
        )

            print(
                "删除成功：",
                removed_task.title
        )

        else:

            logger.warning(
                f"删除失败，不存在任务编号: {index}"
        )

            print("任务不存在")

    def complete_task(self, index):

        if index >= 0 and index < len(self.tasks):

            self.tasks[index].complete()

            self.storage.save(self.tasks)

            logger.info(
                f"完成任务: {self.tasks[index].title}"
        )

            print("任务完成")

        else:

            logger.warning(
                f"完成任务失败，不存在编号: {index}"
        )

            print("任务编号不存在")