# 侧边栏——预览窗口
from PySide6.QtWidgets import QTabWidget, QTableWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHeaderView


class PreviewWindow:
    def __init__(self, main_window, dock_widget):
        self.main_window = main_window
        self.dock_widget = dock_widget
        self.window = self.main_window.window

        self.preview_window = QWidget(self.dock_widget) # 创建左侧预览窗口

        self.tab_widget = QTabWidget(self.preview_window)  # 创建标签页
        self.preview_window_layout = QVBoxLayout()
        self.preview_window_layout.setContentsMargins(5, 0, 5, 0)
        self.preview_window_layout.setSpacing(0)
        self.preview_window_layout.addWidget(self.tab_widget)

        # 分词结果标签
        self.seg_result_tab = QWidget()
        self.tab_widget.addTab(self.seg_result_tab, "分词结果")
        self.seg_result_layout = QVBoxLayout()

        self.seg_result_table = QTableWidget(self.seg_result_tab) # 创建表
        self.seg_result_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 设为只读
        self.seg_result_table.setSortingEnabled(True) # 可排序
        self.seg_result_table.setColumnCount(3) # 设置列数
        self.seg_result_table.setHorizontalHeaderLabels(["词名", "词频", "词性"]) # 设置表头
        self.seg_result_header = self.seg_result_table.horizontalHeader() # 表头拉伸
        self.seg_result_header.setSectionResizeMode(0, QHeaderView.Stretch) # 填充剩余空间
        self.seg_result_header.setSectionResizeMode(1, QHeaderView.ResizeToContents) # 自适应内容宽度
        self.seg_result_header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        self.seg_result_layout.addWidget(self.seg_result_table) # 将表添加至标签页中
        self.seg_result_layout.setContentsMargins(2, 2, 2, 2) # 控制间距为0
        self.seg_result_tab.setLayout(self.seg_result_layout)

        # 词典标签
        self.dic_tab = QWidget()
        self.tab_widget.addTab(self.dic_tab, "词典")
        self.dic_layout = QVBoxLayout()

        self.dic_table = QTableWidget(self.dic_tab) # 创建表
        self.dic_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 设为只读
        self.dic_table.setColumnCount(3) # 设置列数
        self.dic_table.setHorizontalHeaderLabels(["词名", "词频", "词性"]) # 设置表头
        self.dic_header = self.dic_table.horizontalHeader() # 表头拉伸
        self.dic_header.setSectionResizeMode(0, QHeaderView.Stretch) # 填充剩余空间
        self.dic_header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.dic_header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        self.dic_layout.addWidget(self.dic_table) # 将表添加至标签页中
        self.dic_layout.setContentsMargins(2, 2, 2, 2) # 控制间距为0
        self.dic_tab.setLayout(self.dic_layout)

        self.dock_widget.setWidget(self.preview_window)

        self.preview_window.setLayout(self.preview_window_layout)