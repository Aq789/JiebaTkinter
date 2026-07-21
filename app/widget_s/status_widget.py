# 状态栏
from PySide6.QtWidgets import QLabel


class StatusWidget:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window

        self.status_bar = self.window.statusBar()

        self.status_label = QLabel("准备就绪")
        self.status_label.setContentsMargins(12, 2, 12, 2)
        self.status_bar.addWidget(self.status_label)