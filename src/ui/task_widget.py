"""
Module contains the task widget to show in the main screen
"""

import os
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QWidget

from data.register import TaskRegisters


class TaskWidget(QWidget):
    """
    Task widget customized
    """

    def __init__(
        self, task: str, task_register: TaskRegisters, remove_from_view
    ) -> None:
        super().__init__()

        self.task_register = task_register
        self.remove_from_view = remove_from_view

        layout = QHBoxLayout()
        label = QLabel(task)
        btn_finishe = QPushButton(
            self.__get_icon("check-mark.png"),
            "",
        )
        btn_finishe.setStyleSheet("border: 0")

        btn_finishe.setMaximumWidth(60)
        btn_finishe.clicked.connect(lambda: self.finishe_task(task))

        btn_remove = QPushButton(self.__get_icon("delete.png"), "")
        btn_remove.setMaximumWidth(60)
        btn_remove.setStyleSheet("border: 0")
        btn_remove.clicked.connect(lambda: self.remove_task(task))

        layout.addWidget(label)
        layout.addWidget(btn_finishe)
        layout.addWidget(btn_remove)

        self.setLayout(layout)

    def remove_task(self, task: str) -> None:
        """
        Method to remove task from view and from saved list

        Args:
            task (str): to be removed
        """
        self.task_register.remove(task)
        self.remove_from_view(task)

    def finishe_task(self, task: str) -> None:
        """
        Method to finishe the task and move there to all finished tasks

        Args:
            task (str): should be finished
        """
        self.task_register.finishe(task)
        self.remove_from_view(task)

    def __get_icon(self, icon_name: str) -> QIcon:
        return QIcon(os.path.join(os.path.dirname(__file__), f"../images/{icon_name}"))
