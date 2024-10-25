import tkinter as tk

from actions.register_button import ButtonAction
from widgets.input_text import InputText

WIDTH, HEIGHT = 600, 600

button_action = ButtonAction()

root = tk.Tk()
root.title("Task management")
root.minsize(width=WIDTH, height=HEIGHT)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

input_label = InputText(frame).draw()

button_register = tk.Button(frame, text="Register",
                            command=lambda: button_action.register(input_label))
button_register.pack(pady=10)

root.mainloop()
