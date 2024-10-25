import tkinter as tk

from widgets.input_text import InputText
from widgets.register_button import RegisterButton

WIDTH, HEIGHT = 600, 600


root = tk.Tk()
root.title("Task management")
root.minsize(width=WIDTH, height=HEIGHT)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

input_label = InputText(frame).draw()
register_button_wg = RegisterButton(frame, input_label).draw()


root.mainloop()
