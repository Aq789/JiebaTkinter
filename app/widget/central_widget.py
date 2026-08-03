# 工作区
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPlainTextEdit


class CentralWidget:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window
        self.central_widget = QWidget(self.window)
        self.central_layout = QVBoxLayout()

        self.text_edit = QPlainTextEdit()
        self.central_layout.addWidget(self.text_edit)
        self.central_widget.setLayout(self.central_layout)

        self.window.setCentralWidget(self.central_widget)

        self.init_central_widget()

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

    # 复制方法
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