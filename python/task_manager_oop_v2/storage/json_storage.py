import json
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)


DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)


os.makedirs(DATA_DIR, exist_ok=True)


FILE_PATH = os.path.join(
    DATA_DIR,
    "tasks.json"
)


class JsonStorage:


    def load(self):

        if not os.path.exists(FILE_PATH):

            return []

        with open(
            FILE_PATH,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)



    def save(self, tasks):

        data = []

        for task in tasks:

            data.append(
                {
                    "title": task.title,
                    "completed": task.completed
                }
            )


        with open(
            FILE_PATH,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )


        print(
            "保存路径:",
            FILE_PATH
        )