from PySide6.QtWidgets import QApplication, QTableView
from PySide6.QtGui import QStandardItemModel, QStandardItem

app = QApplication([])
model = QStandardItemModel(3, 2)
model.setHorizontalHeaderLabels(["商品", "价格"])
model.setItem(0, 0, QStandardItem("苹果"))
model.setItem(0, 1, QStandardItem("5.5"))

view = QTableView()
view.setModel(model)
view.show()
app.exec()