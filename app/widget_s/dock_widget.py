# 侧边栏
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDockWidget
import app.widget_s.preview_window as w_pw

class DockWidget:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window
        self.dock_widget = QDockWidget("预览", self.window) # 侧边栏创建
        self.dock_widget.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)

        self.preview_window = w_pw.PreviewWindow(self.main_window, self.dock_widget)

        self.window.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock_widget)
        self.window.resizeDocks([self.dock_widget], [250], Qt.Orientation.Horizontal)