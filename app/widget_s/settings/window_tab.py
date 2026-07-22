# 窗口全局设置
from PySide6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QCheckBox, QHBoxLayout, QRadioButton, QLabel, QSizePolicy, QLineEdit, QPushButton, QSpinBox

class WindowTab:
    def __init__(self, main_window, window_settings_tab):
        self.main_window = main_window
        self.window = self.main_window.window
        self.window_settings_tab = window_settings_tab

        self.window_settings_layout = QVBoxLayout()

        self.main_settings_group = QGroupBox("主窗口选项")
        self.main_settings_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.main_settings_group.setContentsMargins(2, 2, 2, 2)
        self.window_settings_layout.addWidget(self.main_settings_group)
        self.window_settings_layout.addStretch()

        self.main_layout = QVBoxLayout()

        self.window_size_widget = QWidget()
        self.window_size_layout = QHBoxLayout()
        self.window_size_layout.setContentsMargins(0, 10, 0, 0)
        self.label1 = QLabel("窗口大小：")
        self.label2 = QLabel("宽度")
        self.window_weight = QSpinBox()
        self.window_weight.setRange(1, 3000)
        self.window_weight.setFixedWidth(80)
        self.label3 = QLabel("高度")
        self.label3.setContentsMargins(10, 0, 0, 0)
        self.window_height = QSpinBox()
        self.window_height.setRange(1, 2000)
        self.window_height.setFixedWidth(80)
        self.window_size_layout.addWidget(self.label1)
        self.window_size_layout.addWidget(self.label2)
        self.window_size_layout.addWidget(self.window_weight)
        self.window_size_layout.addWidget(self.label3)
        self.window_size_layout.addWidget(self.window_height)
        self.window_size_layout.addStretch()
        self.window_size_widget.setLayout(self.window_size_layout)
        self.main_layout.addWidget(self.window_size_widget)

        self.read_size_widget = QWidget()
        self.read_size_layout = QHBoxLayout()
        self.read_window_size = QPushButton("读取当前窗口")
        self.read_size_layout.addStretch()
        self.read_size_layout.addWidget(self.read_window_size)
        self.read_size_widget.setLayout(self.read_size_layout)
        self.main_layout.addWidget(self.read_size_widget)

        self.auto_enter = QCheckBox("默认开启自动换行")
        self.main_layout.addWidget(self.auto_enter)

        self.main_settings_group.setLayout(self.main_layout)

        self.window_settings_tab.setLayout(self.window_settings_layout)