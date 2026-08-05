# 导出有关方法
import json


# 数据转换方法
def output_txt_data(list_data):
    result = ""
    for data in list_data:
        temp = f"{data.word_name} {data.word_frequency} {data.word_class}\n"
        result += temp
    return result

def output_csv_data(list_data):
    result = ""
    for data in list_data:
        temp = f"{data.word_name},{data.word_frequency},{data.word_class}\n"
        result += temp
    return result

def output_dic_data(list_data):
    word_dic_list = []
    for data in list_data:
        temp = {
            "word_name": data.word_name,
            "word_frequency": data.word_frequency,
            "word_class": data.word_class
        }
        word_dic_list.append(temp)

    word_dict = {
        "word_dic_list": word_dic_list
    }
    return word_dict

# 保存至磁盘
def output_text_file(text, path):
    with open(f"{path}", "w", encoding="utf-8") as f:
        f.writelines(text)

def output_word_seg_file(data, path):
    with open(f"{path}", "w", encoding="utf-8-sig") as f:
        f.writelines(data)

def output_word_dic_file(data, path):
    with open(f"{path}", "w", encoding="utf-8-sig") as f:
        f.writelines(data)

def output_dic_file(data, path):
    with open(f"{path}", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)