import tkinter as tk

class TasksListWidget:
    def __init__(self, root, task_register) -> None:
        self.root = root
        self.task_register = task_register

        if len(task_register.tasks) > 0:
            for item in task_register.tasks:
                self.draw(item)

    def draw(self, task):
        frame = tk.Frame(self.root)

        label = tk.Label(frame, text=task, font=("Courier", 14))
        label.pack(side="left", padx=12)

        button = tk.Button(frame, text="Finishe", command=lambda:
                           self.finishe_task(task, frame))
        button.pack()

        frame.pack()

    def finishe_task(self, task, frame):
        self.task_register.finishe(task)
        frame.destroy()


