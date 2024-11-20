"""
This module is to handle with the main application window
"""

from os import path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from constants.core import WINDOW_MIN_HEIGHT, WINDOW_MIN_WIDTH
from data.register import TaskRegisters
from ui.input_task_widget import InputTaskWidget
from ui.input_text_widget import InputTextWidget
from ui.task_widget import TaskWidget


class MainWindow(QMainWindow):
    """
    Main app window
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Management")
        self.setMinimumWidth(WINDOW_MIN_WIDTH)
        self.setMinimumHeight(WINDOW_MIN_HEIGHT)

        main_layout = QVBoxLayout()
        layout_input_actions = QHBoxLayout()

        self.layout_tasks = QVBoxLayout()
        self.layout_tasks.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout_tasks_widget = QWidget()
        layout_tasks_widget.setLayout(self.layout_tasks)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        with open(
            path.join(path.dirname(__file__), "css/scroll-area.qss"), encoding="utf-8"
        ) as f:
            scroll_area.setStyleSheet(f.read())
        scroll_area.setWidget(layout_tasks_widget)

        btn = QPushButton("Register")
        btn.pressed.connect(self.register_button_clicked)

        self.input_text_widget = InputTextWidget()

        layout_input_actions.addWidget(self.input_text_widget)
        layout_input_actions.addWidget(btn)

        input_actions_widget = InputTaskWidget(layout_input_actions)

        self.task_register = TaskRegisters()

        self.show_task_list()

        main_layout.addWidget(input_actions_widget)
        main_layout.addWidget(scroll_area)

        widget = QWidget()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)

        main_layout.setAlignment(layout_input_actions, Qt.AlignmentFlag.AlignTop)
        main_layout.setAlignment(self.layout_tasks, Qt.AlignmentFlag.AlignTop)

    def register_button_clicked(self):
        """
        Handle the event when the button 'Register' is clicked
        """
        task = self.input_text_widget.text()
        self.task_register.add(task)

        self.input_text_widget.clear()
        self.draw_task(task)

    def show_task_list(self):
        """
        Draw all tasks in the screen
        """
        for item in self.task_register.tasks:
            self.draw_task(item)

    def draw_task(self, task: str):
        """
        Draw a single task

        Args:
            task (str): the task to be added
        """
        label = TaskWidget(task, self.task_register, self.remove_task)
        self.layout_tasks.addWidget(label)

    def remove_task(self, task: str):
        """
        Remove a task from the screen

        Args:
            task (str): the task to be removed
        """
        index = self.task_register.tasks.index(task)
        self.layout_tasks.takeAt(index).widget().deleteLater()
