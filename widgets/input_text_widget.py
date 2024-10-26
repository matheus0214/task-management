import tkinter as tk

class InputTextWidget:
    def __init__(self, root) -> None:
        self.root = root

    def draw(self):
        component = tk.Text(self.root, height=5, font=("Arial", 14), padx=10, pady=10)
        component.pack()

        return component
