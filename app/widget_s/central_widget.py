# 工作区
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit


class CentralWidget:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window
        self.central_widget = QWidget(self.window)
        self.central_layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        self.text_edit.setAcceptRichText(False)
        self.central_layout.addWidget(self.text_edit)
        self.central_widget.setLayout(self.central_layout)

        self.window.setCentralWidget(self.central_widget)

        """QSS样式表"""
        self.text_edit.setStyleSheet("""
                QTextEdit {
                    border: 0px solid #cccccc;
                    border-radius: 4px;
                    padding: 4px;
                }
                QTextEdit:focus {
                    border: 0px solid #cccccc;
                    outline: none;
                }
            """)