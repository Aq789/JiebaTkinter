# 分词全局设置
from PySide6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QCheckBox, QHBoxLayout, QRadioButton, QLabel, QSizePolicy, QLineEdit, QPushButton


class SegTab:
    def __init__(self, main_window, seg_settings_tab):
        self.main_window = main_window
        self.window = self.main_window.window
        self.seg_settings_tab = seg_settings_tab

        self.seg_settings_layout = QVBoxLayout()

        self.seg_settings_group = QGroupBox("分词选项")
        self.dic_settings_group = QGroupBox("词典选项")
        self.seg_settings_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.dic_settings_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.seg_settings_group.setContentsMargins(2, 2, 2, 2)
        self.dic_settings_group.setContentsMargins(2, 2, 2, 2)
        self.seg_settings_layout.addWidget(self.seg_settings_group)
        self.seg_settings_layout.addWidget(self.dic_settings_group)
        self.seg_settings_layout.addStretch()

        self.seg_layout = QVBoxLayout()

        self.mode_widget = QWidget()
        self.mode_layout = QHBoxLayout()
        self.mode_layout.setContentsMargins(0, 8, 0, 0)
        self.label1 = QLabel("切分模式：")
        self.full_mode = QRadioButton("全模式")
        self.exact_mode = QRadioButton("精确模式")
        self.search_mode = QRadioButton("搜索引擎模式")
        self.mode_layout.addWidget(self.label1)
        self.mode_layout.addWidget(self.full_mode)
        self.mode_layout.addWidget(self.exact_mode)
        self.mode_layout.addWidget(self.search_mode)
        self.mode_layout.addStretch()
        self.mode_widget.setLayout(self.mode_layout)
        self.seg_layout.addWidget(self.mode_widget)

        self.auto_seg_result_frequency = QCheckBox("是否统计词频")
        self.seg_layout.addWidget(self.auto_seg_result_frequency)

        self.auto_seg_result_class = QCheckBox("是否进行词性标注")
        self.seg_layout.addWidget(self.auto_seg_result_class)

        self.hmm_button = QCheckBox("是否开启HMM（可能增加耗时）")
        self.seg_layout.addWidget(self.hmm_button)

        self.chinese_word_class = QCheckBox("显示中文词性")
        self.seg_layout.addWidget(self.chinese_word_class)

        self.ignore_widget = QWidget()
        self.ignore_layout = QHBoxLayout()
        self.ignore_layout.setContentsMargins(0, 0, 0, 0)
        self.label2 = QLabel("忽略项：")
        self.ignore_sign_button = QCheckBox("标点符号")
        self.ignore_english_button = QCheckBox("英文单词")
        self.ignore_layout.addWidget(self.label2)
        self.ignore_layout.addWidget(self.ignore_sign_button)
        self.ignore_layout.addWidget(self.ignore_english_button)
        self.ignore_layout.addStretch()
        self.ignore_widget.setLayout(self.ignore_layout)
        self.seg_layout.addWidget(self.ignore_widget)

        self.seg_settings_group.setLayout(self.seg_layout)

        self.dic_layout = QVBoxLayout()

        self.label3 = QLabel("主词典设置")
        self.label3.setContentsMargins(0, 10, 0, 0)
        self.default_dic = QRadioButton("默认词典")
        self.custom_path = QRadioButton("自定义词典路径（不推荐）")
        self.dic_layout.addWidget(self.label3)
        self.dic_layout.addWidget(self.default_dic)
        self.dic_layout.addWidget(self.custom_path)

        self.custom_widget = QWidget()
        self.custom_widget.setContentsMargins(0, -10, 0, 0)
        self.custom_layout = QHBoxLayout()
        self.custom_path_entry = QLineEdit()
        self.custom_path_entry.setContentsMargins(0, 0, 0, 0)
        self.custom_path_button = QPushButton("...")
        self.custom_path_button.setFixedWidth(30)
        self.custom_path_button.setContentsMargins(0, 0, 0, 0)
        self.custom_layout.addWidget(self.custom_path_entry)
        self.custom_layout.addWidget(self.custom_path_button)
        self.custom_widget.setLayout(self.custom_layout)
        self.dic_layout.addWidget(self.custom_widget)

        self.dic_settings_group.setLayout(self.dic_layout)

        self.seg_settings_tab.setLayout(self.seg_settings_layout)