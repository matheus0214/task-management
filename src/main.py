"""
Main module to run the application
"""

from PySide6.QtWidgets import QApplication

from ui.core import MainWindow

if __name__ == "__main__":
    app = QApplication()

    main_window = MainWindow()
    main_window.show()

    app.exec()
