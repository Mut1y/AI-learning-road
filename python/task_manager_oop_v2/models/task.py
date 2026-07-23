class Task:


    def __init__(self, title):

        self.title = title

        self.completed = False



    def complete(self):

        self.completed = True



    def show(self):

        status = "完成" if self.completed else "未完成"

        print(self.title, "-", status)