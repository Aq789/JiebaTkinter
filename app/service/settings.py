# 数据集与字典
import app.service.io.settings as s_is

# 将分词配置转换为字典
def seg_settings_to_dict(seg_settings):
    seg_settings_dic = {
        "seg_mode_data": seg_settings.seg_mode_data,
        "auto_seg_result_frequency_data": seg_settings.auto_seg_result_frequency_data,
        "auto_seg_result_class_data": seg_settings.auto_seg_result_class_data,
        "hmm_data": seg_settings.hmm_data,
        "chinese_word_class_data": seg_settings.chinese_word_class_data,
        "ignore_sign_data": seg_settings.ignore_sign_data,
        "ignore_english_data": seg_settings.ignore_english_data,
        "dic_var_data": seg_settings.dic_var_data,
        "custom_path": seg_settings.custom_path
    }
    return seg_settings_dic

# 将窗口配置转换为字典
def window_settings_to_dict(window_settings):
    window_settings_dic = {
        "window_weight_data": window_settings.window_weight_data,
        "window_height_data": window_settings.window_height_data,
        "auto_enter_data": window_settings.auto_enter_data
    }
    return window_settings_dic

# 将字体配置转换为字典
def font_settings_to_dict(font_settings):
    font_settings_dic = {
        "font_data": font_settings.font_data,
        "shape_data": font_settings.shape_data,
        "size_data": font_settings.size_data,
        "under_line_data": font_settings.under_line_data,
        "delete_line_data": font_settings.delete_line_data,
        "color_data": font_settings.color_data
    }
    return font_settings_dic

# 将字典转换为分词配置
def seg_settings_to_data(window):
    data = s_is.load_seg_settings()
    window.seg_settings_datas.seg_mode_data = data["seg_mode_data"]
    window.seg_settings_datas.auto_seg_result_frequency_data = data["auto_seg_result_frequency_data"]
    window.seg_settings_datas.auto_seg_result_class_data = data["auto_seg_result_class_data"]
    window.seg_settings_datas.hmm_data = data["hmm_data"]
    window.seg_settings_datas.chinese_word_class_data = data["chinese_word_class_data"]
    window.seg_settings_datas.ignore_sign_data = data["ignore_sign_data"]
    window.seg_settings_datas.ignore_english_data = data["ignore_english_data"]
    window.seg_settings_datas.dic_var_data = data["dic_var_data"]
    window.seg_settings_datas.custom_path = data["custom_path"]

# 将字典转换为窗口配置
def window_settings_to_data(window):
    data = s_is.load_window_settings()
    window.window_settings_datas.window_weight_data = data["window_weight_data"]
    window.window_settings_datas.window_height_data = data["window_height_data"]
    window.window_settings_datas.auto_enter_data = data["auto_enter_data"]

# 将字典转换为字体配置
def font_settings_to_data(window):
    data = s_is.load_font_settings()
    window.font_settings_datas.font_data = data["font_data"]
    window.font_settings_datas.shape_data = data["shape_data"]
    window.font_settings_datas.size_data = data["size_data"]
    window.font_settings_datas.under_line_data = data["under_line_data"]
    window.font_settings_datas.delete_line_data = data["delete_line_data"]
    window.font_settings_datas.color_data = data["color_data"]
