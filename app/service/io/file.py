# 项目文件有关方法
import json
from app.datas.word_seg_result import WordSegResultDatas
from app.datas.word_dic import WordDicDatas
from app.datas.text import Text
from app.datas.statistic import Statistic
from app.datas.file import File

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

    text_result_list = word_seg_result_datas.get_text_result_list()

    word_seg_result_dict = {
        "word_seg_result_list": word_seg_result_list,
        "text_result_list": text_result_list
    }

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
        "word_seg_result_datas": word_seg_result_dict,
        "word_dic_datas": word_dic_list,
        "text_datas": text_datas.get_text_data(),
        "statistic": statistic_dic,
        "file_datas": file_datas.get_file_path_data()
    }

    return file_dic

# 将加载的文件数据上传至数据集
def load_from_dic(data, main_window):
    ls = check_data(data, main_window)
    if ls is not None:
        main_window.word_seg_result_datas = ls[0]
        main_window.word_dic_datas = ls[1]
        main_window.text_datas = ls[2]
        main_window.statistic_datas = ls[3]
        main_window.file_datas = ls[4]
        return True
    else:
        return False

# 检查数据是否合法
def check_data(data, main_window):
    try:
        temp_word_seg_result_datas = WordSegResultDatas(main_window)
        temp_word_dic_datas = WordDicDatas(main_window)
        temp_text_datas = Text(main_window)
        temp_statistic_datas = Statistic(main_window)
        temp_file_datas = File(main_window)

        word_seg_result_dict = data["word_seg_result_datas"]
        temp_word_seg_result_datas.delete_all_word_seg_result()
        for word_seg_result in word_seg_result_dict["word_seg_result_list"]:
            temp_word_seg_result_datas.add_word_seg_result(word_seg_result["word_name"], word_seg_result["word_frequency"],
                                                      word_seg_result["word_class"])
        temp_word_seg_result_datas.set_text_result_list(word_seg_result_dict["text_result_list"])

        word_dic_list = data["word_dic_datas"]
        temp_word_dic_datas.delete_all_word_dic()
        for word_dic in word_dic_list:
            temp_word_dic_datas.add_word_dic(word_dic["word_name"], word_dic["word_frequency"], word_dic["word_class"])

        temp_text_datas.set_text_data(data["text_datas"])

        statistic_dict = data["statistic"]
        temp_statistic_datas.set_chinese_char_count_data(statistic_dict["chinese_char_count_data"])
        temp_statistic_datas.set_char_count_no_space_data(statistic_dict["char_count_no_space_data"])
        temp_statistic_datas.set_char_count_with_space_data(statistic_dict["char_count_with_space_data"])
        temp_statistic_datas.set_chinese_word_count_data(statistic_dict["chinese_word_count_data"])
        temp_statistic_datas.set_seg_result_count_only_chinese_data(statistic_dict["seg_result_count_only_chinese_data"])
        temp_statistic_datas.set_seg_result_count_all_data(statistic_dict["seg_result_count_all_data"])
        temp_statistic_datas.set_custom_dict_size_data(statistic_dict["custom_dict_size_data"])
        temp_statistic_datas.set_english_word_count_data(statistic_dict["english_word_count_data"])
        temp_statistic_datas.set_line_count_data(statistic_dict["line_count_data"])

        temp_file_datas.set_file_path_data(data["file_datas"])

        return temp_word_seg_result_datas, temp_word_dic_datas, temp_text_datas, temp_statistic_datas, temp_file_datas
    except Exception:
        return None

# 保存到磁盘
def save_to_file(file_dic, path):
    with open(f"{path}", "w", encoding="utf-8") as f:
        json.dump(file_dic, f, ensure_ascii=False)

# 从磁盘中加载
def load_from_file(path):
    try:
        with open(f"{path}", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    return data