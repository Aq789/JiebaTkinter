# 编辑词典窗口
from PySide6.QtCore import Qt, QSignalBlocker
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QTableWidget, QHeaderView, QLabel


class WordDicWidget:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window
        self.word_dic_widget = QMainWindow(self.window)
        self.word_dic_widget.setWindowTitle("编辑词典")
        self.word_dic_widget.resize(600, 450)
        self.word_dic_widget.setAttribute(Qt.WA_DeleteOnClose)

        self.toolbar = self.word_dic_widget.addToolBar("主工具栏")
        self.new_action = QAction("新建", self.word_dic_widget)
        self.new_action.setStatusTip("新建词典项")
        self.delete_action = QAction("删除", self.word_dic_widget)
        self.delete_action.setStatusTip("删除部分词典项")
        self.edit_action = QAction("编辑", self.word_dic_widget)
        self.edit_action.setStatusTip("编辑所选词典项")
        self.check_action = QAction("查找", self.word_dic_widget)
        self.check_action.setStatusTip("通过关键信息查找词典项")
        self.save_action = QAction("保存", self.word_dic_widget)
        self.save_action.setStatusTip("保存修改后的词典")
        self.toolbar.addAction(self.new_action)
        self.toolbar.addAction(self.delete_action)
        self.toolbar.addAction(self.edit_action)
        self.toolbar.addAction(self.check_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.save_action)

        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout()
        self.word_dic_table = QTableWidget()
        self.word_dic_table.setFixedWidth(400)
        self.word_dic_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.word_dic_table.setSortingEnabled(True)
        self.word_dic_table.setColumnCount(3)
        self.word_dic_table.setHorizontalHeaderLabels(["词名", "词频", "词性"])
        self.word_dic_header = self.word_dic_table.horizontalHeader()
        self.word_dic_header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.word_dic_header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.word_dic_header.setSectionResizeMode(2, QHeaderView.Stretch)
        self.central_layout.addStretch()
        self.central_layout.addWidget(self.word_dic_table)
        self.central_layout.addStretch()
        self.central_widget.setLayout(self.central_layout)
        self.word_dic_widget.setCentralWidget(self.central_widget)

        self.state_label = QLabel("行：列：")
        self.word_dic_widget.statusBar().addWidget(self.state_label)

        self.word_dic_widget.destroyed.connect(self.on_close)

        self.word_dic_widget.show()

    # 用户点击窗口关闭时触发方法
    def on_close(self):
        self.main_window.menu.word_dic_widget = None
        with QSignalBlocker(self.main_window.menu.edit_dic_action):
            self.main_window.menu.edit_dic_action.setChecked(False)