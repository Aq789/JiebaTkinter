# 编辑分词结果窗口
from PySide6.QtCore import Qt, QSignalBlocker
from PySide6.QtWidgets import QMessageBox, QMainWindow, QTableWidget, QHeaderView, QWidget, QHBoxLayout, QLabel, \
    QAbstractItemView, QMenu
from PySide6.QtGui import QAction, QKeySequence
from app.service.pyside6.table_widget import CustomTable
import app.controllers.edit_widget.word_seg_result_widget as c_ewwsrw

class WordSegResultWidget:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window
        self.saved = True
        self.word_seg_result_widget = QMainWindow(self.window)
        self.word_seg_result_widget.setWindowTitle("编辑分词结果")
        self.word_seg_result_widget.setMinimumSize(400, 450)
        self.word_seg_result_widget.setAttribute(Qt.WA_DeleteOnClose)

        self.toolbar = self.word_seg_result_widget.addToolBar("主工具栏")
        self.check_action = QAction("查找", self.word_seg_result_widget)
        self.check_action.setShortcut(QKeySequence("Ctrl+F"))
        self.check_action.setCheckable(True)
        self.check_action.setStatusTip("通过关键信息查找分词结果项")
        self.check_action.setToolTip("查找 Ctrl+F")
        self.delete_action = QAction("删除", self.word_seg_result_widget)
        self.delete_action.setStatusTip("删除部分分词结果项")
        self.delete_action.setShortcut(QKeySequence("Delete"))
        self.delete_action.setToolTip("删除 Delete")
        self.copy_action = QAction("复制", self.word_seg_result_widget)
        self.copy_action.setShortcut(QKeySequence("Ctrl+C"))
        self.copy_action.setStatusTip("复制所选表格内容到剪贴板")
        self.copy_action.setToolTip("复制 Ctrl+C")
        self.save_action = QAction("保存", self.word_seg_result_widget)
        self.save_action.setShortcut(QKeySequence("Ctrl+S"))
        self.save_action.setStatusTip("保存修改后的分词结果项")
        self.save_action.setToolTip("保存 Ctrl+S")
        self.toolbar.addAction(self.check_action)
        self.toolbar.addAction(self.delete_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.copy_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.save_action)

        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout()
        self.word_seg_result_table = CustomTable(self.central_widget, 3)
        self.word_seg_result_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.word_seg_result_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.word_seg_result_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.word_seg_result_table.setSortingEnabled(True)
        self.word_seg_result_table.setColumnCount(3)
        self.word_seg_result_table.setHorizontalHeaderLabels(["词名", "词频", "词性"])
        self.word_seg_result_header = self.word_seg_result_table.horizontalHeader()
        self.word_seg_result_header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.word_seg_result_header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.word_seg_result_header.setSectionResizeMode(2, QHeaderView.Stretch)
        self.central_layout.addWidget(self.word_seg_result_table)
        self.central_widget.setLayout(self.central_layout)
        self.word_seg_result_widget.setCentralWidget(self.central_widget)

        self.state_label = QLabel("总计 项")
        self.state_label.setContentsMargins(5, 1, 5, 1)
        self.save_state = QLabel("已保存")
        self.save_state.setContentsMargins(5, 1, 5, 1)
        self.word_seg_result_widget.statusBar().addWidget(self.state_label)
        self.word_seg_result_widget.statusBar().addWidget(self.save_state)

        c_ewwsrw.input_seg_result_data(self)

        self.menu_action = self.main_window.menu.edit_seg_result_action

        self.word_seg_result_widget.closeEvent = self.custom_close_event

        # 信号槽
        self.word_seg_result_widget.destroyed.connect(self.on_close)
        self.delete_action.triggered.connect(lambda :c_ewwsrw.delete_current_row(self))
        self.check_action.toggled.connect(lambda :c_ewwsrw.check_datas(self))
        self.save_action.triggered.connect(lambda :c_ewwsrw.output_seg_result_data(self))
        self.word_seg_result_table.horizontalHeader().sortIndicatorChanged.connect(lambda :c_ewwsrw.save_refresh(self, False))
        self.word_seg_result_table.itemSelectionChanged.connect(lambda :c_ewwsrw.status_refresh(self))
        self.copy_action.triggered.connect(self.copy)
        self.word_seg_result_table.customContextMenuRequested.connect(self.menu)

        # 表格样式
        self.word_seg_result_table.setStyleSheet(
            """
                QTableWidget::item:selected {
                    background-color: palette(highlight);
                    color: palette(highlighted-text);
                }
            """
        )

        self.word_seg_result_widget.show()

    # 右键菜单
    def menu(self, pos):
        self.menu = QMenu()
        self.copy_menu_action = QAction("复制")
        self.copy_menu_action.setShortcut(QKeySequence("Ctrl+C"))
        self.delete_menu_action = QAction("删除")
        self.delete_menu_action.setShortcut(QKeySequence("Delete"))

        self.menu.addAction(self.copy_menu_action)
        self.menu.addSeparator()
        self.menu.addAction(self.delete_menu_action)

        if self.is_selected() == 0:
            self.copy_menu_action.setEnabled(False)
            self.delete_menu_action.setEnabled(False)

        self.copy_menu_action.triggered.connect(self.copy)
        self.delete_menu_action.triggered.connect(lambda :c_ewwsrw.delete_current_row(self))

        self.menu.exec(self.word_seg_result_table.mapToGlobal(pos))

    # 选中项监测
    def is_selected(self):
        select_num = self.word_seg_result_table.selectedIndexes()
        if not select_num:
            return 0
        else:
            return int(len(select_num) / 3)

    # 用户点击窗口关闭时触发方法
    def on_close(self):
        self.main_window.menu.word_seg_result_widget = None # 将menu的widget清零
        with QSignalBlocker(self.main_window.menu.edit_seg_result_action):
            self.main_window.menu.edit_seg_result_action.setChecked(False)

    # 自定义窗口关闭方法
    def custom_close_event(self, event):
        if self.saved:
            event.accept()
            return

        reply = QMessageBox.question(self.word_seg_result_widget, "确认", "是否关闭窗口？未保存的更改将丢失。", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            with QSignalBlocker(self.menu_action):
                self.menu_action.setChecked(True)

    # 复制方法
    def copy(self):
        self.word_seg_result_table.copy_rows_as_custom_string()