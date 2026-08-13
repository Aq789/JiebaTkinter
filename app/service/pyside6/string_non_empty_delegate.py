# 限制单元格不为空
from PySide6.QtWidgets import QStyledItemDelegate

class StringNonEmptyDelegate(QStyledItemDelegate):
    def setModelData(self, editor, model, index):
        text = editor.text().strip()
        if text == "":
            return
        model.setData(index, text)