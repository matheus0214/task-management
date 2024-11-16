from PySide6.QtWidgets import QLineEdit


class InputTextWidget(QLineEdit):
    def __init__(self):
        super().__init__()
         
        self.setPlaceholderText("Task title")
        
        self.returnPressed.connect(self.enter)

    def enter(self):
        print("Return pressed", self.text())
