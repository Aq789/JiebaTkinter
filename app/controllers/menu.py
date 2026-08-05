# 菜单栏控制器
from PySide6.QtCore import Qt

import app.widget.settings.settings_widget as w_ssw
import app.widget.statistic_widget as w_sw
import app.controllers.central_widget as c_cw
import app.controllers.file as c_f
import app.controllers.io.output as c_io
import app.controllers.io.input as c_ii

# 创建设置窗口
def create_settings_widget(menu):
    w_ssw.SettingsWidget(menu.main_window)

# 创建统计窗口
def create_statistic_widget(menu):
    w_sw.StatisticWidget(menu.main_window)

# 开始分词
def start_menu(menu):
    central_widget = menu.main_window.central_widget
    c_cw.start_seg_word(central_widget)

# 换行开关
def auto_enter(menu):
    central_widget = menu.main_window.central_widget
    if menu.auto_enter_action.isChecked():
        c_cw.open_auto_enter(central_widget)
    else:
        c_cw.close_auto_enter(central_widget)

# 创建查找窗口
def check_widget(menu):
    if menu.check_widget is None:
        menu.check_widget = menu.main_window.create_check_widget()
    else:
        menu.check_widget.check_widget.close()
        menu.check_widget = None

# 编辑分词结果开关
def word_seg_result_widget(menu, checked):
    if checked:
        if menu.word_seg_result_widget is None:
            menu.word_seg_result_widget = menu.main_window.create_word_seg_result_widget()
    else:
        if menu.word_seg_result_widget is not None:
            menu.word_seg_result_widget.word_seg_result_widget.close()

# 编辑词典开关
def word_dic_widget(menu, checked):
    if checked:
        if menu.word_dic_widget is None:
            menu.word_dic_widget = menu.main_window.create_word_dic_widget()
    else:
        if menu.word_dic_widget is not None:
            menu.word_dic_widget.word_dic_widget.close()

# 状态栏隐藏开关
def toggle_statusbar(menu):
    menu.main_window.status_widget.toggle_statusbar()

# 侧边栏开关
def on_dock_visibility_changed(menu, visible):
    if menu.main_window.window.windowState() & Qt.WindowMinimized: return
    menu.preview_window_hidden_action.setChecked(not visible)

# 侧边栏隐藏函数
def on_checkbox_toggled(menu, checked):
    dock_widget = menu.main_window.dock_widget.dock_widget
    dock_widget.setVisible(not checked)

# 复制操作
def on_copy(menu):
    editor = menu.main_window.get_focus()
    if editor == 0:
        menu.main_window.central_widget.copy()
    elif editor == 1:
        menu.main_window.dock_widget.preview_window.seg_result_table.copy_rows_as_custom_string()
    else:
        return

# 剪切操作
def on_cut(menu):
    menu.main_window.central_widget.cut()

# 粘贴操作
def on_paste(menu):
    menu.main_window.central_widget.paste()

# 撤销操作
def undo(menu):
    menu.main_window.central_widget.undo()

# 恢复操作
def redo(menu):
    menu.main_window.central_widget.redo()

# 保存操作
def save(menu):
    c_f.save_file(menu.main_window)

# 另存为操作
def other_save(menu):
    c_f.other_save_file(menu.main_window)

# 打开操作
def open_file(menu):
    c_f.open_file(menu.main_window)

# 新建操作
def new_file(menu):
    c_f.new_file(menu.main_window)

# 导入文本文件
def input_text_file(menu):
    c_ii.input_text_file(menu.main_window)

# 导入词典文件
def input_dic_file(menu):
    c_ii.input_dic_file(menu.main_window)

# 导出文本文件
def output_text_file(menu):
    c_io.output_text_file(menu.main_window)

# 导出分词结果文件
def output_seg_result_file(menu):
    c_io.output_seg_result_file(menu.main_window)

# 导出词典文件
def output_dic_file(menu):
    c_io.output_dic_file(menu.main_window)

# 退出
def exit_action(menu):
    menu.main_window.on_close()