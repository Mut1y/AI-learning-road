import json


class JsonStorage:


    def __init__(self, filename):

        self.filename = filename



    def save(self, tasks):

        data = []


        for task in tasks:

            data.append(
                {
                    "title": task.title,
                    "completed": task.completed
                }
            )
        print("保存路径:", self.filename)


        file = open(
            self.filename,
            "w",
            encoding="utf-8"
        )


        json.dump(
            data,
            file,
            ensure_ascii=False
        )


        file.close()



    def load(self):

        try:
            print("读取路径:", self.filename)
            file = open(
                self.filename,
                "r",
                encoding="utf-8"
            )


            data = json.load(file)


            file.close()


            return data


        except FileNotFoundError:

            return []