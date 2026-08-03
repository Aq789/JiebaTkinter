# 项目文件有关方法
import json


# 将数据转换成字典
def save_to_dic(word_seg_result_datas, word_dic_datas, text_datas, statistic_datas, file_datas):

    word_seg_result_list = []
    for word_seg_result in word_seg_result_datas.return_word_seg_result_list():
        temp_dic = {
            "word_name": word_seg_result.word_name,
            "word_frequency": word_seg_result.word_frequency,
            "word_class": word_seg_result.word_class
        }
        word_seg_result_list.append(temp_dic)

    word_dic_list = []
    for word_dic in word_dic_datas.return_word_dic_list():
        temp_dic = {
            "word_name": word_dic.word_name,
            "word_frequency": word_dic.word_frequency,
            "word_class": word_dic.word_class
        }
        word_dic_list.append(temp_dic)

    statistic_dic = {
        "chinese_char_count_data": statistic_datas.chinese_char_count_data,
        "char_count_no_space_data": statistic_datas.char_count_no_space_data,
        "char_count_with_space_data": statistic_datas.char_count_with_space_data,
        "chinese_word_count_data": statistic_datas.chinese_word_count_data,
        "seg_result_count_only_chinese_data": statistic_datas.seg_result_count_only_chinese_data,
        "seg_result_count_all_data": statistic_datas.seg_result_count_all_data,
        "custom_dict_size_data": statistic_datas.custom_dict_size_data,
        "english_word_count_data": statistic_datas.english_word_count_data,
        "line_count_data": statistic_datas.line_count_data
    }

    file_dic = {
        "word_seg_result_datas": word_seg_result_list,
        "word_dic_datas": word_dic_list,
        "text_datas": text_datas.get_text_data(),
        "statistic": statistic_dic,
        "file_datas": file_datas.get_file_path_data()
    }

    return file_dic

# 保存到磁盘
def save_to_file(file_dic, path):
    with open(f"{path}", "w", encoding="utf-8") as f:
        json.dump(file_dic, f, indent=0, ensure_ascii=False)