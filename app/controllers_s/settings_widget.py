# 设置总窗口控制器
import app.service.io.settings as s_is

# 应用按钮触发时
def apply(settings_widget):
    seg_tab = settings_widget.seg_tab
    window_tab = settings_widget.window_tab
    font_tab = settings_widget.font_tab

    if not check_custom_path(settings_widget): return False

    seg_settings_datas = settings_widget.main_window.seg_settings_datas
    window_settings_datas = settings_widget.main_window.window_settings_datas
    font_settings_datas = settings_widget.main_window.font_settings_datas

    ## 上传至数据集
    seg_settings_datas.set_seg_mode_data(seg_tab.seg_mode())
    seg_settings_datas.set_auto_seg_result_frequency_data(seg_tab.auto_seg_result_frequency.isChecked())
    seg_settings_datas.set_auto_seg_result_class_data(seg_tab.auto_seg_result_class.isChecked())
    seg_settings_datas.set_hmm_data(seg_tab.hmm_button.isChecked())
    seg_settings_datas.set_chinese_word_class_data(seg_tab.chinese_word_class.isChecked())
    seg_settings_datas.set_ignore_sign_data(seg_tab.ignore_sign_button.isChecked())
    seg_settings_datas.set_ignore_english_data(seg_tab.ignore_english_button.isChecked())
    seg_settings_datas.set_dic_var_data(seg_tab.custom_state_change())
    seg_settings_datas.set_custom_path(seg_tab.custom_path_entry.text())

    window_settings_datas.set_window_weight_data(window_tab.window_weight.value())
    window_settings_datas.set_window_height_data(window_tab.window_height.value())
    window_settings_datas.set_auto_enter_data(window_tab.auto_enter.isChecked())

    font_settings_datas.set_font_data(font_tab.families_line.text())
    font_settings_datas.set_shape_data(font_tab.styles_line.text())
    font_settings_datas.set_size_data(int(font_tab.sizes_line.text()))
    font_settings_datas.set_under_line_data(font_tab.underline.isChecked())
    font_settings_datas.set_delete_line_data(font_tab.over_strike.isChecked())

    # 更新底部按钮
    settings_widget.apply_button.setEnabled(False)

    # 将分词设置转为json并保存
    s_is.save_seg_settings(seg_settings_datas)
    s_is.save_window_settings(window_settings_datas)
    s_is.save_font_settings(font_settings_datas)

    # 应用设置
    settings_widget.main_window.central_widget.change_font()
    settings_widget.main_window.set_window_size()

    return True

# 确定按钮触发时
def ok(settings_widget):
    apply(settings_widget)
    settings_widget.settings_widget.close()

# 取消按钮触发时
def cancel(settings_widget):
    settings_widget.settings_widget.close()

# 检查目录是否合法
def check_custom_path(settings_widget):
    path = settings_widget.seg_tab.custom_path.text()
    dic_var = settings_widget.seg_tab.custom_state_change()

    if dic_var == 0:
        return True
    else:
        try:
            open(f"{path}", "r")
        except FileNotFoundError:
            settings_widget.error_window("路径错误", "自定义词典路径不存在！")
            return False
        except PermissionError:
            settings_widget.error_window("路径错误", "自定义词典路径不合法！")
            return False
        return True