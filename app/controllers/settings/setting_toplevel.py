# 设置总窗口控制器
import app.service.io.settings

def apply(settings_toplevel):
    seg_notebook = settings_toplevel.seg_notebook # 将数据集和界面的数据赋予到临时变量中
    window_notebook = settings_toplevel.window_notebook

    seg_settings_datas = settings_toplevel.main_window.seg_settings_datas
    window_settings_datas = settings_toplevel.main_window.window_settings_datas

    # 上传至数据集
    seg_settings_datas.seg_mode_data = seg_notebook.seg_var.get()
    seg_settings_datas.auto_seg_result_frequency_data = seg_notebook.auto_seg_result_frequency_var.get()
    seg_settings_datas.auto_seg_result_class_data = seg_notebook.auto_seg_result_class_var.get()
    seg_settings_datas.hmm_data = seg_notebook.hmm_var.get()
    seg_settings_datas.chinese_word_class_data = seg_notebook.chinese_word_class_var.get()
    seg_settings_datas.ignore_sign_data = seg_notebook.ignore_sign_var.get()
    seg_settings_datas.ignore_english_data = seg_notebook.ignore_english_var.get()
    seg_settings_datas.dic_var_data = seg_notebook.dic_var.get()
    seg_settings_datas.custom_path = seg_notebook.custom_path_entry.get()

    window_settings_datas.window_weight_data = window_notebook.window_weight.get()
    window_settings_datas.window_height_data = window_notebook.window_height.get()

    settings_toplevel.apply_button_disabled()

    app.service.io.settings.save_seg_settings(seg_settings_datas) # 将分词设置转为json配置文件并保存
    app.service.io.settings.save_window_settings(window_settings_datas) # 将窗口设置转为json配置文件并保存

    # 现应用设置
    settings_toplevel.main_window.set_window_size(window_settings_datas.window_weight_data, window_settings_datas.window_height_data)

def ok(settings_toplevel):
    apply(settings_toplevel)
    settings_toplevel.settings_window.destroy()

def cancel(settings_toplevel):
    settings_toplevel.settings_window.destroy()
