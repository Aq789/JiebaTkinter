# 工作区
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit
from PySide6.QtGui import QTextCursor, QTextCharFormat, QFont


class CentralWidget:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window
        self.central_widget = QWidget(self.window)
        self.central_layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        self.text_edit.setAcceptRichText(False)
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
        font = QTextCharFormat() # 构建QTextCharFormat对象
        font.setFontFamily(font_settings_datas.get_font_data())
        font.setFontPointSize(font_settings_datas.get_size_data())
        font.setFontWeight(self.shape_font(font_settings_datas.get_shape_data())[0])
        font.setFontItalic(self.shape_font(font_settings_datas.get_shape_data())[1])
        font.setFontUnderline(font_settings_datas.get_under_line_data())
        font.setFontStrikeOut(font_settings_datas.get_delete_line_data())

        cursor = self.text_edit.textCursor() # 获取当前坐标
        cursor.select(QTextCursor.SelectionType.Document) # 全选
        cursor.setCharFormat(font) # 应用格式
        cursor.clearSelection() # 取消全选
        self.text_edit.setTextCursor(cursor) # 更新光标到编辑器
        cursor = self.text_edit.textCursor() # 重新获取
        cursor.setCharFormat(font) # 设置当前光标格式
        self.text_edit.setTextCursor(cursor) # 更新编辑器光标

    # 字形处理函数
    @staticmethod
    def shape_font(style):
        style_map = {"常规": (QFont.Normal, False), "粗体": (QFont.Bold, False), "斜体": (QFont.Normal, True), "粗斜体": (QFont.Bold, True)}
        weight, italic = style_map.get(style, (QFont.Normal, False))
        return weight, italic