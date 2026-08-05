# 导入有关方法
import json

from app.datas.word_dic import WordDicDatas


# 将词典格式词典数据导入数据集
def input_dic_data(data, main_window):
    temp_word_dic_datas = check_dic_data(data, main_window)
    if temp_word_dic_datas is not None:
        for word_dic in temp_word_dic_datas.return_word_dic_list():
            main_window.word_dic_datas.add_word_dic(word_dic.word_name, word_dic.word_frequency, word_dic.word_class)
        return True
    else:
        return False

# 将文本格式词典数据导入数据集
def input_txt_data(data, main_window):
    temp_word_dic_datas = check_txt_data(data, main_window)
    if temp_word_dic_datas is not None:
        for word_dic in temp_word_dic_datas.return_word_dic_list():
            main_window.word_dic_datas.add_word_dic(word_dic.word_name, word_dic.word_frequency, word_dic.word_class)
        return True
    else:
        return False

# 将表格格式词典数据导入数据集
def input_csv_data(data, main_window):
    temp_word_dic_datas = check_csv_data(data, main_window)
    if temp_word_dic_datas is not None:
        for word_dic in temp_word_dic_datas.return_word_dic_list():
            main_window.word_dic_datas.add_word_dic(word_dic.word_name, word_dic.word_frequency, word_dic.word_class)
        return True
    else:
        return False

# 检查词典dic文件数据
def check_dic_data(data, main_window):
    try:
        temp_word_dic_datas = WordDicDatas(main_window)
        for word_dic in data["word_dic_list"]:
            temp_word_dic_datas.add_word_dic(word_dic["word_name"], word_dic["word_frequency"], word_dic["word_class"])

        return temp_word_dic_datas
    except Exception:
        return None

# 检查词典txt文件数据
def check_txt_data(data, main_window):
    try:
        temp_word_dic_datas = WordDicDatas(main_window)
        for line in data:
            temp_word_dic_datas.add_word_dic(line[0], line[1], line[2])

        return temp_word_dic_datas
    except Exception:
        return None

# 检查词典csv文件数据
def check_csv_data(data, main_window):
    try:
        temp_word_dic_datas = WordDicDatas(main_window)
        for line in data:
            temp_word_dic_datas.add_word_dic(line[0], line[1], line[2])

        return temp_word_dic_datas
    except Exception:
        return None

# 从磁盘中加载文本类文件
def input_text_file(path):
    try:
        with open(f"{path}", "r", encoding="utf-8") as f:
            data = f.read()
    except FileNotFoundError:
        return None
    return data

# 从磁盘中加载文本类文件
def input_csv_file(path):
    try:
        with open(f"{path}", "r", encoding="utf-8-sig") as f:
            data = f.read()
    except FileNotFoundError:
        return None
    return data

# 从磁盘中加载json类文件
def input_dic_file(path):
    try:
        with open(f"{path}", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    return data