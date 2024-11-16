from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget

from constants.core import WINDOW_MIN_HEIGHT, WINDOW_MIN_WIDTH
from ui.input_text_widget import InputTextWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Management")
        self.setMinimumWidth(WINDOW_MIN_WIDTH)
        self.setMinimumHeight(WINDOW_MIN_HEIGHT)
        
        main_layout = QVBoxLayout()
        layout_input_actions = QHBoxLayout()
        btn = QPushButton("Register")
        btn.pressed.connect(self.register_button_clicked)

        self.input_text_widget = InputTextWidget()

        layout_input_actions.addWidget(self.input_text_widget)
        layout_input_actions.addWidget(btn)

        main_layout.addLayout(layout_input_actions)

        widget = QWidget()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)

        main_layout.setAlignment(layout_input_actions, Qt.AlignmentFlag.AlignTop)

    def register_button_clicked(self):
        print("Click", self.input_text_widget.text())

