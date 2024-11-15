from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QMainWindow, QPushButton, QWidget

from constants.core import WINDOW_MIN_HEIGHT, WINDOW_MIN_WIDTH
from ui.input_text_widget import InputTextWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Management")
        self.setMinimumWidth(WINDOW_MIN_WIDTH)
        self.setMinimumHeight(WINDOW_MIN_HEIGHT)
        
        main_layout = QGridLayout()
        layout_input_actions = QHBoxLayout()
        btn = QPushButton("Register")

        input_text_widget = InputTextWidget()

        layout_input_actions.addWidget(input_text_widget)
        layout_input_actions.addWidget(btn)

        main_layout.addLayout(layout_input_actions, 0, 0)

        widget = QWidget()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)

        main_layout.setAlignment(layout_input_actions, Qt.AlignmentFlag.AlignTop)
