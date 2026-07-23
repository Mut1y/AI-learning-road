import json


def load_tasks():

    try:

        file = open("tasks.json", "r", encoding="utf-8")

        tasks = json.load(file)

        file.close()

        return tasks


    except FileNotFoundError:

        return []


def save_tasks(tasks):

    file = open("tasks.json", "w", encoding="utf-8")

    json.dump(tasks, file, ensure_ascii=False)

    file.close()