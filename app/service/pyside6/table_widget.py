from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QTableWidget, QApplication, QTableWidgetItem

import app.service.word_class_name as s_wcn
import app.service.word_dic as s_wd
from service.pyside6.numeric_table_item import NumericTableItem


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
            return None

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

        return rows

    # 获取选中的行，转换成特定字符串并复制到剪贴板
    def cut_rows_as_custom_string(self):
        rows = self.copy_rows_as_custom_string()

        if not rows:
            return

        for row in sorted(rows, reverse=True):
            self.removeRow(row)

    # 获取剪贴板中的内容，转换成表格内容
    def paste_rows_as_custom_string(self):
        clipboard = QApplication.clipboard().text()

        temp_list = s_wd.txt_to_dic(clipboard)
        for row in temp_list:
            self.create_dic_data(row[0], row[1], row[2])
        return True

    # 在表格中添加数据方法
    def new_row(self, row, word_name, word_frequency, word_class):
        self.insertRow(row)
        self.setItem(row, 0, QTableWidgetItem(str(word_name)))
        self.setItem(row, 1, NumericTableItem(str(word_frequency)))
        self.setItem(row, 2, QTableWidgetItem(str(word_class)))

    # 新建数据方法
    def create_dic_data(self, word_name, word_frequency, word_class):
        selected_rows = set()
        for index in self.selectedIndexes():
            selected_rows.add(index.row())

        if len(selected_rows) == 1:
            selected_row = next(iter(selected_rows))
            self.new_row(selected_row + 1, word_name, word_frequency, word_class)
        else:
            self.new_row(self.rowCount(), word_name, word_frequency, word_class)

    @staticmethod
    def format_row(row_index, data_list):
        return f"{data_list[0]} {data_list[1]} {s_wcn.simple_word_class(data_list[2])}"