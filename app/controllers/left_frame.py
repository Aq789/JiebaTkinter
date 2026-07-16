# 左侧窗口模块控制器
import tkinter as tk
import time

import app.controllers.right_frame as c_rf
import app.service.jieba.start as s_js
import app.service.word_class_name as s_wcn

# 从分词结果数据导入至左侧表格模块
def input_seg_result_data(left_frame):
    setting_chinese_word_class = left_frame.main_window.seg_settings_datas.get_chinese_word_class_data() # 获取中文词性设置

    last_iid = left_frame.show_word_seg_result.insert('', "end")
    temp_iid = left_frame.show_word_seg_result.prev(last_iid)
    left_frame.show_word_seg_result.delete(last_iid)
    while temp_iid:
        prev_temp_iid = left_frame.show_word_seg_result.prev(temp_iid)
        left_frame.show_word_seg_result.delete(temp_iid)
        temp_iid = prev_temp_iid

    number = 1  # 用来记录序号
    if setting_chinese_word_class:
        for data in left_frame.main_window.word_seg_result_datas.return_word_seg_result_list():  # 遍历分词结果数据
            left_frame.show_word_seg_result.insert('', "end", values=(number, data.word_name, data.word_frequency, s_wcn.chinese_word_class(data.word_class))) # 添加到表格中
            number += 1
    else:
        for data in left_frame.main_window.word_seg_result_datas.return_word_seg_result_list():  # 遍历分词结果数据
            left_frame.show_word_seg_result.insert('', "end", values=(number, data.word_name, data.word_frequency, data.word_class)) # 添加到表格中
            number += 1
    return True

# 从词典数据导入至左侧表格模块
def input_dic_data(left_frame):
    last_iid = left_frame.show_word_dic.insert('', "end")
    temp_iid = left_frame.show_word_dic.prev(last_iid)
    left_frame.show_word_dic.delete(last_iid)
    while temp_iid:
        prev_temp_iid = left_frame.show_word_dic.prev(temp_iid)
        left_frame.show_word_dic.delete(temp_iid)
        temp_iid = prev_temp_iid

    number = 1  # 用来记录序号
    for data in left_frame.main_window.word_dic_datas.return_word_dic_list():  # 遍历词典数据
        left_frame.show_word_dic.insert('', "end", values=(number, data.word_name, data.word_frequency, data.word_class))  # 添加到表格中
        number += 1
    return True

# 开始分词按钮总控制器
def start_seg_word(left_frame):
    status_bar = left_frame.main_window.status_bar

    start_time = time.perf_counter()
    left_frame.start_word_seg_result.config(state=tk.DISABLED) # 将开始按钮设为禁用
    c_rf.text_to_data(left_frame.main_window.paned_window.right_frame) # 将文本上传至数据集
    s_js.start(left_frame.main_window.seg_settings_datas, left_frame.main_window.text_datas, left_frame.main_window.word_dic_datas, left_frame.main_window.word_seg_result_datas)
    input_seg_result_data(left_frame)
    left_frame.start_word_seg_result.config(state=tk.NORMAL)  # 将开始按钮设为启用
    end_time = time.perf_counter()

    total_time = (end_time - start_time) * 1000
    status_bar.set_ready_status(f"分词完成，耗时{total_time:.1f}ms")