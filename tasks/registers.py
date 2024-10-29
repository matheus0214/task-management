class TaskRegisters:
    def __init__(self) -> None:
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def remove(self, task):
        self.tasks.remove(task)
