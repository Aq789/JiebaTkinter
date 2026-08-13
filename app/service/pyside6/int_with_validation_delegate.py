# 限制单元格输入数字
from PySide6.QtCore import Qt, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QStyledItemDelegate, QLineEdit


class IntWithValidationDelegate(QStyledItemDelegate):

    def __init__(self, parent=None, min_val=0, max_val=9999):
        super().__init__(parent)
        self.min_val = min_val
        self.max_val = max_val

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        regex = QRegularExpression(r'^[0-9]*$')
        validator = QRegularExpressionValidator(regex, parent)
        editor.setValidator(validator)
        return editor

    def setEditorData(self, editor, index):
        value = index.data(Qt.EditRole)
        editor.setText(str(value) if value is not None else "")

    def setModelData(self, editor, model, index):
        text = editor.text().strip()

        if text == "":
            model.setData(index, "")
            return

        try:
            value = int(text)
            if not (self.min_val <= value <= self.max_val):
                raise ValueError("超出范围")
        except ValueError:
            return

        model.setData(index, value) # 全部合法，更新数据