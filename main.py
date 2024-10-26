import tkinter as tk

from actions.register_button_action import ButtonAction
from tasks.registers import TaskRegisters
from widgets.input_text_widget import InputTextWidget
from widgets.register_button_widget import RegisterButtonWidget
from widgets.tasks_list_widget import TasksListWidget

WIDTH, HEIGHT = 600, 600


root = tk.Tk()
root.title("Task management")
root.minsize(width=WIDTH, height=HEIGHT)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

input_label = InputTextWidget(frame).draw()
task_register = TaskRegisters()
tasks_list = TasksListWidget(frame)

button_action = ButtonAction(task_register, tasks_list)

register_button_wg = RegisterButtonWidget(frame, input_label, button_action).draw()


root.mainloop()
