# 查找窗口
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextDocument, QTextCursor
from PySide6.QtWidgets import QPushButton, QLabel, QDialog, QGridLayout, QLineEdit


class CheckWidget:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window
        self.text_edit = self.main_window.central_widget.text_edit
        self.check_widget = QDialog(self.window)
        self.check_widget.setWindowTitle("查找或替换")
        self.check_widget.setFixedSize(400, 100)
        self.check_widget.setAttribute(Qt.WA_DeleteOnClose)

        self.layout = QGridLayout()

        self.label1 = QLabel("查找：")
        self.layout.addWidget(self.label1, 0, 0)
        self.check = QLineEdit()
        self.layout.addWidget(self.check, 0, 1)
        self.previous = QPushButton("上一个")
        self.layout.addWidget(self.previous, 0, 2)
        self.next = QPushButton("下一个")
        self.layout.addWidget(self.next, 0, 3)

        self.label2 = QLabel("替换为：")
        self.layout.addWidget(self.label2, 1, 0)
        self.place = QLineEdit()
        self.layout.addWidget(self.place, 1, 1)
        self.place_button = QPushButton("替换")
        self.layout.addWidget(self.place_button, 1, 2)
        self.place_all_button = QPushButton("替换所有")
        self.layout.addWidget(self.place_all_button, 1, 3)

        self.check_widget.setLayout(self.layout)

        self.check_widget.show()

        # 信号槽
        self.check_widget.destroyed.connect(self.on_close)
        self.next.clicked.connect(self.check_next)
        self.previous.clicked.connect(self.check_previous)
        self.place_button.clicked.connect(self.place_text)
        self.place_all_button.clicked.connect(self.place_all_text)

    def on_close(self):
        self.main_window.menu.check_widget = None

    # 查找下一个
    def check_next(self):
        self.text_edit.find(self.check.text())

    # 查找上一个
    def check_previous(self):
        flags = QTextDocument.FindFlag.FindBackward
        self.text_edit.find(self.check.text(), flags)

    # 替换
    def place_text(self):
        cursor = self.text_edit.textCursor()
        if cursor.hasSelection():
            cursor.insertText(self.place.text())

    # 替换所有
    def place_all_text(self):
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QTextCursor.Start)
        self.text_edit.setTextCursor(cursor)

        count = 0
        while self.text_edit.find(self.check.text()):
            cursor = self.text_edit.textCursor()
            cursor.insertText(self.place.text())
            count += 1

            cursor.movePosition(QTextCursor.NextCharacter, QTextCursor.MoveAnchor)
            self.text_edit.setTextCursor(cursor)