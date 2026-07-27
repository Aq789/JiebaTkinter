from PySide6.QtWidgets import QTableWidget, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence

import app.service.word_class_name as s_wcn

class CustomTable(QTableWidget):
    def __init__(self, rows, cols, parent=None):
        super().__init__(rows, cols, parent)

    # 拦截 Ctrl+C 快捷键
    def keyPressEvent(self, event):

        if event.matches(QKeySequence.Copy):
            self.copy_rows_as_custom_string()
        else:
            super().keyPressEvent(event)

    # 获取选中的行，转换成特定字符串并复制到剪贴板
    def copy_rows_as_custom_string(self):

        if not self.selectedIndexes():
            return

        rows = sorted({index.row() for index in self.selectedIndexes()}) # 提取所有选中的行（去重）

        row_strings = []
        for row in rows:
            row_data = []
            for col in range(self.columnCount()):
                item = self.item(row, col)
                row_data.append(item.text() if item else "")

            formatted_row = self.format_row(row, row_data) # 调用格式转换函数，把这一行变成你想要的字符串
            row_strings.append(formatted_row)

        final_text = "\n".join(row_strings)
        QApplication.clipboard().setText(final_text)

    @staticmethod
    def format_row(row_index, data_list):
        return f"{data_list[0]} {s_wcn.simple_word_class(data_list[2])} {data_list[1]}"