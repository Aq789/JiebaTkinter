from PySide6.QtWidgets import QApplication, QPlainTextEdit

class MyEdit(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.selectionChanged.connect(self.on_selection_change)

    def on_selection_change(self):
        if self.textCursor().hasSelection():
            print("状态变为：有选中文本")
        else:
            print("状态变为：无选中文本")

app = QApplication([])
edit = MyEdit()
edit.show()
app.exec()