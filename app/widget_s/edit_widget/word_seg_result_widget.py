# 编辑分词结果窗口
from PySide6.QtCore import Qt, QSignalBlocker
from PySide6.QtWidgets import QMainWindow, QTableWidget, QHeaderView, QWidget, QHBoxLayout, QLabel
from PySide6.QtGui import QAction

class WordSegResultWidget:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window
        self.word_seg_result_widget = QMainWindow(self.window)
        self.word_seg_result_widget.setWindowTitle("编辑分词结果")
        self.word_seg_result_widget.resize(600, 450)
        self.word_seg_result_widget.setAttribute(Qt.WA_DeleteOnClose)

        self.toolbar = self.word_seg_result_widget.addToolBar("主工具栏")
        self.check_action = QAction("查找", self.word_seg_result_widget)
        self.check_action.setStatusTip("通过关键信息查找分词结果项")
        self.delete_action = QAction("删除", self.word_seg_result_widget)
        self.delete_action.setStatusTip("删除部分分词结果项")
        self.save_action = QAction("保存", self.word_seg_result_widget)
        self.save_action.setStatusTip("保存修改后的分词结果项")
        self.toolbar.addAction(self.check_action)
        self.toolbar.addAction(self.delete_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.save_action)

        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout()
        self.word_seg_result_table = QTableWidget()
        self.word_seg_result_table.setFixedWidth(400)
        self.word_seg_result_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.word_seg_result_table.setSortingEnabled(True)
        self.word_seg_result_table.setColumnCount(3)
        self.word_seg_result_table.setHorizontalHeaderLabels(["词名", "词频", "词性"])
        self.word_seg_result_header = self.word_seg_result_table.horizontalHeader()
        self.word_seg_result_header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.word_seg_result_header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.word_seg_result_header.setSectionResizeMode(2, QHeaderView.Stretch)
        self.central_layout.addStretch()
        self.central_layout.addWidget(self.word_seg_result_table)
        self.central_layout.addStretch()
        self.central_widget.setLayout(self.central_layout)
        self.word_seg_result_widget.setCentralWidget(self.central_widget)

        self.state_label = QLabel("行：列：")
        self.word_seg_result_widget.statusBar().addWidget(self.state_label)

        self.word_seg_result_widget.destroyed.connect(self.on_close)

        self.word_seg_result_widget.show()

    # 用户点击窗口关闭时触发方法
    def on_close(self):
        self.main_window.menu.word_seg_result_widget = None # 将menu的widget清零
        with QSignalBlocker(self.main_window.menu.edit_seg_result_action):
            self.main_window.menu.edit_seg_result_action.setChecked(False)