"""Main initialize the application."""

from PySide6.QtWidgets import QApplication

from task_management.ui.core import MainWindow


def main():
    """Run the application."""
    app = QApplication()
    main_window = MainWindow()
    main_window.show()

    app.exec()

if __name__ == "__main__":
    main() 
