# 统计窗口
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QLabel, QDialog, QGroupBox, QGridLayout

import app.controllers.statistic_widget as c_sw

class StatisticWidget:
    def __init__(self, main_window):
        class MessageLabel:
            def __init__(self, message_label, layout, row):
                self.message_label = QLabel(message_label)
                self.message = QLabel("-")
                layout.addWidget(self.message_label, row, 0)
                layout.addWidget(self.message, row, 1, Qt.AlignRight)

        self.main_window = main_window
        self.window = self.main_window.window
        self.statistic_widget = QDialog()
        self.statistic_widget.setWindowTitle("统计")
        self.statistic_widget.setModal(True)
        self.statistic_widget.setFixedSize(240, 300)

        self.statistic_layout = QGridLayout()

        self.statistic_group = QGroupBox("统计信息")

        self.message_layout = QGridLayout()

        self.chinese_char_count = MessageLabel("中文字数", self.message_layout, 0)
        self.char_count_no_space = MessageLabel("字符数", self.message_layout, 1)
        self.char_count_with_space = MessageLabel("字符数（计空格）", self.message_layout, 2)
        self.chinese_word_count = MessageLabel("* 中文词数", self.message_layout, 3)
        self.seg_result_count_only_chinese = MessageLabel("* 分词结果总数（仅中文）", self.message_layout, 4)
        self.seg_result_count_all = MessageLabel("* 分词结果总数（所有）", self.message_layout, 5)
        self.custom_dict_size = MessageLabel("* 自定义词典总数", self.message_layout, 6)
        self.english_word_count = MessageLabel("* 英文单词数", self.message_layout, 7)
        self.line_count = MessageLabel("行数", self.message_layout, 8)

        self.statistic_group.setLayout(self.message_layout)

        self.statistic_layout.addWidget(self.statistic_group, 0, 0, 1, 2)

        self.label = QLabel("* 部分数据需分词后可见")
        self.statistic_layout.addWidget(self.label, 1, 0, 1, 2)

        self.label2 = QLabel()
        self.statistic_layout.addWidget(self.label2, 2, 0, 1, 1)

        self.close_button = QPushButton("关闭")
        self.statistic_layout.addWidget(self.close_button, 2, 1, 1, 1, Qt.AlignRight)

        self.statistic_widget.setLayout(self.statistic_layout)

        c_sw.statistic_start(self)

        self.close_button.clicked.connect(self.on_close)

        self.statistic_widget.exec()

    # 关闭方法
    def on_close(self):
        self.statistic_widget.close()