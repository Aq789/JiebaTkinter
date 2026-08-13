# 菜单栏
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMenu, QApplication

import app.controllers.menu as c_m
from app import get_icon


class Menu:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window
        self.menubar = self.main_window.window.menuBar()

        self.style = QApplication.style()
        self.word_seg_result_widget = None
        self.word_dic_widget = None
        self.check_widget = None

        # 菜单栏项
        self.file_menu = self.menubar.addMenu("文件(&F)")
        self.edit_menu = self.menubar.addMenu("编辑(&E)")
        self.check_menu = self.menubar.addMenu("查看(&V)")
        self.settings_menu = self.menubar.addMenu("设置(&S)")
        self.help_menu = self.menubar.addMenu("帮助(&H)")

        # 文件项
        self.new_action = QAction("新建", self.window)
        self.new_action.setShortcut(QKeySequence("Ctrl+N"))
        self.new_action.setIcon(get_icon("new_action.svg"))
        self.new_action.icon_name = "new_action.svg"

        self.open_action = QAction("打开", self.window)
        self.open_action.setShortcut(QKeySequence("Ctrl+O"))
        self.open_action.setIcon(get_icon("open_action.svg"))
        self.open_action.icon_name = "open_action.svg"

        self.save_action = QAction("保存", self.window)
        self.save_action.setShortcut(QKeySequence("Ctrl+S"))
        self.save_action.setIcon(get_icon("save_action.svg"))
        self.save_action.icon_name = "save_action.svg"

        self.other_save_action = QAction("另存为", self.window)
        self.other_save_action.setShortcut(QKeySequence("Ctrl+Shift+S"))

        self.input_menu = QMenu("导入...")
        self.input_text_action = QAction("导入文本文件(&T)")
        self.input_dic_action = QAction("导入词典文件(&D)")

        self.output_menu = QMenu("导出...")
        self.output_text_action = QAction("导出文本文件(&T)")
        self.output_seg_result_action = QAction("导出分词结果(&S)")
        self.output_dic_action = QAction("导出自定义词典(&D)")

        self.exit_action = QAction("退出(&X)")
        self.exit_action.setIcon(get_icon("exit_action.svg"))
        self.exit_action.icon_name = "exit_action.svg"

        # 编辑项
        self.undo_action = QAction("撤销", self.window)
        self.undo_action.setShortcut(QKeySequence("Ctrl+Z"))
        self.undo_action.setIcon(get_icon("undo_action.svg"))
        self.undo_action.icon_name = "undo_action.svg"

        self.redo_action = QAction("恢复", self.window)
        self.redo_action.setShortcut(QKeySequence("Ctrl+Shift+Z"))
        self.redo_action.setIcon(get_icon("redo_action.svg"))
        self.redo_action.icon_name = "redo_action.svg"

        self.copy_action = QAction("复制", self.window)
        self.copy_action.setShortcut(QKeySequence("Ctrl+C"))
        self.copy_action.setIcon(get_icon("copy_action.svg"))
        self.copy_action.icon_name = "copy_action.svg"

        self.cut_action = QAction("剪切", self.window)
        self.cut_action.setShortcut(QKeySequence("Ctrl+X"))
        self.cut_action.setIcon(get_icon("cut_action.svg"))
        self.cut_action.icon_name = "cut_action.svg"

        self.paste_action = QAction("粘贴", self.window)
        self.paste_action.setShortcut(QKeySequence("Ctrl+V"))
        self.paste_action.setIcon(get_icon("paste_action.svg"))
        self.paste_action.icon_name = "paste_action.svg"

        self.find_action = QAction("查找", self.window)
        self.find_action.setShortcut(QKeySequence("Ctrl+F"))
        self.find_action.setIcon(get_icon("check_action.svg"))
        self.find_action.icon_name = "check_action.svg"

        self.edit_seg_result_action = QAction("编辑分词结果", self.window)
        self.edit_seg_result_action.setShortcut(QKeySequence("Shift+F1"))
        self.edit_seg_result_action.setIcon(get_icon("null_action.svg"))
        self.edit_seg_result_action.icon_name = "null_action.svg"
        self.edit_seg_result_action.checked = False

        self.edit_dic_action = QAction("编辑词典", self.window)
        self.edit_dic_action.setShortcut(QKeySequence("Shift+F2"))
        self.edit_dic_action.setIcon(get_icon("null_action.svg"))
        self.edit_dic_action.icon_name = "null_action.svg"
        self.edit_dic_action.checked = False

        self.start_menu = QMenu("开始分词", self.window)
        self.start_menu.setIcon(get_icon("start_action.svg"))
        self.start_menu.icon_name = "start_action.svg"
        self.start_seg_action = QAction("所有文本")
        self.start_seg_action.setShortcut(QKeySequence("Shift+F3"))
        self.start_seg_part_action = QAction("仅选中文本")
        self.start_seg_part_action.setShortcut(QKeySequence("Shift+F4"))

        # 查看项
        self.status_bar_hidden_action = QAction("隐藏状态栏", self.window)
        self.status_bar_hidden_action.setCheckable(True)
        self.preview_window_hidden_action = QAction("隐藏预览窗口", self.window)
        self.preview_window_hidden_action.setCheckable(True)
        self.auto_enter_action = QAction("自动换行", self.window)
        self.auto_enter_action.setCheckable(True)
        self.auto_enter_action.setChecked(True)
        self.statistic_action = QAction("统计(&S)", self.window)

        # 设置项
        self.settings_action = QAction("全局设置", self.window)
        self.settings_action.setShortcut(QKeySequence("Shift+F5"))
        self.settings_action.setIcon(get_icon("settings_action.svg"))
        self.settings_action.icon_name = "settings_action.svg"

        # 帮助项
        self.welcome_action = QAction("欢迎", self.window)
        self.help_action = QAction("帮助(&H)", self.window)
        self.help_action.setIcon(get_icon("help_action.svg"))
        self.help_action.icon_name = "help_action.svg"
        self.about_action = QAction("关于...(&A)", self.window)

        # 开始创建
        self.file_menu.addAction(self.new_action)
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.other_save_action)
        self.file_menu.addSeparator()
        self.file_menu.addMenu(self.input_menu)
        self.input_menu.addAction(self.input_text_action)
        self.input_menu.addAction(self.input_dic_action)
        self.file_menu.addMenu(self.output_menu)
        self.output_menu.addAction(self.output_text_action)
        self.output_menu.addAction(self.output_seg_result_action)
        self.output_menu.addAction(self.output_dic_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.exit_action)
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
        self.edit_menu.addMenu(self.start_menu)
        self.start_menu.addAction(self.start_seg_action)
        self.start_menu.addAction(self.start_seg_part_action)
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
        self.start_seg_part_action.triggered.connect(lambda :c_m.start_part_menu(self))
        self.auto_enter_action.toggled.connect(lambda :c_m.auto_enter(self))
        self.edit_seg_result_action.triggered.connect(lambda checked :c_m.word_seg_result_widget(self))
        self.edit_dic_action.triggered.connect(lambda checked :c_m.word_dic_widget(self))
        self.statistic_action.triggered.connect(lambda :c_m.create_statistic_widget(self))
        self.status_bar_hidden_action.toggled.connect(lambda :c_m.toggle_statusbar(self))
        self.preview_window_hidden_action.toggled.connect(lambda checked :c_m.on_checkbox_toggled(self, checked))
        self.copy_action.triggered.connect(lambda :c_m.on_copy(self))
        self.cut_action.triggered.connect(lambda :c_m.on_cut(self))
        self.paste_action.triggered.connect(lambda :c_m.on_paste(self))
        self.find_action.triggered.connect(lambda :c_m.check_widget(self))
        self.undo_action.triggered.connect(lambda :c_m.undo(self))
        self.redo_action.triggered.connect(lambda :c_m.redo(self))
        self.save_action.triggered.connect(lambda :c_m.save(self))
        self.other_save_action.triggered.connect(lambda :c_m.other_save(self))
        self.open_action.triggered.connect(lambda :c_m.open_file(self))
        self.new_action.triggered.connect(lambda :c_m.new_file(self))
        self.input_text_action.triggered.connect(lambda :c_m.input_text_file(self))
        self.input_dic_action.triggered.connect(lambda :c_m.input_dic_file(self))
        self.output_text_action.triggered.connect(lambda :c_m.output_text_file(self))
        self.output_seg_result_action.triggered.connect(lambda :c_m.output_seg_result_file(self))
        self.output_dic_action.triggered.connect(lambda :c_m.output_dic_file(self))
        self.about_action.triggered.connect(lambda :c_m.create_about_widget(self))
        self.help_action.triggered.connect(lambda :c_m.help_menu(self))
        self.exit_action.triggered.connect(lambda :c_m.exit_action(self))