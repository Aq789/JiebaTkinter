# 设置窗口
from PySide6.QtWidgets import QDialog, QVBoxLayout, QTabWidget, QWidget, QHBoxLayout, QPushButton
import app.widget_s.settings.seg_tab as w_sst
import app.widget_s.settings.window_tab as w_swt
import app.widget_s.settings.font_tab as w_sft

class SettingsWidget:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window
        self.settings_widget = QDialog()
        self.settings_widget.setWindowTitle("全局设置")
        self.settings_widget.setModal(True)
        self.settings_widget.resize(400, 500)
        #self.settings_widget.setFixedSize(400, 500)

        # 标签栏部分
        self.settings_layout = QVBoxLayout()
        self.settings_tab_widget = QTabWidget() # 放置标签页
        self.seg_settings_tab = QWidget()
        self.font_settings_tab = QWidget()
        self.window_settings_tab = QWidget()
        self.settings_tab_widget.addTab(self.seg_settings_tab, "分词设置")
        self.settings_tab_widget.addTab(self.window_settings_tab, "窗口设置")
        self.settings_tab_widget.addTab(self.font_settings_tab, "字体设置")
        self.seg_tab = w_sst.SegTab(self.main_window, self.seg_settings_tab)
        self.window_tab = w_swt.WindowTab(self.main_window, self.window_settings_tab)
        self.font_tab = w_sft.FontTab(self.main_window, self.font_settings_tab)


        self.settings_layout.addWidget(self.settings_tab_widget)

        # 底部按钮
        self.bottom_button_widget = QWidget()
        self.bottom_button_widget_layout = QHBoxLayout()
        self.bottom_button_widget_layout.addStretch()
        self.ok_button = QPushButton("确定")
        self.cancel_button = QPushButton("取消")
        self.apply_button = QPushButton("应用")
        self.bottom_button_widget_layout.addWidget(self.ok_button)
        self.bottom_button_widget_layout.addWidget(self.cancel_button)
        self.bottom_button_widget_layout.addWidget(self.apply_button)
        self.bottom_button_widget_layout.setContentsMargins(2, 5, 2, 0)
        self.bottom_button_widget.setLayout(self.bottom_button_widget_layout)
        self.settings_layout.addWidget(self.bottom_button_widget)

        self.settings_widget.setLayout(self.settings_layout)

        self.settings_widget.exec()