import tkinter as tk

WIDTH, HEIGHT = 600, 600

root = tk.Tk()
root.title("Task management")
root.minsize(width=WIDTH, height=HEIGHT)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

input_label = tk.Text(frame, height=5, font=("Arial", 14), padx=10, pady=10)
input_label.pack()

root.mainloop()
