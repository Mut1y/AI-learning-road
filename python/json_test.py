import json

tasks = [
    "学习Python",
    "完成AI项目",
    "提交GitHub"
]

file = open("tasks.json", "w", encoding="utf-8")

json.dump(tasks, file, ensure_ascii=False)

file.close()