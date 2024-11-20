"""
Customized input task widget
"""

from PySide6.QtWidgets import QWidget


class InputTaskWidget(QWidget):
    """
    Widget customized to has correct input text height
    """
    def __init__(self, layout):
        super().__init__()

        self.setLayout(layout)
        self.setSizePolicy(
            self.sizePolicy().horizontalPolicy(),
            self.sizePolicy().Policy.Minimum,
        )

        self.setMaximumHeight(layout.sizeHint().height())
