# 设置总窗口控制器

def apply(settings_toplevel):
    seg_notebook = settings_toplevel.seg_notebook # 将数据集和界面的数据赋予到临时变量中
    seg_settings_datas = settings_toplevel.main_window.seg_settings_datas

    # 上传至数据集
    seg_settings_datas.seg_mode_data = seg_notebook.seg_var.get()
    seg_settings_datas.auto_seg_result_frequency_data = seg_notebook.auto_seg_result_frequency_var.get()
    seg_settings_datas.auto_seg_result_class_data = seg_notebook.auto_seg_result_class_var.get()
    seg_settings_datas.hmm_data = seg_notebook.hmm_var.get()
    seg_settings_datas.word_frequency_adjust_data = seg_notebook.word_frequency_adjust_var.get()
    seg_settings_datas.dic_var_data = seg_notebook.dic_var.get()
    seg_settings_datas.custom_path = seg_notebook.custom_path_entry.get()

    settings_toplevel.apply_button.state(['disabled'])   # 设置禁用状态

def ok(settings_toplevel):
    apply(settings_toplevel)
    settings_toplevel.settings_window.destroy()

def cancel(settings_toplevel):
    settings_toplevel.settings_window.destroy()
