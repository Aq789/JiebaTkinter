# 设置总窗口控制器
import app.service.io.settings

from tkinter import messagebox

# 应用按钮触发时
def apply(settings_toplevel):
    seg_notebook = settings_toplevel.seg_notebook # 将数据集和界面的数据赋予到临时变量中
    window_notebook = settings_toplevel.window_notebook

    # 检查数据合法性
    if not check(settings_toplevel): return False

    seg_settings_datas = settings_toplevel.main_window.seg_settings_datas
    window_settings_datas = settings_toplevel.main_window.window_settings_datas

    ## 上传至数据集
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

    # 按钮回调
    settings_toplevel.apply_button_disabled()

    app.service.io.settings.save_seg_settings(seg_settings_datas) # 将分词设置转为json配置文件并保存
    app.service.io.settings.save_window_settings(window_settings_datas) # 将窗口设置转为json配置文件并保存

    # 现应用设置
    settings_toplevel.main_window.set_window_size(window_settings_datas.window_weight_data, window_settings_datas.window_height_data)

    return True

# 确定按钮触发时
def ok(settings_toplevel):
    apply(settings_toplevel)
    settings_toplevel.settings_window.destroy()

# 取消按钮触发时
def cancel(settings_toplevel):
    settings_toplevel.settings_window.destroy()

# 检查函数
def check(settings_toplevel):
    seg_notebook = settings_toplevel.seg_notebook
    window_notebook = settings_toplevel.window_notebook

    if not check_window_size(window_notebook.window_weight.get(), window_notebook.window_height.get()): return False
    if not check_custom_path_entry(seg_notebook.custom_path_entry.get(), seg_notebook.dic_var.get()): return False
    return True

# 检查目录是否合法
def check_custom_path_entry(path, dic_var):
    if dic_var == 0:
        return True
    else:
        try:
            open(f"{path}", "r")
        except FileNotFoundError:
            messagebox.showerror("错误", "自定义词典路径不存在！")
            return False
        except PermissionError:
            messagebox.showerror("错误", "自定义词典路径不合法！")
            return False
        return True

# 检查窗口大小是否合法
def check_window_size(weight, height):
    try:
        if 0 < int(weight) < 10000 and 0 < int(height) < 10000:
            return True
        else:
            messagebox.showerror("错误", "窗口大小不合法！")
            return False
    except ValueError:
        messagebox.showerror("错误", "窗口大小不合法！")
        return False