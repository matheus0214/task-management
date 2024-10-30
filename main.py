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

frame_register_new = tk.Frame(frame)
frame_register_new.pack(fill="both")

canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill="both", expand=False)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

frame_list = tk.Frame(canvas)
frame_list.pack(fill="both")

canvas.create_window((90, 0), window=frame_list, anchor="nw")

input_label = InputTextWidget(frame_register_new).draw()
task_register = TaskRegisters()
tasks_list = TasksListWidget(frame_list, task_register)

button_action = ButtonAction(task_register, tasks_list)

register_button_wg = RegisterButtonWidget(frame_register_new, input_label, button_action).draw()

frame_list.bind("<Configure>", lambda _ :
                canvas.configure(scrollregion=canvas.bbox("all")))

root.mainloop()
