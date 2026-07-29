import json
import os


MEMORY_FILE = "memory.json"



def load_memory():

    if not os.path.exists(MEMORY_FILE):

        return []


    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def save_memory(history):

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            history,
            file,
            ensure_ascii=False,
            indent=4
        )