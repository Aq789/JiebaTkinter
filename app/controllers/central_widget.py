# 文本框控制器
import time

from PySide6.QtWidgets import QPlainTextEdit, QMessageBox

import app.controllers.edit_widget.word_seg_result_widget as c_ewwsrw
import app.controllers.preview_window as c_pw
import app.service.jieba.start as s_js
from app.datas.text import Text


# 将文本上传至数据集
def text_to_data(central_widget):
    central_widget.main_window.text_datas.set_text_data(central_widget.text_edit.toPlainText())

# 从数据集中加载文本
def data_to_text(central_widget):
    data = central_widget.main_window.text_datas.get_text_data()
    central_widget.text_edit.setPlainText(data)

# 开始分词控制器
def start_seg_word(central_widget, state=True):
    status_bar = central_widget.main_window.status_widget
    word_seg_result_widget = central_widget.main_window.menu.word_seg_result_widget
    seg_settings_datas = central_widget.main_window.seg_settings_datas
    text_datas = central_widget.main_window.text_datas
    word_dic_datas = central_widget.main_window.word_dic_datas
    word_seg_result_datas = central_widget.main_window.word_seg_result_datas

    if state:
        word_seg_result_datas.delete_all_word_seg_result()
        text_to_data(central_widget) # 将文本上传至数据集
    else:
        text_datas = Text(central_widget.main_window)
        text_datas.set_text_data(central_widget.is_selected())
        if len(word_seg_result_datas.return_word_seg_result_list()) != 0:
            reply = QMessageBox.question(central_widget.main_window.window, "导入词典", "当前词典尚有条目，是否覆盖？", QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)  # 询问用户要不要覆盖
            if reply == QMessageBox.StandardButton.Ok:  # 如果用户选覆盖
                word_seg_result_datas.delete_all_word_seg_result()
            else:
                status_bar.set_message_status(f"取消分词")
                return

    start_time = time.perf_counter()
    s_js.start(seg_settings_datas, text_datas, word_dic_datas, word_seg_result_datas) # 开始分词
    c_pw.input_seg_result_data(central_widget.main_window.dock_widget.preview_window)
    if word_seg_result_widget is not None:
        c_ewwsrw.input_seg_result_data(word_seg_result_widget)
    central_widget.main_window.change_saved(False)
    end_time = time.perf_counter()

    total_time = (end_time - start_time) * 1000
    status_bar.set_ready_status(f"分词完成，耗时 {total_time:.1f} ms")

# 开启自动换行
def open_auto_enter(central_widget):
    central_widget.text_edit.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)

# 关闭自动换行
def close_auto_enter(central_widget):
    central_widget.text_edit.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

# 在预览窗口中显示
def show_selected_search(central_widget, state):
    preview_window = central_widget.main_window.dock_widget.preview_window
    if state:
        table = preview_window.seg_result_table
    else:
        table = preview_window.dic_table
    text = central_widget.is_selected()
    if text != "":
        c_pw.search_datas(table, text)
    else:
        c_pw.search_datas(table, "")
        return