# 文件相关控制器
from PySide6.QtWidgets import QFileDialog, QMessageBox

import app.service.io.file as s_if
import app.controllers.central_widget as c_cw
import app.controllers.statistic_widget as c_sw

# 保存文件
def save_file(main_window):

    if not main_window.file_datas.check_is_filed(): # 如果当前没有打开文件
        file_path, selected_filter = QFileDialog.getSaveFileName(
            main_window.window,
            "请选择保存路径",
            "~/新建分词文件.jbt",
            "分词文件 (*.jbt);;所有文件 (*.*)"
        )
        if not file_path:
            return False
        main_window.file_datas.set_file_path_data(file_path)

    c_cw.text_to_data(main_window.central_widget)
    c_sw.statistic_start_main(main_window)
    main_window.file_datas.set_is_filed_data(True)
    main_window.file_datas.set_filed_saved_data(True)

    file_dic = s_if.save_to_dic(main_window.word_seg_result_datas,
              main_window.word_dic_datas,
              main_window.text_datas,
              main_window.statistic_datas,
              main_window.file_datas
        )

    s_if.save_to_file(file_dic, main_window.file_datas.get_file_path_data())
    main_window.change_saved(True)
    return True

# 关闭窗口方法
def close_event(main_window, event):
    is_saved = main_window.file_datas.get_filed_saved_data()
    if is_saved:
        event.accept()
        return

    reply = QMessageBox.question(main_window.window, "保存更改", "当前文件尚未保存，是否保存？", QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel)
    if reply == QMessageBox.StandardButton.Save:
        if save_file(main_window):
            event.accept()
        else:
            event.ignore()
    elif reply == QMessageBox.StandardButton.Discard:
        event.accept()
    else:
        event.ignore()