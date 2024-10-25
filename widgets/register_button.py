import tkinter as tk

from actions.register_button import ButtonAction

class RegisterButton:
    def __init__(self, root, input_label) -> None:
        self.root = root
        self.input_label = input_label

    def draw(self):
        button_action = ButtonAction()
        register_button = tk.Button(self.root, text="Register", command=lambda :
                                   button_action.register(self.input_label))
        register_button.pack(pady=10)

        return register_button
