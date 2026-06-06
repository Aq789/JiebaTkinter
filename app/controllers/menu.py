# 菜单栏控制器
import app.widget.settings.setting_toplevel as w_sst

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