# 菜单栏控制器
import app.widget.settings.setting_toplevel as w_sst
import app.widget.statistic_toplevel as w_st
import app.controllers.left_frame as c_lf

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

# 创建设置窗口
def create_settings_toplevel(menu):
    w_sst.SettingsToplevel(menu.main_window)

# 创建统计窗口
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

# 状态栏显示开关
def visible_status_bar(menu):
    if menu.visible_status_bar_var.get():
        menu.visible_status_bar_var.set(True)
        status_bar = menu.main_window.status_bar
        status_bar.bottom_status_bar.grid_remove()
    else:
        menu.visible_status_bar_var.set(False)
        status_bar = menu.main_window.status_bar
        status_bar.bottom_status_bar.grid()

# 左侧预览窗口显示开关
def visible_left_frame(menu):
    if menu.visible_left_frame_var.get():
        menu.visible_left_frame_var.set(True)
        paned_window = menu.main_window.paned_window
        paned_window.invisible_left_frame()
    else:
        menu.visible_left_frame_var.set(False)
        paned_window = menu.main_window.paned_window
        paned_window.visible_left_frame()

# 开始分词
def start_menu(menu):
    paned_window = menu.main_window.paned_window
    left_frame = paned_window.left_frame

    menu.visible_left_frame_var.set(False)  # 调整菜单状态
    paned_window.visible_left_frame()
    c_lf.start_seg_word(left_frame) # 调用侧边栏开始分词