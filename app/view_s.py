# 主窗口创建
from PySide6.QtWidgets import QMainWindow
import app.widget_s.menu
import app.widget_s.dock_widget
import app.widget_s.central_widget
import app.widget_s.status_widget

def create_new_window(): # 创建窗口实例方法
    new_window = MainWindow() # 创建窗口实例
    MainWindow.windows.append(new_window) # 添加窗口到列表

def delete_new_window(): # 删除窗口实例方法
    last_window = MainWindow.windows.pop() # 将列表中最后一个窗口去掉并记录下来


class MainWindow:
    windows = []

    def __init__(self):
        self.window = QMainWindow()
        self.window.setWindowTitle("中文分词工具")
        self.window.resize(800, 450)
        self.window.show()

        # 加载模块
        app.widget_s.menu.Menu(self)
        app.widget_s.dock_widget.DockWidget(self)
        app.widget_s.central_widget.CentralWidget(self)
        app.widget_s.status_widget.StatusWidget(self)

    # 销毁窗口
    def destroy_window(self):
        if self.window:
            self.window.close()