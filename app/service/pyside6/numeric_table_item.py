# 表格数字比较重写
from PySide6.QtWidgets import QTableWidgetItem

class NumericTableItem(QTableWidgetItem):
    def __lt__(self, other):
        try:
            return float(self.text()) < float(other.text())
        except (ValueError, TypeError):
            return super().__lt__(other)