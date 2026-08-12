# 工作区
from PySide6.QtGui import QFont, QAction, QKeySequence
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPlainTextEdit, QMenu
from PySide6.QtCore import Qt
import app.controllers.central_widget as c_cw
from app import get_icon, ICON_DIR

class CentralWidget:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window
        self.central_widget = QWidget(self.window)
        self.central_layout = QVBoxLayout()

        self.text_edit = QPlainTextEdit()
        self.text_edit.setContextMenuPolicy(Qt.CustomContextMenu)
        self.central_layout.addWidget(self.text_edit)
        self.central_widget.setLayout(self.central_layout)

        self.window.setCentralWidget(self.central_widget)

        self.init_central_widget()

        # 信号槽
        self.text_edit.textChanged.connect(self.text_changed)
        self.text_edit.customContextMenuRequested.connect(self.menu)
        self.text_edit.selectionChanged.connect(self.change_state)

    # 右键菜单
    def menu(self, pos):
        self.text_edit_menu = QMenu()
        self.undo_action = QAction("撤销")
        self.undo_action.setShortcut(QKeySequence("Ctrl+Z"))
        self.undo_action.setIcon(get_icon("undo_action.svg"))
        self.undo_action.icon_name = "undo_action.svg"

        self.redo_action = QAction("恢复")
        self.redo_action.setShortcut(QKeySequence("Ctrl+Shift+Z"))
        self.redo_action.setIcon(get_icon("redo_action.svg"))
        self.redo_action.icon_name = "redo_action.svg"

        self.copy_action = QAction("复制")
        self.copy_action.setShortcut(QKeySequence("Ctrl+C"))
        self.copy_action.setIcon(get_icon("copy_action.svg"))
        self.copy_action.icon_name = "copy_action.svg"

        self.cut_action = QAction("剪切")
        self.cut_action.setShortcut(QKeySequence("Ctrl+X"))
        self.cut_action.setIcon(get_icon("cut_action.svg"))
        self.cut_action.icon_name = "cut_action.svg"

        self.paste_action = QAction("粘贴")
        self.paste_action.setShortcut(QKeySequence("Ctrl+V"))
        self.paste_action.setIcon(get_icon("paste_action.svg"))
        self.paste_action.icon_name = "paste_action.svg"

        self.check_menu = QMenu("查找")
        self.check_seg_result_action = QAction("查找分词结果(&S)")
        self.check_dic_action = QAction("查找词典结果(&D)")
        self.start_menu = QMenu("开始分词")
        self.start_action = QAction("所有文本")
        self.start_action.setShortcut(QKeySequence("Shift+F3"))
        self.start_word_seg = QAction("仅选中文本")
        self.start_word_seg.setShortcut(QKeySequence("Shift+F4"))

        self.text_edit_menu.addAction(self.undo_action)
        self.text_edit_menu.addAction(self.redo_action)
        self.text_edit_menu.addSeparator()
        self.text_edit_menu.addAction(self.copy_action)
        self.text_edit_menu.addAction(self.cut_action)
        self.text_edit_menu.addAction(self.paste_action)
        self.text_edit_menu.addMenu(self.check_menu)
        self.check_menu.addAction(self.check_seg_result_action)
        self.check_menu.addAction(self.check_dic_action)
        self.text_edit_menu.addSeparator()
        self.text_edit_menu.addMenu(self.start_menu)
        self.start_menu.addAction(self.start_action)
        self.start_menu.addAction(self.start_word_seg)

        if self.is_selected() == "":
            self.copy_action.setEnabled(False)
            self.cut_action.setEnabled(False)

        self.undo_action.triggered.connect(self.undo)
        self.redo_action.triggered.connect(self.redo)
        self.copy_action.triggered.connect(self.copy)
        self.cut_action.triggered.connect(self.cut)
        self.paste_action.triggered.connect(self.paste)
        self.check_seg_result_action.triggered.connect(self.check_seg_result)
        self.check_dic_action.triggered.connect(self.check_dic)
        self.start_word_seg.triggered.connect(self.start_part)
        self.start_action.triggered.connect(self.start_all)

        self.text_edit_menu.exec(self.text_edit.mapToGlobal(pos))

    # 初始化工作区方法
    def init_central_widget(self):
        self.change_font()

    # 字体应用函数
    def change_font(self):
        font_settings_datas = self.main_window.font_settings_datas # 传入数据
        font = QFont()
        font.setFamily(font_settings_datas.get_font_data())
        font.setPointSize(font_settings_datas.get_size_data())

        weight, italic = self.shape_font(font_settings_datas.get_shape_data())
        font.setWeight(weight)
        font.setItalic(italic)
        font.setUnderline(font_settings_datas.get_under_line_data())
        font.setStrikeOut(font_settings_datas.get_delete_line_data())

        self.text_edit.setFont(font)

    # 字形处理函数
    @staticmethod
    def shape_font(style):
        style_map = {"常规": (QFont.Normal, False), "粗体": (QFont.Bold, False), "斜体": (QFont.Normal, True), "粗斜体": (QFont.Bold, True)}
        weight, italic = style_map.get(style, (QFont.Normal, False))
        return weight, italic

    # 选中文本监测
    def is_selected(self):
        cursor = self.text_edit.textCursor()
        if cursor.hasSelection():
            return cursor.selectedText()
        else:
            return ""

    # 在分词结果查找菜单状态改变
    def change_state(self):
        if self.is_selected() == "":
            c_cw.show_selected_search(self, True)
            c_cw.show_selected_search(self, False)

    # 文字更改状态函数
    def text_changed(self):
        self.main_window.change_saved(False)

    def copy(self):
        self.text_edit.copy()

    def cut(self):
        self.text_edit.cut()

    def paste(self):
        self.text_edit.paste()

    def undo(self):
        self.text_edit.undo()

    def redo(self):
        self.text_edit.redo()

    def check_seg_result(self):
        preview_window = self.main_window.dock_widget.preview_window
        preview_window.tab_widget.setCurrentIndex(0)
        c_cw.show_selected_search(self, True)

    def check_dic(self):
        preview_window = self.main_window.dock_widget.preview_window
        preview_window.tab_widget.setCurrentIndex(1)
        c_cw.show_selected_search(self, False)

    # 选中部分分词
    def start_part(self):
        c_cw.start_seg_word(self, False)

    def start_all(self):
        c_cw.start_seg_word(self)