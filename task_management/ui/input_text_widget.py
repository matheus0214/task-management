"""Module contain customized input text widget."""

from PySide6.QtWidgets import QLineEdit


class InputTextWidget(QLineEdit):
    """Customized input widget."""

    def __init__(self):
        """Initialize a customized input text widget."""
        super().__init__()

        self.setPlaceholderText("Task title")
        self.returnPressed.connect(self.enter)

    def enter(self):
        """Event to get when user wants to register a new task."""
        print("Return pressed", self.text())
