from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QWidget

from data.register import TaskRegisters


class TaskWidget(QWidget):
    def __init__(self, task: str, task_register: TaskRegisters,
                 remove_from_view) -> None:
        super().__init__()

        self.task_register = task_register
        self.remove_from_view = remove_from_view

        layout = QHBoxLayout()
        label = QLabel(task)
        btn_finishe = QPushButton("Finishe")
        btn_finishe.setMaximumWidth(60)
        btn_finishe.clicked.connect(lambda  : self.finishe_task(task))

        btn_remove = QPushButton("Remove")
        btn_remove.setMaximumWidth(60)
        btn_remove.clicked.connect(lambda  : self.remove_task(task))

        layout.addWidget(label)
        layout.addWidget(btn_finishe)
        layout.addWidget(btn_remove)

        self.setLayout(layout)

    def remove_task(self, task: str) -> None:
        self.task_register.remove(task)
        self.remove_from_view(task)

    def finishe_task(self, task: str) -> None:
        self.task_register.finishe(task)
        self.remove_from_view(task)
