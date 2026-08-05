# 状态栏
from PySide6.QtWidgets import QLabel, QProgressBar, QWidget, QHBoxLayout
from PySide6.QtCore import QTimer
import app.service.statistic as s_s


class StatusWidget:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window
        self.text_edit = self.main_window.central_widget.text_edit

        self.status_bar = self.window.statusBar()

        self.point_label = QLabel("当前位置：行0, 列0")
        self.point_label.setContentsMargins(10, 0, 10, 0)
        self.status_bar.addWidget(self.point_label)

        self.chinese_char_count = QLabel("总字数：0")
        self.chinese_char_count.setContentsMargins(10, 0, 10, 0)
        self.status_bar.addWidget(self.chinese_char_count)

        self.custom_dict_count = QLabel("自定义词典数：")
        self.custom_dict_count.setContentsMargins(10, 0, 10, 0)
        self.status_bar.addWidget(self.custom_dict_count)

        self.status_container = QWidget()
        self.status_container.setContentsMargins(10, 0, 10, 0)

        self.status_layout = QHBoxLayout(self.status_container)
        self.status_layout.setContentsMargins(0, 0, 0, 0)
        self.status_layout.setSpacing(0)

        self.state = QLabel("就绪")
        self.state.setContentsMargins(0, 0, 10, 0)
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setFixedWidth(100)
        self.progress_bar.setValue(0)

        self.status_layout.addStretch()
        self.status_layout.addWidget(self.state)
        self.status_layout.addWidget(self.progress_bar)
        self.status_bar.addPermanentWidget(self.status_container)

        self.saved = QLabel("未保存")
        self.saved.setContentsMargins(10, 0, 10, 0)
        self.status_bar.addPermanentWidget(self.saved)

        self.refresh_custom_dict_count()

        self.text_edit.cursorPositionChanged.connect(self.refresh_point_label)
        self.text_edit.cursorPositionChanged.connect(self.refresh_chinese_char_count)

    # 返回行号和列号
    def refresh_point_label(self):
        cursor = self.text_edit.textCursor()
        row = cursor.blockNumber() + 1
        col = cursor.columnNumber() + 1
        self.point_label.setText(f"当前位置：行{row}, 列{col}")

    # 字数以及选中文本
    def refresh_chinese_char_count(self):
        cursor = self.text_edit.textCursor()
        if cursor.selectedText():
            self.chinese_char_count.setText(
                f"总字数：{s_s.first_statistic(self.text_edit.toPlainText())[0]}  选中：{s_s.first_statistic(cursor.selectedText())[0]}")
        else:
            self.chinese_char_count.setText(f"总字数：{s_s.first_statistic(self.text_edit.toPlainText())[0]}")

    # 自定义词典数
    def refresh_custom_dict_count(self):
        custom_dict_count = self.main_window.word_dic_datas.return_len_word_dic_list()
        self.custom_dict_count.setText(f"自定义词典数：{custom_dict_count}")

    # 就绪状态设置
    def set_ready_status(self, message):
        self.state.setText(message)
        self.progress_bar.setVisible(False)

    # 进行状态设置
    def set_process_status(self, message):
        self.state.setText(message)
        self.progress_bar.setVisible(True)

    # 设置消息状态
    def set_message_status(self, message, text="就绪", timeout=1500):
        self.state.setText(message)
        self.progress_bar.setVisible(False)
        QTimer.singleShot(timeout, lambda :self.state.setText(text))

    # 设置进度条
    def set_process_bar(self, value):
        self.progress_bar.setValue(value)

    # 状态栏隐藏方法
    def toggle_statusbar(self):
        if self.window.statusBar().isVisible():
            self.status_bar.hide()
            self.main_window.menu.status_bar_hidden_action.setChecked(True)
        else:
            self.status_bar.show()
            self.main_window.menu.status_bar_hidden_action.setChecked(False)