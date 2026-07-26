# 菜单栏控制器
import app.widget_s.settings.settings_widget as w_ssw
import app.widget_s.statistic_widget as w_sw
import app.controllers_s.central_widget as c_cw

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