import json

file = open("tasks.json", "r", encoding="utf-8")

tasks = json.load(file)

print(tasks)

print(type(tasks))

file.close()