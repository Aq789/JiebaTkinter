# 数据集与字典
import app.service.io.settings as s_is

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