"""
Module to handle with tasks persistence
"""

from pathlib import Path
import json


class TaskRegisters:
    """
    Class to persist tasks
    """

    FILE_PATH = "/usr/local/share/task-management/data/tasks.json"
    FILE_FINISHED_TASKS_PATH = "/usr/local/share/task-management/data/finished.json"

    def __init__(self) -> None:
        self.tasks = self.load_data()

    def add(self, task: str):
        """
        Method to persist a task

        Args:
            task (str): that should be persisted
        """
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

    def remove(self, task: str):
        """
        Method to remove task already persisted

        Args:
            task (str): should be removed
        """
        with open(TaskRegisters.FILE_PATH, "r", encoding="utf-8") as file:
            file_data = json.load(file)

        if not isinstance(file_data, list):
            file_data = [file_data]

        file_data.remove(task)

        with open(TaskRegisters.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(file_data, file, indent=4, ensure_ascii=False)

    def finishe(self, task: str):
        """
        Method to set a task as completed

        Args:
            task (str): completed
        """
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
        """
        Method to load register tasks
        """
        try:
            if Path(TaskRegisters.FILE_PATH).exists():
                with open(TaskRegisters.FILE_PATH, encoding="utf-8") as file:
                    data = json.load(file)

                    if not isinstance(data, list):
                        data = [data]
            else:
                data = []

            return data
        except FileNotFoundError:
            return []
