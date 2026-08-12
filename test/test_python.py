import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QStyle
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("菜单图标示例")

        menubar = self.menuBar()
        file_menu = menubar.addMenu("文件(&F)")

        # 1. 新建（使用系统标准图标）
        new_action = QAction("新建(&N)", self)
        new_action.setShortcut("Ctrl+N")
        # 获取系统标准图标
        new_action.setIcon(self.style().standardIcon(QStyle.SP_FileIcon))
        file_menu.addAction(new_action)

        # 2. 打开（使用系统标准图标）
        open_action = QAction("打开(&O)", self)
        open_action.setIcon(self.style().standardIcon(QStyle.SP_DirOpenIcon))
        file_menu.addAction(open_action)

        # 3. 退出（使用系统标准图标）
        exit_action = QAction("退出(&X)", self)
        exit_action.setIcon(self.style().standardIcon(QStyle.SP_DialogCloseButton))
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec())