from PySide6.QtWidgets import QMainWindow

from constants.core import WINDOW_MIN_HEIGHT, WINDOW_MIN_WIDTH


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Management")
        self.setMinimumWidth(WINDOW_MIN_WIDTH)
        self.setMinimumHeight(WINDOW_MIN_HEIGHT)
