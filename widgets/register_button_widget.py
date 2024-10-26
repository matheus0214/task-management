import tkinter as tk

class RegisterButtonWidget:
    def __init__(self, root, input_label, button_action) -> None:
        self.root = root
        self.input_label = input_label
        self.button_action = button_action

    def draw(self):
        register_button = tk.Button(self.root, text="Register", command=lambda :
                                   self.button_action.register(self.input_label))
        register_button.pack(pady=10)

        return register_button
