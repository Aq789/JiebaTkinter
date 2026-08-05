# 导出控制器
from PySide6.QtWidgets import QMessageBox, QFileDialog
import app.service.io.output as s_io

# 导出文本
def output_text_file(main_window):
    status_widget = main_window.status_widget
    status_widget.set_process_status("正在导出文本内容")

    text_edit = main_window.central_widget.text_edit

    file_datas = main_window.file_datas
    if file_datas.get_is_filed_data():
        file_name = f"~/{file_datas.get_file_real_name_data()} 文本"
    else:
        file_name = "~/新建文本文件"

    file_path, selected_filter = QFileDialog.getSaveFileName(
        main_window.window,
        "导出",
        file_name,
        "文本文件 (*.txt);;所有文件 (*.*)"
    )
    if not file_path:
        status_widget.set_message_status("取消导出文本内容")
        return False

    text = text_edit.toPlainText()
    s_io.output_text_file(text, file_path)
    status_widget.set_message_status("导出文本内容成功")
    return True

# 导出分词结果
def output_seg_result_file(main_window):
    status_widget = main_window.status_widget
    status_widget.set_process_status("正在导出分词结果")

    word_seg_result_datas = main_window.word_seg_result_datas

    file_datas = main_window.file_datas
    if file_datas.get_is_filed_data():
        file_name = f"~/{file_datas.get_file_real_name_data()} 分词结果"
    else:
        file_name = "~/新建分词结果文件"

    file_path, selected_filter = QFileDialog.getSaveFileName(
        main_window.window,
        "导出",
        file_name,
        "文本文件 (*.txt);;表格文件 (*.csv);;所有文件 (*.*)"
    )
    if not file_path:
        status_widget.set_message_status("取消导出分词结果")
        return False

    if selected_filter == "文本文件 (*.txt)":
        result = s_io.output_txt_data(word_seg_result_datas.return_word_seg_result_list())
        s_io.output_word_seg_file(result, file_path)
        status_widget.set_message_status("导出分词结果成功")
        return True
    elif selected_filter == "表格文件 (*.csv)":
        result = s_io.output_csv_data(word_seg_result_datas.return_word_seg_result_list())
        s_io.output_word_seg_file(result, file_path)
        status_widget.set_message_status("导出分词结果成功")
        return True
    else:
        result = s_io.output_txt_data(word_seg_result_datas.return_word_seg_result_list())
        s_io.output_word_seg_file(result, file_path)
        status_widget.set_message_status("导出分词结果成功")
        return True

# 导出词典
def output_dic_file(main_window):
    status_widget = main_window.status_widget
    status_widget.set_process_status("正在导出自定义词典")

    word_dic_datas = main_window.word_dic_datas

    file_datas = main_window.file_datas
    if file_datas.get_is_filed_data():
        file_name = f"~/{file_datas.get_file_real_name_data()} 自定义词典"
    else:
        file_name = "~/新建自定义词典文件"

    file_path, selected_filter = QFileDialog.getSaveFileName(
        main_window.window,
        "导出",
        file_name,
        "词典文件 (*.dic);;文本文件 (*.txt);;表格文件 (*.csv);;所有文件 (*.*)"
    )
    if not file_path:
        status_widget.set_message_status("取消导出自定义词典")
        return False

    if selected_filter == "文本文件 (*.txt)":
        result = s_io.output_txt_data(word_dic_datas.return_word_dic_list())
        s_io.output_word_dic_file(result, file_path)
        status_widget.set_message_status("导出自定义词典成功")
        return True
    elif selected_filter == "表格文件 (*.csv)":
        result = s_io.output_csv_data(word_dic_datas.return_word_dic_list())
        s_io.output_word_dic_file(result, file_path)
        status_widget.set_message_status("导出自定义词典成功")
        return True
    elif selected_filter == "词典文件 (*.dic)":
        result = s_io.output_dic_data(word_dic_datas.return_word_dic_list())
        s_io.output_dic_file(result, file_path)
        status_widget.set_message_status("导出自定义词典成功")
        return True
    else:
        result = s_io.output_txt_data(word_dic_datas.return_word_dic_list())
        s_io.output_word_dic_file(result, file_path)
        status_widget.set_message_status("导出自定义词典成功")
        return True