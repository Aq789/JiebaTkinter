# 文本框控制器
from PySide6.QtWidgets import QPlainTextEdit

import app.controllers_s.preview_window as c_pw
import app.controllers_s.edit_widget.word_seg_result_widget as c_ewwsrw
import app.service.jieba.start as s_js


# 将文本上传至数据集
def text_to_data(central_widget):
    central_widget.main_window.text_datas.set_text_data(central_widget.text_edit.toPlainText())

# 开始分词控制器
def start_seg_word(central_widget):
    word_seg_result_widget = central_widget.main_window.menu.word_seg_result_widget
    seg_settings_datas = central_widget.main_window.seg_settings_datas
    text_datas = central_widget.main_window.text_datas
    word_dic_datas = central_widget.main_window.word_dic_datas
    word_seg_result_datas = central_widget.main_window.word_seg_result_datas

    text_to_data(central_widget) # 将文本上传至数据集
    s_js.start(seg_settings_datas, text_datas, word_dic_datas, word_seg_result_datas) # 开始分词
    c_pw.input_seg_result_data(central_widget.main_window.dock_widget.preview_window)
    if word_seg_result_widget is not None:
        c_ewwsrw.input_seg_result_data(word_seg_result_widget)

# 开启自动换行
def open_auto_enter(central_widget):
    central_widget.text_edit.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)

# 关闭自动换行
def close_auto_enter(central_widget):
    central_widget.text_edit.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)