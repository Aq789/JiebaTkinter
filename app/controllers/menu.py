# 菜单栏控制器
import app.widget.settings.setting_toplevel as w_sst
import app.widget.statistic_toplevel as w_st

# 打开编辑分词结果窗口
def open_seg_result_toplevel(menu):
    left_frame = menu.main_window.paned_window.left_frame
    if not menu.edit_seg_result_var.get():
        menu.edit_seg_result_toplevel.on_close()
    else:
        menu.edit_seg_result_toplevel = left_frame.create_seg_result_toplevel()

# 打开编辑词典窗口
def open_dic_toplevel(menu):
    left_frame = menu.main_window.paned_window.left_frame
    if not menu.edit_dic_var.get():
        menu.edit_dic_toplevel.on_close()
    else:
        menu.edit_dic_toplevel = left_frame.create_word_dic_toplevel()

def create_settings_toplevel(menu):
    w_sst.SettingsToplevel(menu.main_window)

def create_statistic_toplevel(menu):
    w_st.StatisticToplevel(menu.main_window)

# 自动换行开关
def auto_enter(menu):
    if menu.auto_enter_var.get():
        menu.auto_enter_var.set(True)
        menu.main_window.paned_window.right_frame.open_auto_enter()
    else:
        menu.auto_enter_var.set(False)
        menu.main_window.paned_window.right_frame.close_auto_enter()