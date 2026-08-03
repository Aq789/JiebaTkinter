# 统计相关方法
import app.service.statistic as s_s

def statistic_start(statistic_widget):
    text = statistic_widget.main_window.central_widget.text_edit.toPlainText()
    seg_list = statistic_widget.main_window.word_seg_result_datas.get_text_result_list()
    seg_result_list = statistic_widget.main_window.word_seg_result_datas.return_word_seg_result_list()
    word_dic_datas = statistic_widget.main_window.word_dic_datas
    statistic_datas = statistic_widget.main_window.statistic_datas

    # 开始计算
    statistic_list = s_s.start_statistic(text, seg_list, seg_result_list, word_dic_datas)

    # 保存至统计信息数据集
    statistic_datas.set_all_datas(statistic_list)

    # 显示到界面
    statistic_widget.chinese_char_count.message.setText(str(statistic_list[0]))
    statistic_widget.char_count_no_space.message.setText(str(statistic_list[1]))
    statistic_widget.char_count_with_space.message.setText(str(statistic_list[2]))
    statistic_widget.chinese_word_count.message.setText(str(statistic_list[3]))
    statistic_widget.seg_result_count_only_chinese.message.setText(str(statistic_list[4]))
    statistic_widget.seg_result_count_all.message.setText(str(statistic_list[5]))
    statistic_widget.custom_dict_size.message.setText(str(statistic_list[6]))
    statistic_widget.english_word_count.message.setText(str(statistic_list[7]))
    statistic_widget.line_count.message.setText(str(statistic_list[8]))

# 主窗口统计方法
def statistic_start_main(main_window):
    text = main_window.central_widget.text_edit.toPlainText()
    seg_list = main_window.word_seg_result_datas.get_text_result_list()
    seg_result_list = main_window.word_seg_result_datas.return_word_seg_result_list()
    word_dic_datas = main_window.word_dic_datas
    statistic_datas = main_window.statistic_datas

    # 开始计算
    statistic_list = s_s.start_statistic(text, seg_list, seg_result_list, word_dic_datas)

    # 保存至统计信息数据集
    statistic_datas.set_all_datas(statistic_list)