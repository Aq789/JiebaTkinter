# 编辑词典窗口
from PySide6.QtCore import Qt, QSignalBlocker
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QHeaderView, QLabel, QMessageBox, \
    QAbstractItemView, QMenu

import app.controllers.edit_widget.word_dic_widget as c_ewwdw
import app.controllers.menu as c_m
from app import get_icon, get_style
from app.service.pyside6.int_with_validation_delegate import IntWithValidationDelegate
from app.service.pyside6.string_non_empty_delegate import StringNonEmptyDelegate
from app.service.pyside6.table_widget import CustomTable


class WordDicWidget:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window
        self.saved = True
        self.word_dic_widget = QMainWindow(self.window)
        self.word_dic_widget.setWindowTitle("编辑词典")
        self.word_dic_widget.setMinimumSize(400, 450)
        self.word_dic_widget.setAttribute(Qt.WA_DeleteOnClose)

        self.toolbar = self.word_dic_widget.addToolBar("主工具栏")
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.new_action = QAction("新建", self.word_dic_widget)
        self.new_action.setShortcut(QKeySequence("Ctrl+N"))
        self.new_action.setToolTip("新建 Ctrl+N")
        self.new_action.setStatusTip("新建词典项")
        self.new_action.setIcon(get_icon("new_action_1.svg"))
        self.new_action.icon_name = "new_action_1.svg"

        self.delete_action = QAction("删除", self.word_dic_widget)
        self.delete_action.setShortcut(QKeySequence("Delete"))
        self.delete_action.setToolTip("删除 Delete")
        self.delete_action.setStatusTip("删除部分词典项")
        self.delete_action.setIcon(get_icon("delete_action.svg"))
        self.delete_action.icon_name = "delete_action.svg"

        self.copy_action = QAction("复制", self.word_dic_widget)
        self.copy_action.setShortcut(QKeySequence("Ctrl+C"))
        self.copy_action.setToolTip("复制 Ctrl+C")
        self.copy_action.setStatusTip("复制所选表格内容到剪贴板")
        self.copy_action.setIcon(get_icon("copy_action.svg"))
        self.copy_action.icon_name = "copy_action.svg"

        self.cut_action = QAction("剪切", self.word_dic_widget)
        self.cut_action.setShortcut(QKeySequence("Ctrl+X"))
        self.cut_action.setToolTip("剪切 Ctrl+X")
        self.cut_action.setStatusTip("剪切所选表格内容到剪贴板")
        self.cut_action.setIcon(get_icon("cut_action.svg"))
        self.cut_action.icon_name = "cut_action.svg"

        self.paste_action = QAction("粘贴", self.word_dic_widget)
        self.paste_action.setShortcut(QKeySequence("Ctrl+V"))
        self.paste_action.setToolTip("粘贴 Ctrl+V")
        self.paste_action.setStatusTip("粘贴剪贴板内容到表格（需对应格式）")
        self.paste_action.setIcon(get_icon("paste_action.svg"))
        self.paste_action.icon_name = "paste_action.svg"

        self.check_action = QAction("查找", self.word_dic_widget)
        self.check_action.setShortcut(QKeySequence("Ctrl+F"))
        self.check_action.setToolTip("查找 Ctrl+F")
        self.check_action.setCheckable(True)
        self.check_action.setStatusTip("通过关键信息查找词典项")
        self.check_action.setIcon(get_icon("check_action.svg"))
        self.check_action.icon_name = "check_action.svg"

        self.save_action = QAction("保存", self.word_dic_widget)
        self.save_action.setShortcut(QKeySequence("Ctrl+S"))
        self.save_action.setToolTip("保存 Ctrl+S")
        self.save_action.setStatusTip("保存修改后的词典")
        self.save_action.setIcon(get_icon("save_action.svg"))
        self.save_action.icon_name = "save_action.svg"

        self.toolbar.addAction(self.new_action)
        self.toolbar.addAction(self.delete_action)
        self.toolbar.addAction(self.check_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.copy_action)
        self.toolbar.addAction(self.cut_action)
        self.toolbar.addAction(self.paste_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.save_action)

        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout()
        self.word_dic_table = CustomTable(self.word_dic_widget, 3)
        self.word_dic_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.word_dic_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.word_dic_table.setSortingEnabled(True)
        self.word_dic_table.setColumnCount(3)

        delegate = IntWithValidationDelegate(self.word_dic_table, min_val=0, max_val=9999)
        self.word_dic_table.setItemDelegateForColumn(1, delegate)

        delegate_nonempty = StringNonEmptyDelegate()
        self.word_dic_table.setItemDelegateForColumn(0, delegate_nonempty)

        self.word_dic_table.setHorizontalHeaderLabels(["词名", "词频", "词性"])
        self.word_dic_header = self.word_dic_table.horizontalHeader()
        self.word_dic_header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.word_dic_header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.word_dic_header.setSectionResizeMode(2, QHeaderView.Stretch)
        self.central_layout.addWidget(self.word_dic_table)
        self.central_widget.setLayout(self.central_layout)
        self.word_dic_widget.setCentralWidget(self.central_widget)

        self.state_label = QLabel("总计 项")
        self.state_label.setContentsMargins(5, 1, 5, 1)
        self.save_state = QLabel("已保存")
        self.save_state.setContentsMargins(5, 1, 5, 1)
        self.word_dic_widget.statusBar().addWidget(self.state_label)
        self.word_dic_widget.statusBar().addWidget(self.save_state)

        c_ewwdw.input_dic_data(self)

        self.menu_action = self.main_window.menu.edit_dic_action

        self.word_dic_widget.closeEvent = self.custom_close_event

        # 信号槽
        self.word_dic_widget.destroyed.connect(self.on_close)
        self.delete_action.triggered.connect(lambda :c_ewwdw.delete_current_row(self))
        self.check_action.toggled.connect(lambda :c_ewwdw.check_datas(self))
        self.save_action.triggered.connect(lambda :c_ewwdw.output_dic_data(self))
        self.word_dic_table.horizontalHeader().sortIndicatorChanged.connect(lambda :c_ewwdw.save_refresh(self, False))
        self.word_dic_table.itemSelectionChanged.connect(lambda :c_ewwdw.status_refresh(self))
        self.word_dic_table.cellChanged.connect(lambda :c_ewwdw.save_refresh(self, False))
        self.new_action.triggered.connect(lambda :c_ewwdw.create_dic_data(self))
        self.copy_action.triggered.connect(self.copy)
        self.paste_action.triggered.connect(self.paste)
        self.cut_action.triggered.connect(self.cut)
        self.word_dic_table.customContextMenuRequested.connect(self.menu)

        # 表格样式
        self.word_dic_table.setStyleSheet(get_style("table.qss"))

        self.word_dic_widget.show()

    # 右键菜单
    def menu(self, pos):
        self.menu = QMenu()
        self.new_menu_action = QAction("新建")
        self.new_menu_action.setShortcut(QKeySequence("Ctrl+N"))
        self.new_menu_action.setIcon(get_icon("new_action_1.svg"))
        self.new_menu_action.icon_name = "new_action_1.svg"

        self.delete_menu_action = QAction("删除")
        self.delete_menu_action.setShortcut(QKeySequence("Delete"))
        self.delete_menu_action.setIcon(get_icon("delete_action.svg"))
        self.delete_menu_action.icon_name = "delete_action.svg"

        self.copy_menu_action = QAction("复制")
        self.copy_menu_action.setShortcut(QKeySequence("Ctrl+C"))
        self.copy_menu_action.setIcon(get_icon("copy_action.svg"))
        self.copy_menu_action.icon_name = "copy_action.svg"

        self.cut_menu_action = QAction("剪切")
        self.cut_menu_action.setShortcut(QKeySequence("Ctrl+X"))
        self.cut_menu_action.setIcon(get_icon("cut_action.svg"))
        self.cut_menu_action.icon_name = "cut_action.svg"

        self.paste_menu_action = QAction("粘贴")
        self.paste_menu_action.setShortcut(QKeySequence("Ctrl+V"))
        self.paste_menu_action.setIcon(get_icon("paste_action.svg"))
        self.paste_menu_action.icon_name = "paste_action.svg"

        self.menu.addAction(self.new_menu_action)
        self.menu.addAction(self.delete_menu_action)
        self.menu.addSeparator()
        self.menu.addAction(self.copy_menu_action)
        self.menu.addAction(self.cut_menu_action)
        self.menu.addAction(self.paste_menu_action)

        if self.is_selected() == 0:
            self.copy_menu_action.setEnabled(False)
            self.cut_menu_action.setEnabled(False)
            self.delete_menu_action.setEnabled(False)

        self.new_menu_action.triggered.connect(lambda: c_ewwdw.create_dic_data(self))
        self.copy_menu_action.triggered.connect(self.copy)
        self.paste_menu_action.triggered.connect(self.paste)
        self.cut_menu_action.triggered.connect(self.cut)
        self.delete_menu_action.triggered.connect(lambda: c_ewwdw.delete_current_row(self))

        self.menu.exec(self.word_dic_table.mapToGlobal(pos))

    # 刷新样式表
    def refresh_style(self):
        style = get_style("table.qss")
        self.word_dic_table.setStyleSheet(style)

    # 选中项监测
    def is_selected(self):
        select_num = self.word_dic_table.selectedIndexes()
        if not select_num:
            return 0
        else:
            return int(len(select_num) / 3)

    # 用户点击窗口关闭时触发方法
    def on_close(self):
        self.main_window.menu.word_dic_widget = None
        with QSignalBlocker(self.main_window.menu.edit_dic_action):
            self.main_window.menu.edit_dic_action.checked = True
            c_m.word_dic_widget(self.main_window.menu)

    # 自定义窗口关闭方法
    def custom_close_event(self, event):
        if self.saved:
            event.accept()
            return

        reply = QMessageBox.question(self.word_dic_widget, "确认", "是否关闭窗口？未保存的更改将丢失。", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            with QSignalBlocker(self.menu_action):
                self.menu_action.setChecked(True)

    # 复制方法
    def copy(self):
        self.word_dic_table.copy_rows_as_custom_string()

    # 粘贴方法
    def paste(self):
        if self.word_dic_table.paste_rows_as_custom_string():
            return
        else:
            QMessageBox.warning(self.word_dic_widget, "提示", "粘贴失败，请检查词典格式后重试！")

    # 剪切方法
    def cut(self):
        self.word_dic_table.cut_rows_as_custom_string()