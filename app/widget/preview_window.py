# 侧边栏——预览窗口
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QTabWidget, QTableWidget, QAbstractItemView, QMenu, QMessageBox
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHeaderView
from PySide6.QtCore import Qt

from app.service.pyside6.table_widget import CustomTable
import app.controllers.menu as c_m

class PreviewWindow:
    def __init__(self, main_window, dock_widget):
        self.main_window = main_window
        self.dock_widget = dock_widget
        self.window = self.main_window.window

        self.preview_window = QWidget(self.dock_widget) # 创建左侧预览窗口

        self.tab_widget = QTabWidget(self.preview_window)  # 创建标签页
        self.preview_window_layout = QVBoxLayout()
        self.preview_window_layout.setContentsMargins(8, 5, 8, 5)
        self.preview_window_layout.setSpacing(0)
        self.preview_window_layout.addWidget(self.tab_widget)

        # 分词结果标签
        self.seg_result_tab = QWidget()
        self.tab_widget.addTab(self.seg_result_tab, "分词结果")
        self.seg_result_layout = QVBoxLayout()

        self.seg_result_table = CustomTable(self.seg_result_tab, 3) # 创建表
        self.seg_result_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.seg_result_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 设为只读
        self.seg_result_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.seg_result_table.setSortingEnabled(True) # 可排序
        self.seg_result_table.setColumnCount(3) # 设置列数
        self.seg_result_table.setHorizontalHeaderLabels(["词名", "词频", "词性"]) # 设置表头
        self.seg_result_header = self.seg_result_table.horizontalHeader() # 表头拉伸
        self.seg_result_header.setSectionResizeMode(0, QHeaderView.Stretch) # 填充剩余空间
        self.seg_result_header.setSectionResizeMode(1, QHeaderView.ResizeToContents) # 自适应内容宽度
        self.seg_result_header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        self.seg_result_layout.addWidget(self.seg_result_table) # 将表添加至标签页中
        self.seg_result_layout.setContentsMargins(5, 5, 5, 5) # 控制间距为0
        self.seg_result_tab.setLayout(self.seg_result_layout)

        # 词典标签
        self.dic_tab = QWidget()
        self.tab_widget.addTab(self.dic_tab, "词典")
        self.dic_layout = QVBoxLayout()

        self.dic_table = CustomTable(self.dic_tab, 3) # 创建表
        self.dic_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.dic_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 设为只读
        self.dic_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.dic_table.setSortingEnabled(True) # 可排序
        self.dic_table.setColumnCount(3) # 设置列数
        self.dic_table.setHorizontalHeaderLabels(["词名", "词频", "词性"]) # 设置表头
        self.dic_header = self.dic_table.horizontalHeader() # 表头拉伸
        self.dic_header.setSectionResizeMode(0, QHeaderView.Stretch) # 填充剩余空间
        self.dic_header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.dic_header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        self.dic_layout.addWidget(self.dic_table) # 将表添加至标签页中
        self.dic_layout.setContentsMargins(5, 5, 5, 5) # 控制间距为0
        self.dic_tab.setLayout(self.dic_layout)

        self.dock_widget.setWidget(self.preview_window)

        self.preview_window.setLayout(self.preview_window_layout)

        # 表格样式
        self.seg_result_table.setStyleSheet(
            """
                QTableWidget::item:selected {
                    background-color: palette(highlight);
                    color: palette(highlighted-text);
                }
            """
        )
        # 表格样式
        self.dic_table.setStyleSheet(
            """
                QTableWidget::item:selected {
                    background-color: palette(highlight);
                    color: palette(highlighted-text);
                }
            """
        )

        # 信号槽
        self.seg_result_table.customContextMenuRequested.connect(self.seg_result_menu)
        self.dic_table.customContextMenuRequested.connect(self.dic_menu)

        """右键菜单"""
        self.seg_result_copy_action = QAction("复制到剪贴板", self.main_window.window)
        self.seg_result_copy_action.setShortcut(QKeySequence("Ctrl+Shift+C"))
        self.seg_result_copy_action.setShortcutContext(Qt.ApplicationShortcut)
        self.seg_result_check_action = QAction("在文中查找", self.main_window.window)
        self.seg_result_check_action.setShortcut(QKeySequence("Ctrl+Shift+F"))
        self.seg_result_check_action.setShortcutContext(Qt.ApplicationShortcut)
        self.seg_result_open_widget_action = QAction("编辑分词结果", self.main_window.window)
        self.seg_result_open_widget_action.setShortcut(QKeySequence("Ctrl+Shift+F1"))
        self.seg_result_open_widget_action.setShortcutContext(Qt.ApplicationShortcut)
        self.dic_copy_action = QAction("复制到剪贴板", self.main_window.window)
        self.dic_copy_action.setShortcut(QKeySequence("Ctrl+Shift+C"))
        self.dic_copy_action.setShortcutContext(Qt.ApplicationShortcut)
        self.dic_check_action = QAction("在文中查找", self.main_window.window)
        self.dic_check_action.setShortcut(QKeySequence("Ctrl+Shift+F"))
        self.dic_check_action.setShortcutContext(Qt.ApplicationShortcut)
        self.dic_open_widget_action = QAction("编辑词典", self.main_window.window)
        self.dic_open_widget_action.setShortcut(QKeySequence("Ctrl+Shift+F2"))
        self.dic_open_widget_action.setShortcutContext(Qt.ApplicationShortcut)

        self.main_window.window.addAction(self.seg_result_copy_action)
        self.main_window.window.addAction(self.seg_result_check_action)
        self.main_window.window.addAction(self.seg_result_open_widget_action)
        self.main_window.window.addAction(self.dic_copy_action)
        self.main_window.window.addAction(self.dic_check_action)
        self.main_window.window.addAction(self.dic_open_widget_action)

        self.seg_result_copy_action.triggered.connect(self.seg_result_copy)
        self.seg_result_check_action.triggered.connect(self.seg_result_check)
        self.seg_result_open_widget_action.triggered.connect(self.seg_result_open_widget)
        self.dic_copy_action.triggered.connect(self.dic_copy)
        self.dic_check_action.triggered.connect(self.dic_check)
        self.dic_open_widget_action.triggered.connect(self.dic_open_widget)

        self.seg_result_table.selectionModel().selectionChanged.connect(self._update_seg_actions)
        self.dic_table.selectionModel().selectionChanged.connect(self._update_dic_actions)
        self._update_seg_actions()
        self._update_dic_actions()

    # 右键菜单
    def seg_result_menu(self, pos):
        menu = QMenu()
        menu.addAction(self.seg_result_copy_action)
        menu.addAction(self.seg_result_check_action)
        menu.addAction(self.seg_result_open_widget_action)
        menu.exec(self.seg_result_table.mapToGlobal(pos))

    # 右键菜单
    def dic_menu(self, pos):
        menu = QMenu()
        menu.addAction(self.dic_copy_action)
        menu.addAction(self.dic_check_action)
        menu.addAction(self.dic_open_widget_action)
        menu.exec(self.dic_table.mapToGlobal(pos))

    # 更新函数
    def _update_seg_actions(self):
        enabled = self._is_selected(self.seg_result_table)
        self.seg_result_copy_action.setEnabled(enabled)
        self.seg_result_check_action.setEnabled(enabled)

    def _update_dic_actions(self):
        enabled = self._is_selected(self.dic_table)
        self.dic_copy_action.setEnabled(enabled)
        self.dic_check_action.setEnabled(enabled)

    @staticmethod
    def _is_selected(table):
        return len(table.selectedIndexes()) > 0

    # 复制到剪切板
    def seg_result_copy(self):
        self.seg_result_table.copy_rows_as_custom_string()

    # 复制到剪切板
    def dic_copy(self):
        self.dic_table.copy_rows_as_custom_string()

    # 在文本中查找
    def seg_result_check(self):
        menu = self.main_window.menu
        current_row = self.seg_result_table.currentRow()
        item = self.seg_result_table.item(current_row, 0)
        search_text = item.text()
        if self._is_selected(self.seg_result_table):
            if menu.check_widget is None:
                menu.check_widget = menu.main_window.create_check_widget()
                menu.check_widget.set_check(search_text)
            else:
                menu.check_widget.set_check(search_text)

    # 在文本中查找
    def dic_check(self):
        menu = self.main_window.menu
        current_row = self.dic_table.currentRow()
        item = self.dic_table.item(current_row, 0)
        search_text = item.text()
        if self._is_selected(self.dic_table):
            if menu.check_widget is None:
                menu.check_widget = menu.main_window.create_check_widget()
                menu.check_widget.set_check(search_text)
            else:
                menu.check_widget.set_check(search_text)

    # 编辑分词结果
    def seg_result_open_widget(self):
        menu = self.main_window.menu
        if menu.word_seg_result_widget is not None:
            QMessageBox.warning(self.main_window.window, "提示", "编辑分词结果窗口已打开！")
        else:
            menu.edit_seg_result_action.setChecked(True)

    # 编辑分词结果
    def dic_open_widget(self):
        menu = self.main_window.menu
        if menu.word_dic_widget is not None:
            QMessageBox.warning(self.main_window.window, "提示", "编辑词典窗口已打开！")
        else:
            menu.edit_dic_action.setChecked(True)