#字体全局设置
from PySide6.QtWidgets import (QWidget, QGroupBox, QVBoxLayout,
                               QCheckBox, QHBoxLayout, QRadioButton, QAbstractItemView,
                               QLabel, QSizePolicy, QLineEdit,
                               QPushButton, QGridLayout, QListWidget
                               )
from PySide6.QtCore import Qt

class FontTab:
    def __init__(self, main_window, font_settings_tab):
        self.main_window = main_window
        self.window = self.main_window.window
        self.font_settings_tab = font_settings_tab

        self.font_settings_layout = QVBoxLayout()

        self.font_settings_group = QGroupBox("字体选项")
        self.font_settings_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.font_settings_group.setContentsMargins(2, 2, 2, 2)
        self.font_settings_layout.addWidget(self.font_settings_group)
        self.font_settings_layout.addStretch()

        self.font_layout = QGridLayout()
        self.font_layout.setColumnStretch(0, 2)
        self.font_layout.setColumnStretch(1, 1)
        self.font_layout.setColumnStretch(2, 1)

        self.families_widget = QWidget()
        self.families_widget.setContentsMargins(-5, 0, -5, 0)
        self.families_layout = QVBoxLayout()
        self.label1 = QLabel("字体")
        self.families_line = QLineEdit()
        self.families_line.setReadOnly(True)
        self.families_list = QListWidget()
        self.families_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.families_list.setFixedHeight(120)
        self.families_layout.addWidget(self.label1)
        self.families_layout.addWidget(self.families_line)
        self.families_layout.addWidget(self.families_list)
        self.families_widget.setLayout(self.families_layout)
        self.font_layout.addWidget(self.families_widget, 0, 0, 1, 1)

        self.styles_widget = QWidget()
        self.styles_widget.setContentsMargins(-5, 0, -5, 0)
        self.styles_widget.setFixedWidth(80)
        self.styles_layout = QVBoxLayout()
        self.label2 = QLabel("字形")
        self.styles_line = QLineEdit()
        self.styles_line.setReadOnly(True)
        self.styles_list = QListWidget()
        self.styles_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.styles_list.setFixedHeight(120)
        self.styles_layout.addWidget(self.label2)
        self.styles_layout.addWidget(self.styles_line)
        self.styles_layout.addWidget(self.styles_list)
        self.styles_widget.setLayout(self.styles_layout)
        self.font_layout.addWidget(self.styles_widget, 0, 1, 1, 1)

        self.sizes_widget = QWidget()
        self.sizes_widget.setContentsMargins(-5, 0, -5, 0)
        self.sizes_widget.setFixedWidth(80)
        self.sizes_layout = QVBoxLayout()
        self.label3 = QLabel("字号")
        self.sizes_line = QLineEdit()
        self.sizes_line.setReadOnly(True)
        self.sizes_list = QListWidget()
        self.sizes_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.sizes_list.setFixedHeight(120)
        self.sizes_layout.addWidget(self.label3)
        self.sizes_layout.addWidget(self.sizes_line)
        self.sizes_layout.addWidget(self.sizes_list)
        self.sizes_widget.setLayout(self.sizes_layout)
        self.font_layout.addWidget(self.sizes_widget, 0, 2, 1, 1)

        self.example_widget = QGroupBox("示例")
        self.example_layout = QGridLayout()
        self.example_label = QLabel("示例文本AaBb")
        self.example_layout.addWidget(self.example_label, 0, 0, Qt.AlignmentFlag.AlignCenter)
        self.example_widget.setLayout(self.example_layout)
        self.font_layout.addWidget(self.example_widget, 1, 0, 1, 1)

        self.effect_widget = QGroupBox("效果")
        self.effect_layout = QVBoxLayout()
        self.underline = QCheckBox("下划线")
        self.over_strike = QCheckBox("删除线")
        self.choose_color = QPushButton("选择颜色")
        self.effect_layout.addWidget(self.underline)
        self.effect_layout.addWidget(self.over_strike)
        self.effect_layout.addWidget(self.choose_color)
        self.effect_widget.setLayout(self.effect_layout)
        self.font_layout.addWidget(self.effect_widget, 1, 1, 1, 2)

        self.font_settings_group.setLayout(self.font_layout)

        self.font_settings_tab.setLayout(self.font_settings_layout)
