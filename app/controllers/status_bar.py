# 状态栏控制方法

# 刷新自定义词典数量
def refresh_custom_dict_count(status_bar):
    status_bar.len_word_dic_list_data = status_bar.main_window.word_dic_datas.return_len_word_dic_list()
    status_bar.custom_dict_count.config(text=f"自定义词典数：{status_bar.len_word_dic_list_data}")