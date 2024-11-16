from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget

from constants.core import WINDOW_MIN_HEIGHT, WINDOW_MIN_WIDTH
from data.register import TaskRegisters
from ui.input_text_widget import InputTextWidget
from ui.task_widget import TaskWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Management")
        self.setMinimumWidth(WINDOW_MIN_WIDTH)
        self.setMinimumHeight(WINDOW_MIN_HEIGHT)
        
        main_layout = QVBoxLayout()
        layout_input_actions = QHBoxLayout()
        layout_input_actions_widget = QWidget()

        layout_input_actions_widget.setLayout(layout_input_actions)
        layout_input_actions_widget.setSizePolicy(
            layout_input_actions_widget.sizePolicy().horizontalPolicy(),
            layout_input_actions_widget.sizePolicy().Policy.Minimum
        )
                
        layout_tasks = QVBoxLayout()
        layout_tasks.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout_tasks_widget = QWidget()
        layout_tasks_widget.setLayout(layout_tasks)

        btn = QPushButton("Register")
        btn.pressed.connect(self.register_button_clicked)

        self.input_text_widget = InputTextWidget()

        layout_input_actions.addWidget(self.input_text_widget)
        layout_input_actions.addWidget(btn)

        layout_input_actions_widget.setMaximumHeight(
            layout_input_actions.sizeHint().height()
        )

        task_register = TaskRegisters()

        for item in task_register.tasks:
            label = TaskWidget(item)
            layout_tasks.addWidget(label)

        main_layout.addWidget(layout_input_actions_widget)
        main_layout.addWidget(layout_tasks_widget) 

        widget = QWidget()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)

        main_layout.setAlignment(layout_input_actions, Qt.AlignmentFlag.AlignTop)
        main_layout.setAlignment(layout_tasks, Qt.AlignmentFlag.AlignTop)

    def register_button_clicked(self):
        print("Click", self.input_text_widget.text())

