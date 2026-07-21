# 工作区
from PySide6.QtWidgets import QWidget


class CentralWidget:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window
        self.central_widget = QWidget(self.window)

        self.window.setCentralWidget(self.central_widget)