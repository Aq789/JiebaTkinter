# 文件相关控制器
from PySide6.QtWidgets import QFileDialog, QMessageBox

import app.service.io.file as s_if
import app.controllers.central_widget as c_cw
import app.controllers.statistic_widget as c_sw
import app.controllers.preview_window as c_pw
import app.view

# 保存文件
def save_file(main_window):
    status_widget = main_window.status_widget
    status_widget.set_process_status("正在保存文件")

    if not main_window.file_datas.check_is_filed(): # 如果当前没有打开文件
        file_path, selected_filter = QFileDialog.getSaveFileName(
            main_window.window,
            "保存",
            "~/新建分词文件.jbt",
            "分词项目文件 (*.jbt);;所有文件 (*.*)"
        )
        if not file_path:
            status_widget.set_message_status("取消保存文件")
            return False
        main_window.file_datas.set_file_path_data(file_path)

    status_widget.set_process_bar(0)
    c_cw.text_to_data(main_window.central_widget)
    status_widget.set_process_bar(10)
    c_sw.statistic_start_main(main_window)
    status_widget.set_process_bar(20)
    main_window.file_datas.set_is_filed_data(True)
    main_window.file_datas.set_filed_saved_data(True)

    file_dic = s_if.save_to_dic(main_window.word_seg_result_datas,
              main_window.word_dic_datas,
              main_window.text_datas,
              main_window.statistic_datas,
              main_window.file_datas
        )
    status_widget.set_process_bar(50)

    s_if.save_to_file(file_dic, main_window.file_datas.get_file_path_data())
    status_widget.set_process_bar(80)
    main_window.change_saved(True)
    status_widget.set_message_status("保存文件成功")
    return True

# 另存为文件
def other_save_file(main_window):
    status_widget = main_window.status_widget
    status_widget.set_process_status("正在另存为文件")

    file_datas = main_window.file_datas
    if file_datas.get_is_filed_data():
        file_name = f"~/{file_datas.get_file_real_name_data()} - 副本"
    else:
        file_name = "~/新建分词文件"

    file_path, selected_filter = QFileDialog.getSaveFileName(
        main_window.window,
        "另存为",
        file_name,
        "分词项目文件 (*.jbt);;所有文件 (*.*)"
    )
    if not file_path:
        status_widget.set_message_status("取消另存为文件")
        return False
    main_window.file_datas.set_file_path_data(file_path)

    status_widget.set_process_bar(0)
    c_cw.text_to_data(main_window.central_widget)
    status_widget.set_process_bar(10)
    c_sw.statistic_start_main(main_window)
    status_widget.set_process_bar(20)
    main_window.file_datas.set_is_filed_data(True)
    main_window.file_datas.set_filed_saved_data(True)

    file_dic = s_if.save_to_dic(main_window.word_seg_result_datas,
              main_window.word_dic_datas,
              main_window.text_datas,
              main_window.statistic_datas,
              main_window.file_datas
        )
    status_widget.set_process_bar(50)

    s_if.save_to_file(file_dic, main_window.file_datas.get_file_path_data())
    status_widget.set_process_bar(80)
    main_window.change_saved(True)
    status_widget.set_message_status("另存为文件成功")
    return True

# 打开文件方法
def open_file(main_window):
    status_widget = main_window.status_widget
    status_widget.set_process_status("正在打开文件")

    file_path, selected_filter = QFileDialog.getOpenFileName(
        main_window.window,
        "打开",
        "C:/",
        "分词项目文件 (*.jbt);;所有文件 (*.*)"
    )
    if not file_path:
        status_widget.set_message_status("取消打开文件")
        return False

    if on_save(main_window):
        data = s_if.load_from_file(file_path)
        if data is None:
            QMessageBox.critical(main_window.window, "错误", "文件加载失败！")
            status_widget.set_message_status("打开文件失败")
            return False

        status_widget.set_process_bar(20)

        if not s_if.load_from_dic(data, main_window):
            QMessageBox.critical(main_window.window, "错误", "文件加载失败！")
            status_widget.set_message_status("打开文件失败")
            return False
        status_widget.set_process_bar(50)

        c_cw.data_to_text(main_window.central_widget)
        status_widget.set_process_bar(60)
        c_pw.input_seg_result_data(main_window.dock_widget.preview_window)
        status_widget.set_process_bar(70)
        c_pw.input_dic_data(main_window.dock_widget.preview_window)
        status_widget.set_process_bar(80)
        main_window.change_saved(True)
        status_widget.set_process_bar(90)

        status_widget.set_message_status("打开文件成功")
        return True
    else:
        return False

# 新建文件
def new_file(main_window):
    app.view.create_new_window()

# 询问用户未更改是否保存
def on_save(main_window):
    is_saved = main_window.file_datas.get_filed_saved_data()
    if is_saved:
        return True
    else:
        reply = QMessageBox.question(main_window.window, "保存更改", "当前文件尚未保存，是否保存？", QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel)
        if reply == QMessageBox.StandardButton.Save:
            if save_file(main_window):
                return True
            else:
                return False
        elif reply == QMessageBox.StandardButton.Discard:
            return True
        else:
            return False

# 关闭窗口方法
def close_event(main_window, event):
    if on_save(main_window):
        event.accept()
        return True
    else:
        event.ignore()
        return False