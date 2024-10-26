import tkinter as tk

class TasksListWidget:
    def __init__(self, root) -> None:
        self.root = root
        self.labels = []

    def draw(self, task):
        l = tk.Label(self.root, text=task, font=("Courier", 14))
        l.pack()


