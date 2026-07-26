# 菜单栏
from PySide6.QtGui import QAction

import app.controllers_s.menu as c_m

class Menu:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window
        self.menubar = self.main_window.window.menuBar()

        self.word_seg_result_widget = None
        self.word_dic_widget = None

        # 菜单栏项
        self.file_menu = self.menubar.addMenu("文件(&F)")
        self.edit_menu = self.menubar.addMenu("编辑(&E)")
        self.check_menu = self.menubar.addMenu("查看(&V)")
        self.settings_menu = self.menubar.addMenu("设置(&S)")
        self.help_menu = self.menubar.addMenu("帮助(&H)")

        # 文件项
        self.new_action = QAction("新建", self.window)
        self.open_action = QAction("打开", self.window)
        self.save_action = QAction("保存", self.window)
        self.other_save_action = QAction("另存为", self.window)

        # 编辑项
        self.undo_action = QAction("撤销", self.window)
        self.redo_action = QAction("恢复", self.window)
        self.copy_action = QAction("复制", self.window)
        self.cut_action = QAction("剪切", self.window)
        self.paste_action = QAction("粘贴", self.window)
        self.find_action = QAction("查找", self.window)
        self.edit_seg_result_action = QAction("编辑分词结果", self.window)
        self.edit_seg_result_action.setCheckable(True)
        self.edit_seg_result_action.setChecked(False)
        self.edit_dic_action = QAction("编辑词典", self.window)
        self.edit_dic_action.setCheckable(True)
        self.edit_dic_action.setChecked(False)
        self.start_seg_action = QAction("开始分词", self.window)

        # 查看项
        self.status_bar_hidden_action = QAction("隐藏状态栏", self.window)
        self.status_bar_hidden_action.setCheckable(True)
        self.preview_window_hidden_action = QAction("隐藏预览窗口", self.window)
        self.preview_window_hidden_action.setCheckable(True)
        self.auto_enter_action = QAction("自动换行", self.window)
        self.auto_enter_action.setCheckable(True)
        self.auto_enter_action.setChecked(True)
        self.statistic_action = QAction("统计", self.window)

        # 设置项
        self.settings_action = QAction("全局设置", self.window)

        # 帮助项
        self.welcome_action = QAction("欢迎", self.window)
        self.help_action = QAction("帮助", self.window)
        self.about_action = QAction("关于...", self.window)

        # 开始创建
        self.file_menu.addAction(self.new_action)
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.other_save_action)
        self.file_menu.addSeparator()
        self.edit_menu.addAction(self.undo_action)
        self.edit_menu.addAction(self.redo_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.copy_action)
        self.edit_menu.addAction(self.cut_action)
        self.edit_menu.addAction(self.paste_action)
        self.edit_menu.addAction(self.find_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.edit_seg_result_action)
        self.edit_menu.addAction(self.edit_dic_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.start_seg_action)
        self.check_menu.addAction(self.status_bar_hidden_action)
        self.check_menu.addAction(self.preview_window_hidden_action)
        self.check_menu.addAction(self.auto_enter_action)
        self.check_menu.addAction(self.statistic_action)
        self.settings_menu.addAction(self.settings_action)
        self.help_menu.addAction(self.welcome_action)
        self.help_menu.addSeparator()
        self.help_menu.addAction(self.help_action)
        self.help_menu.addAction(self.about_action)

        # 绑定信号槽
        self.settings_action.triggered.connect(lambda :c_m.create_settings_widget(self))
        self.start_seg_action.triggered.connect(lambda :c_m.start_menu(self))
        self.auto_enter_action.toggled.connect(lambda :c_m.auto_enter(self))
        self.edit_seg_result_action.toggled.connect(lambda checked :c_m.word_seg_result_widget(self, checked))
        self.edit_dic_action.toggled.connect(lambda checked :c_m.word_dic_widget(self, checked))
        self.statistic_action.triggered.connect(lambda :c_m.create_statistic_widget(self))
        self.status_bar_hidden_action.toggled.connect(lambda :c_m.toggle_statusbar(self))
        self.preview_window_hidden_action.toggled.connect(lambda checked :c_m.on_checkbox_toggled(self, checked))
