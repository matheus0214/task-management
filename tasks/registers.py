from pathlib import Path
import json

class TaskRegisters:
    FILE_PATH = "/usr/local/share/task-management/data/tasks.json"
    FILE_FINISHED_TASKS_PATH = "/usr/local/share/task-management/data/finished.json"

    def __init__(self) -> None:
        self.tasks = self.load_data()

    def add(self, task):
        try:
            if Path(TaskRegisters.FILE_PATH).exists():
                with open(TaskRegisters.FILE_PATH, "r", encoding="utf-8") as file:
                    file_data = json.load(file)
            else:
                file_data = []

            if not isinstance(file_data, list):
                file_data = [file_data]

            file_data.append(task)

            with open(TaskRegisters.FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(file_data, file, indent=4, ensure_ascii=False)

        except FileNotFoundError as e:
            print(f"Erro to write in file {e}")

    def remove(self, task):
        with open(TaskRegisters.FILE_PATH, "r", encoding="utf-8") as file:
            file_data = json.load(file)

        if not isinstance(file_data, list):
            file_data = [file_data]

        file_data.remove(task)

        with open(TaskRegisters.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(file_data, file, indent=4, ensure_ascii=False)

    def finishe(self, task):
        try:
            if Path(TaskRegisters.FILE_FINISHED_TASKS_PATH).exists():
                with open(
                    TaskRegisters.FILE_FINISHED_TASKS_PATH, "r", encoding="utf-8"
                ) as file:
                    file_data = json.load(file)
            else:
                file_data = []

            if not isinstance(file_data, list):
                file_data = [file_data]

            file_data.append(task)

            with open(
                TaskRegisters.FILE_FINISHED_TASKS_PATH, "w", encoding="utf-8"
            ) as file:
                json.dump(file_data, file, indent=4, ensure_ascii=False)
                
            self.remove(task)
        except FileNotFoundError:
            print("File not found")

    def load_data(self):
        try:
            if Path(TaskRegisters.FILE_PATH).exists():
                with open(TaskRegisters.FILE_PATH) as file:
                    data = json.load(file)

                    if not isinstance(data, list):
                        data = [data]
            else:
                data = []

            return data
        except:
            return []
