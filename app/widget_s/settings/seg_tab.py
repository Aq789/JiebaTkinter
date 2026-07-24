# 分词全局设置
from PySide6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QCheckBox, QHBoxLayout, QRadioButton, QLabel, QSizePolicy, QLineEdit, QPushButton, QFileDialog


class SegTab:
    def __init__(self, main_window, seg_settings_tab, settings_widget):
        self.main_window = main_window
        self.window = self.main_window.window
        self.saved = True
        self.seg_settings_tab = seg_settings_tab
        self.settings_widget = settings_widget
        self.seg_settings_datas = self.main_window.seg_settings_datas

        self.read_seg_settings_datas()

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

        self.init_seg_tab_data()

        # 信号槽
        self.default_dic.clicked.connect(self.custom_state_change)
        self.custom_path.clicked.connect(self.custom_state_change)
        self.custom_path_button.clicked.connect(self.open_custom_dic_txt)
        self.full_mode.clicked.connect(self.state_has_changed)
        self.exact_mode.clicked.connect(self.state_has_changed)
        self.search_mode.clicked.connect(self.state_has_changed)
        self.auto_seg_result_frequency.clicked.connect(self.state_has_changed)
        self.auto_seg_result_class.clicked.connect(self.state_has_changed)
        self.hmm_button.clicked.connect(self.state_has_changed)
        self.chinese_word_class.clicked.connect(self.state_has_changed)
        self.ignore_sign_button.clicked.connect(self.state_has_changed)
        self.ignore_english_button.clicked.connect(self.state_has_changed)
        self.custom_path_entry.textEdited.connect(self.state_has_changed)
        self.custom_path_button.clicked.connect(self.state_has_changed)
        self.default_dic.clicked.connect(self.state_has_changed)
        self.custom_path.clicked.connect(self.state_has_changed)

    # 初始化控件方法
    def init_seg_tab_data(self):
        # 分词模式
        if self.seg_mode_data == 0:
            self.full_mode.setChecked(True)
        elif self.seg_mode_data == 1:
            self.exact_mode.setChecked(True)
        else:
            self.search_mode.setChecked(True)

        # 自动统计词频
        if self.auto_seg_result_frequency_data: self.auto_seg_result_frequency.setChecked(True)
        else: self.auto_seg_result_frequency.setChecked(False)

        # 自动进行词性标注
        if self.auto_seg_result_class_data: self.auto_seg_result_class.setChecked(True)
        else: self.auto_seg_result_class.setChecked(False)

        # 开启HMM
        if self.hmm_data: self.hmm_button.setChecked(True)
        else: self.hmm_button.setChecked(False)

        # 开启中文词性
        if self.chinese_word_class_data: self.chinese_word_class.setChecked(True)
        else: self.chinese_word_class.setChecked(False)

        # 忽略标点符号
        if self.ignore_sign_data: self.ignore_sign_button.setChecked(True)
        else: self.ignore_sign_button.setChecked(False)

        # 忽略英文单词
        if self.ignore_english_data: self.ignore_english_button.setChecked(True)
        else: self.ignore_english_button.setChecked(False)

        # 词典选择
        if self.dic_var_data == 0: self.default_dic.setChecked(True)
        else: self.custom_path.setChecked(True)

        self.custom_path_entry.setText(self.custom_path_data) # 自定义路径
        self.custom_state_change()

    # 读取数据方法
    def read_seg_settings_datas(self):
        self.seg_mode_data = self.seg_settings_datas.get_seg_mode_data()
        self.auto_seg_result_frequency_data = self.seg_settings_datas.get_auto_seg_result_frequency_data()
        self.auto_seg_result_class_data = self.seg_settings_datas.get_auto_seg_result_class_data()
        self.hmm_data = self.seg_settings_datas.get_hmm_data()
        self.chinese_word_class_data = self.seg_settings_datas.get_chinese_word_class_data()
        self.ignore_sign_data = self.seg_settings_datas.get_ignore_sign_data()
        self.ignore_english_data = self.seg_settings_datas.get_ignore_english_data()
        self.dic_var_data = self.seg_settings_datas.get_dic_var_data()
        self.custom_path_data = self.seg_settings_datas.get_custom_path()

    # 默认词典和自定义词典选择函数
    def custom_state_change(self):
        if self.default_dic.isChecked():
            self.custom_path_entry.setEnabled(False)
            self.custom_path_button.setEnabled(False)
            return 0
        elif self.custom_path.isChecked():
            self.custom_path_entry.setEnabled(True)
            self.custom_path_button.setEnabled(True)
            return 1
        else: return -1

    # 打开自定义词典函数
    def open_custom_dic_txt(self):
        file_path, selected_filter = QFileDialog.getOpenFileName(
            self.seg_settings_tab,
            "请选择自定义词典路径",
            "C:/",
            "文本文件 (*.txt);;所有文件 (*.*)"
        )
        if file_path:
            self.custom_path_entry.setText(file_path)
            return True
        else: return False

    # 分词模式映射方法
    def seg_mode(self):
        if self.full_mode.isChecked(): return 0
        elif self.exact_mode.isChecked(): return 1
        elif self.search_mode.isChecked(): return 2
        else: return -1

    # 状态变化函数
    def state_has_changed(self):
       data_state = [
           self.seg_mode_data,
           self.auto_seg_result_frequency_data,
           self.auto_seg_result_class_data,
           self.hmm_data,
           self.chinese_word_class_data,
           self.ignore_sign_data,
           self.ignore_english_data,
           self.dic_var_data,
           self.custom_path_data
       ]
       current_state = [
           self.seg_mode(),
           self.auto_seg_result_frequency.isChecked(),
           self.auto_seg_result_class.isChecked(),
           self.hmm_button.isChecked(),
           self.chinese_word_class.isChecked(),
           self.ignore_sign_button.isChecked(),
           self.ignore_english_button.isChecked(),
           self.custom_state_change(),
           self.custom_path_entry.text()
       ]
       if data_state != current_state:
           self.saved = False
           self.settings_widget.state_has_changed()
       else:
           self.saved = True
           self.settings_widget.state_has_changed()