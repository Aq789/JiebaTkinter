# 窗口全局设置
from PySide6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QCheckBox, QHBoxLayout, QRadioButton, QLabel, QSizePolicy, QLineEdit, QPushButton, QSpinBox

class WindowTab:
    def __init__(self, main_window, window_settings_tab, settings_widget):
        self.main_window = main_window
        self.window = self.main_window.window
        self.saved = True
        self.window_settings_tab = window_settings_tab
        self.settings_widget = settings_widget
        self.window_settings_datas = self.main_window.window_settings_datas

        self.read_window_settings_datas()

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
        self.label3 = QLabel("高度")
        self.label3.setContentsMargins(10, 0, 0, 0)
        self.window_height = QSpinBox()
        self.window_height.setRange(1, 2000)
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
        self.init_window_tab_data()

        # 信号槽
        self.read_window_size.clicked.connect(self.get_window_size)
        self.window_weight.valueChanged.connect(self.state_has_changed)
        self.window_height.valueChanged.connect(self.state_has_changed)
        self.read_window_size.clicked.connect(self.state_has_changed)
        self.auto_enter.clicked.connect(self.state_has_changed)

    # 初始化控件方法
    def init_window_tab_data(self):
        self.window_weight.setValue(self.window_weight_data) # 窗口宽度
        self.window_height.setValue(self.window_height_data) # 窗口高度

        # 自动换行
        if self.auto_enter_data: self.auto_enter.setChecked(True)
        else: self.auto_enter.setChecked(False)

    # 读取数据方法
    def read_window_settings_datas(self):
        self.window_weight_data = self.window_settings_datas.get_window_weight_data()
        self.window_height_data = self.window_settings_datas.get_window_height_data()
        self.auto_enter_data = self.window_settings_datas.get_auto_enter_data()

    # 获取窗口大小并更改信息
    def get_window_size(self):
        window_weight, window_height = self.main_window.get_window_size()
        self.window_weight.setValue(window_weight)
        self.window_height.setValue(window_height)

    # 状态变化函数
    def state_has_changed(self):
        data_state = [
            self.window_weight_data,
            self.window_height_data,
            self.auto_enter_data
        ]
        current_state = [
            self.window_weight.value(),
            self.window_height.value(),
            self.auto_enter.isChecked()
        ]
        if data_state != current_state:
            self.saved = False
            self.settings_widget.state_has_changed()
        else:
            self.saved = True
            self.settings_widget.state_has_changed()