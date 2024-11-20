"""
Module contain customized input text widget
"""

from PySide6.QtWidgets import QLineEdit


class InputTextWidget(QLineEdit):
    """
    Customized input widget
    """

    def __init__(self):
        super().__init__()

        self.setPlaceholderText("Task title")
        self.returnPressed.connect(self.enter)

    def enter(self):
        """
        Method called when user press enter inside input task
        """
        print("Return pressed", self.text())
