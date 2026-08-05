# 导入控制器
from PySide6.QtWidgets import QMessageBox, QFileDialog
import app.service.io.input as s_ii
import app.service.word_dic as s_wd
import app.controllers.preview_window as c_pw
import app.controllers.edit_widget.word_dic_widget as c_ewwdw

# 覆盖自定义对话框
def add_message(window, title, text):
    message = QMessageBox(window)
    message.setWindowTitle(title)
    message.setText(text)
    message.setIcon(QMessageBox.Icon.Question)

    replace_button = message.addButton("覆盖", QMessageBox.ButtonRole.AcceptRole)
    add_button = message.addButton("直接添加", QMessageBox.ButtonRole.DestructiveRole)
    cancel_button = message.addButton("取消", QMessageBox.ButtonRole.RejectRole)

    message.exec()
    clicked_button = message.clickedButton()
    if clicked_button == replace_button:
        return 0
    elif clicked_button == add_button:
        return 1
    elif clicked_button == cancel_button:
        return 2
    else:
        return -1

# 导入文本
def input_text_file(main_window):
    status_widget = main_window.status_widget
    status_widget.set_process_status("正在导入文本文件")

    text_edit = main_window.central_widget.text_edit

    file_path, selected_filter = QFileDialog.getOpenFileName(
        main_window.window,
        "导入",
        "C:/",
        "文本文件 (*.txt);;所有文件 (*.*)"
    )
    if not file_path:
        status_widget.set_message_status("取消导入文本文件")
        return False

    data = s_ii.input_text_file(file_path)
    if data is None:
        QMessageBox.critical(main_window.window, "错误", "文件加载失败！")
        status_widget.set_message_status("导入文本文件失败")
        return False

    text = text_edit.toPlainText()
    if text != "":
        reply = add_message(main_window.window, "导入文本", "当前工作区尚有文本，是否覆盖？")
        if reply == 0:
            text_edit.setPlainText(data)
            status_widget.set_message_status("导入文本文件成功")
            main_window.change_saved(False)
            return True
        elif reply == 1:
            text_edit.setPlainText(text + data)
            status_widget.set_message_status("导入文本文件成功")
            main_window.change_saved(False)
            return True
        else:
            status_widget.set_message_status("取消导入文本文件")
            return False
    else:
        text_edit.setPlainText(data)
        status_widget.set_message_status("导入文本文件成功")
        main_window.change_saved(False)
        return True

# 导入词典
def input_dic_file(main_window):
    # 应用文件
    def apply_file(temp_data, temp_main_window, temp_selected_filter):
        if temp_selected_filter == "词典文件 (*.dic)":
            if s_ii.input_dic_data(temp_data, temp_main_window):  # 检查数据并添加至数据集
                c_pw.input_dic_data(temp_main_window.dock_widget.preview_window)
                if temp_main_window.menu.word_dic_widget is not None:
                    c_ewwdw.input_dic_data(temp_main_window.menu.word_dic_widget)
                status_widget.set_message_status("导入词典文件成功")
                main_window.change_saved(False)
                return True
            else:
                QMessageBox.critical(main_window.window, "错误", "文件加载失败！")
                status_widget.set_message_status("导入词典文件失败")
                return False
        elif temp_selected_filter == "文本文件 (*.txt)":
            if s_ii.input_txt_data(temp_data, temp_main_window):  # 检查数据并添加至数据集
                c_pw.input_dic_data(temp_main_window.dock_widget.preview_window)
                if temp_main_window.menu.word_dic_widget is not None:
                    c_ewwdw.input_dic_data(temp_main_window.menu.word_dic_widget)
                status_widget.set_message_status("导入词典文件成功")
                main_window.change_saved(False)
                return True
            else:
                QMessageBox.critical(main_window.window, "错误", "文件加载失败！")
                status_widget.set_message_status("导入词典文件失败")
                return False
        elif temp_selected_filter == "表格文件 (*.csv)":
            if s_ii.input_csv_data(temp_data, temp_main_window):  # 检查数据并添加至数据集
                c_pw.input_dic_data(temp_main_window.dock_widget.preview_window)
                if temp_main_window.menu.word_dic_widget is not None:
                    c_ewwdw.input_dic_data(temp_main_window.menu.word_dic_widget)
                status_widget.set_message_status("导入词典文件成功")
                main_window.change_saved(False)
                return True
            else:
                QMessageBox.critical(main_window.window, "错误", "文件加载失败！")
                status_widget.set_message_status("导入词典文件失败")
                return False
        else:
            return True

    # 选择类型器
    def select_filter(temp_path, temp_main_window, temp_selected_filter):
        if temp_selected_filter == "词典文件 (*.dic)":
            data = s_ii.input_dic_file(temp_path)  # 从磁盘加载文件并检查
        elif temp_selected_filter == "表格文件 (*.csv)":
            text_data = s_ii.input_csv_file(temp_path)
            data = s_wd.csv_to_dic(text_data)
        else:
            text_data = s_ii.input_text_file(temp_path)
            data = s_wd.txt_to_dic(text_data)

        if data is None:  # 如果检查不通过
            QMessageBox.critical(temp_main_window.window, "错误", "文件加载失败！")
            status_widget.set_message_status("导入词典文件失败")
            return False

        if word_dic_datas.return_len_word_dic_list() != 0:  # 检查通过后，如果数据集中有数据
            reply = add_message(temp_main_window.window, "导入词典", "当前词典尚有条目，是否覆盖？")  # 询问用户要不要覆盖
            if reply == 0:  # 如果用户选覆盖
                word_dic_datas.delete_all_word_dic()  # 删除所有词典
                apply_file(data, temp_main_window, temp_selected_filter)
                return True
            elif reply == 1:
                apply_file(data, temp_main_window, temp_selected_filter)
                return True
            else:
                status_widget.set_message_status("取消导入词典文件")
                return False
        else:
            apply_file(data, temp_main_window, temp_selected_filter)
            return False

    status_widget = main_window.status_widget
    status_widget.set_process_status("正在导入词典文件")

    word_dic_datas = main_window.word_dic_datas

    file_path, selected_filter = QFileDialog.getOpenFileName(
        main_window.window,
        "导入",
        "C:/",
        "词典文件 (*.dic);;文本文件 (*.txt);;表格文件 (*.csv);;所有文件 (*.*)"
    )
    if not file_path:
        status_widget.set_message_status("取消导入词典文件")
        return False

    select_filter(file_path, main_window, selected_filter)
    return True