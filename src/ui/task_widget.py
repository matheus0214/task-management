from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QWidget

class TaskWidget(QWidget):
    def __init__(self, task):
        super().__init__()

        layout = QHBoxLayout()
        label = QLabel(task)
        btn = QPushButton("Finishe")
        btn.setMaximumWidth(60)

        layout.addWidget(label)
        layout.addWidget(btn)

        self.setLayout(layout)
