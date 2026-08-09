import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
    QMenu, QVBoxLayout, QWidget, QHeaderView
)
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("菜单与右键菜单快捷键示例")
        self.resize(600, 400)

        # ---------- 中心表格 ----------
        self.table = QTableWidget(5, 3)  # 5行3列
        self.table.setHorizontalHeaderLabels(["词名", "词频", "词性"])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        # 填充示例数据
        for row in range(5):
            self.table.setItem(row, 0, QTableWidgetItem(f"词{row+1}"))
            self.table.setItem(row, 1, QTableWidgetItem(str(row*10)))
            self.table.setItem(row, 2, QTableWidgetItem("名词"))
        self.setCentralWidget(self.table)

        # ---------- 菜单栏 ----------
        menubar = self.menuBar()
        edit_menu = menubar.addMenu("编辑(&E)")

        # 菜单栏的复制动作（Ctrl+C）
        self.menu_copy_action = QAction("复制", self)
        self.menu_copy_action.setShortcut(QKeySequence("Ctrl+C"))
        self.menu_copy_action.triggered.connect(self.on_menu_copy)
        edit_menu.addAction(self.menu_copy_action)

        # ---------- 右键菜单动作（独立对象，避免快捷键冲突） ----------
        # 注意：快捷键使用 Ctrl+Shift+C 和 Ctrl+Shift+F，避免与菜单栏冲突
        self.context_copy_action = QAction("复制到剪贴板", self)
        self.context_copy_action.setShortcut(QKeySequence("Ctrl+Shift+C"))
        self.context_copy_action.triggered.connect(self.on_context_copy)

        self.context_find_action = QAction("在文中查找", self)
        self.context_find_action.setShortcut(QKeySequence("Ctrl+Shift+F"))
        self.context_find_action.triggered.connect(self.on_context_find)

        # 将右键菜单动作注册到主窗口（让快捷键全局生效）
        self.addAction(self.context_copy_action)
        self.addAction(self.context_find_action)

        # ---------- 初始化动作启用状态 ----------
        self.update_actions_state()

        # ---------- 连接表格选择变化信号，动态更新动作启用状态 ----------
        self.table.selectionModel().selectionChanged.connect(self.update_actions_state)

        # ---------- 设置右键菜单策略 ----------
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.show_context_menu)

    # ---------- 更新动作启用状态（根据表格是否有选中行） ----------
    def update_actions_state(self):
        has_selection = len(self.table.selectedIndexes()) > 0
        self.context_copy_action.setEnabled(has_selection)
        self.context_find_action.setEnabled(has_selection)
        # 菜单栏的复制动作我们也保持同步（可选）
        self.menu_copy_action.setEnabled(has_selection)

    # ---------- 右键菜单弹出 ----------
    def show_context_menu(self, pos):
        menu = QMenu()
        menu.addAction(self.context_copy_action)
        menu.addAction(self.context_find_action)
        menu.exec(self.table.mapToGlobal(pos))

    # ---------- 槽函数 ----------
    def on_menu_copy(self):
        print("菜单栏复制触发")
        self.copy_selected_rows()

    def on_context_copy(self):
        print("右键菜单复制触发")
        self.copy_selected_rows()

    def on_context_find(self):
        print("右键菜单查找触发")
        # 模拟查找操作
        selected = self.table.currentRow()
        if selected >= 0:
            word = self.table.item(selected, 0).text()
            print(f"查找词：{word}")

    def copy_selected_rows(self):
        """将选中行的第一列内容复制到剪贴板（演示）"""
        rows = set()
        for index in self.table.selectedIndexes():
            rows.add(index.row())
        if not rows:
            return
        text = "\n".join(str(self.table.item(row, 0).text()) for row in sorted(rows))
        QApplication.clipboard().setText(text)
        print(f"已复制：{text}")

# ---------- 启动应用 ----------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())