#字体全局设置
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import (QWidget, QGroupBox, QVBoxLayout,
                               QCheckBox, QAbstractItemView,
                               QLabel, QSizePolicy, QLineEdit,
                               QGridLayout, QListWidget,
                               QScrollArea, QHBoxLayout, QPushButton)

class FontTab:
    def __init__(self, main_window, font_settings_tab, settings_widget):
        self.main_window = main_window
        self.window = self.main_window.window
        self.saved = True
        self.font_settings_tab = font_settings_tab
        self.settings_widget = settings_widget
        self.font_settings_datas = self.main_window.font_settings_datas

        self.read_font_settings_datas()

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
        self.example_scroll = QScrollArea()
        self.example_scroll.setWidgetResizable(True)
        self.example_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.example_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.example_scroll_widget = QWidget()
        self.example_scroll_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.example_scroll_layout = QVBoxLayout(self.example_scroll_widget)
        self.example_scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.example_label = QLabel("示例文本AaBb")
        self.example_label.setMinimumHeight(100)
        self.example_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.example_label.setContentsMargins(0, 0, 0, 0)
        self.example_scroll_layout.addWidget(self.example_label)
        self.example_scroll.setWidget(self.example_scroll_widget)
        self.example_layout = QGridLayout(self.example_widget)
        self.example_layout.setContentsMargins(0, 0, 0, 0)
        self.example_layout.addWidget(self.example_scroll, 0, 0)
        self.example_widget.setLayout(self.example_layout)
        self.font_layout.addWidget(self.example_widget, 1, 0, 1, 1)

        self.effect_widget = QGroupBox("效果")
        self.effect_layout = QVBoxLayout()
        self.underline = QCheckBox("下划线")
        self.over_strike = QCheckBox("删除线")
        self.effect_layout.addWidget(self.underline)
        self.effect_layout.addWidget(self.over_strike)
        self.effect_layout.addStretch()
        self.effect_widget.setLayout(self.effect_layout)
        self.font_layout.addWidget(self.effect_widget, 1, 1, 1, 2)

        self.reset_widget = QWidget()
        self.reset_layout = QHBoxLayout()
        self.reset = QPushButton("重置")
        self.reset_layout.addStretch()
        self.reset_layout.addWidget(self.reset)
        self.reset_widget.setLayout(self.reset_layout)
        self.font_layout.addWidget(self.reset_widget, 2, 0, 1, 3)

        self.font_settings_group.setLayout(self.font_layout)

        self.font_settings_tab.setLayout(self.font_settings_layout)
        self.init_font_tab_data()

        # 信号槽
        self.families_list.currentItemChanged.connect(self.font_change)
        self.styles_list.currentItemChanged.connect(self.font_change)
        self.sizes_list.currentItemChanged.connect(self.font_change)
        self.underline.clicked.connect(self.font_change)
        self.over_strike.clicked.connect(self.font_change)
        self.families_list.itemClicked.connect(self.state_has_changed)
        self.styles_list.itemClicked.connect(self.state_has_changed)
        self.sizes_list.itemClicked.connect(self.state_has_changed)
        self.underline.clicked.connect(self.state_has_changed)
        self.over_strike.clicked.connect(self.state_has_changed)
        self.reset.clicked.connect(self.init_font_tab_data)
        self.reset.clicked.connect(self.state_has_changed)

    # 初始化控件方法
    def init_font_tab_data(self):
        self.reset_font()

        # 示例文本
        self.update_example_label(self.families_line.text(),
                                  self.styles_line.text(),
                                  int(self.sizes_line.text()),
                                  self.underline.isChecked(),
                                  self.over_strike.isChecked())

    # 读取数据方法
    def read_font_settings_datas(self):
        self.font_data = self.font_settings_datas.get_font_data()
        self.shape_data = self.font_settings_datas.get_shape_data()
        self.size_data = self.font_settings_datas.get_size_data()
        self.under_line_data = self.font_settings_datas.get_under_line_data()
        self.delete_line_data = self.font_settings_datas.get_delete_line_data()
        self.color_data = self.font_settings_datas.get_color_data()

    # 重置字体方法
    def reset_font(self):
        self.fill_font_data()
        self.families_line.setText(self.font_data)  # 字体
        self.styles_line.setText(self.shape_data)  # 字形
        self.sizes_line.setText(str(self.size_data))  # 字号
        self.choose_list(self.families_list, self.font_data)  # 初始选中
        self.choose_list(self.styles_list, self.shape_data)
        self.choose_list(self.sizes_list, str(self.size_data))

        # 下划线
        if self.under_line_data:
            self.underline.setChecked(True)
        else:
            self.underline.setChecked(False)

        # 删除线
        if self.delete_line_data:
            self.over_strike.setChecked(True)
        else:
            self.over_strike.setChecked(False)

    # 将字体、字形、字号信息填入控件中
    def fill_font_data(self):
        families = QFontDatabase.families()
        sizes = list(range(8, 73, 2))
        styles = ["常规", "粗体", "斜体", "粗斜体"]

        self.families_list.addItems(families)
        self.styles_list.addItems(styles)
        self.sizes_list.addItems([str(s) for s in sizes])

    # 示例文本更新
    def update_example_label(self, family, style, size, underline, over_strike):
        style_map = {"常规": (QFont.Normal, False), "粗体": (QFont.Bold, False), "斜体": (QFont.Normal, True), "粗斜体": (QFont.Bold, True)}
        weight, italic = style_map.get(style, (QFont.Normal, False))
        font = QFont(family, size, weight, italic)
        font.setUnderline(underline)
        font.setStrikeOut(over_strike)
        self.example_label.setFont(font)

    # 字体改变函数
    def font_change(self):
        family_current_item = self.families_list.currentItem()
        if family_current_item:
            family = family_current_item.text()
            self.families_line.setText(family)
        style_current_item = self.styles_list.currentItem()
        if style_current_item:
            style = style_current_item.text()
            self.styles_line.setText(style)
        size_current_item = self.sizes_list.currentItem()
        if size_current_item:
            size = size_current_item.text()
            self.sizes_line.setText(size)

        # 示例文本更新
        self.update_example_label(self.families_line.text(),
                                    self.styles_line.text(),
                                    int(self.sizes_line.text()),
                                    self.underline.isChecked(),
                                    self.over_strike.isChecked())

    # 根据名称选中某项
    @staticmethod
    def choose_list(list_widget, name):
        items = list_widget.findItems(name, Qt.MatchFlag.MatchExactly)
        if items:
            list_widget.setCurrentItem(items[0])
            list_widget.scrollToItem(items[0])

    # 状态变化函数
    def state_has_changed(self):
       data_state = [
           self.font_data,
           self.shape_data,
           self.size_data,
           self.under_line_data,
           self.delete_line_data
       ]
       current_state = [
           self.families_line.text(),
           self.styles_line.text(),
           int(self.sizes_line.text()),
           self.underline.isChecked(),
           self.over_strike.isChecked()
       ]
       if data_state != current_state:
           self.saved = False
           self.settings_widget.state_has_changed()
       else:
           self.saved = True
           self.settings_widget.state_has_changed()