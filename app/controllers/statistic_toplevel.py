# 统计相关方法
import app.service.statistic as s_s

def statistic_start(statistic_toplevel):
    # 初始化数据
    text = statistic_toplevel.main_window.paned_window.right_frame.text
    seg_list = statistic_toplevel.main_window.word_seg_result_datas.get_text_result_list()
    seg_result_list = statistic_toplevel.main_window.word_seg_result_datas.return_word_seg_result_list()
    word_dic_datas = statistic_toplevel.main_window.word_dic_datas
    statistic_datas = statistic_toplevel.main_window.statistic_datas

    # 开始运算
    statistic_list = s_s.start_statistic(text.get("1.0", "end"), seg_list, seg_result_list, word_dic_datas)

    # 保存至统计信息数据集
    statistic_datas.set_chinese_char_count_data(statistic_list[0])
    statistic_datas.set_char_count_no_space_data(statistic_list[1])
    statistic_datas.set_char_count_with_space_data(statistic_list[2])
    statistic_datas.set_chinese_word_count_frame_data(statistic_list[3])
    statistic_datas.set_seg_result_count_only_chinese_data(statistic_list[4])
    statistic_datas.set_seg_result_count_all_data(statistic_list[5])
    statistic_datas.set_custom_dict_size_data(statistic_list[6])
    statistic_datas.set_english_word_count_data(statistic_list[7])
    statistic_datas.set_line_count_data(statistic_list[8])

    # 显示到界面
    statistic_toplevel.chinese_char_count.config(text=str(statistic_list[0]))
    statistic_toplevel.char_count_no_space.config(text=str(statistic_list[1]))
    statistic_toplevel.char_count_with_space.config(text=str(statistic_list[2]))
    statistic_toplevel.chinese_word_count.config(text=str(statistic_list[3]))
    statistic_toplevel.seg_result_count_only_chinese.config(text=str(statistic_list[4]))
    statistic_toplevel.seg_result_count_all.config(text=str(statistic_list[5]))
    statistic_toplevel.custom_dict_size.config(text=str(statistic_list[6]))
    statistic_toplevel.english_word_count.config(text=str(statistic_list[7]))
    statistic_toplevel.line_count.config(text=str(statistic_list[8]))

