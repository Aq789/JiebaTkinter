# 左侧窗口模块控制器

# 从分词结果数据导入至左侧表格模块
def input_seg_result_data(left_frame):

    last_iid = left_frame.show_word_seg_result.insert('', "end")
    temp_iid = left_frame.show_word_seg_result.prev(last_iid)
    left_frame.show_word_seg_result.delete(last_iid)
    while temp_iid:
        prev_temp_iid = left_frame.show_word_seg_result.prev(temp_iid)
        left_frame.show_word_seg_result.delete(temp_iid)
        temp_iid = prev_temp_iid

    number = 1  # 用来记录序号
    for data in left_frame.main_window.word_seg_result_datas.return_word_seg_result_list():  # 遍历分词结果数据
        left_frame.show_word_seg_result.insert('', "end",  # 添加到表格中
                                                         values=(number, data.word_name, data.word_frequency, data.word_class))
        number += 1
    return True