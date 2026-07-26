# 统计相关算法

# 统计窗口弹出时的方法
def start_statistic(text, seg_list, seg_result_list, word_dic_datas):
    chinese_char_count_data, char_count_no_space_data, char_count_with_space_data, line_count_data = first_statistic(text)
    chinese_word_count_data, english_word_count_data = second_statistic(seg_list)
    seg_result_count_only_chinese_data, seg_result_count_all_data = third_statistic(seg_result_list)
    custom_dict_size_data = last_statistic(word_dic_datas)
    return chinese_char_count_data, char_count_no_space_data, char_count_with_space_data, chinese_word_count_data, seg_result_count_only_chinese_data, seg_result_count_all_data, custom_dict_size_data, english_word_count_data, line_count_data

# 一次遍历算出中文字数，字符数（计空格和不计空格）
def first_statistic(text):
    chinese_count = 0
    char_no_space = 0
    char_with_space = 0
    line_count = 1

    for ch in text:
        if ch != "\n":
            char_with_space += 1

        if ch == '\n':
            line_count += 1

        if not ch.isspace():
            char_no_space += 1
            code = ord(ch)
            if 0x4E00 <= code <= 0x9FFF or 0x3400 <= code <= 0x4DBF:
                chinese_count += 1

    return chinese_count, char_no_space, char_with_space, line_count

# 算出中文词数，英文单词数，行数
def second_statistic(seg_list):
    # 中文词数
    chinese_word_count = 0
    for token in seg_list:
        for ch in token:
            if 0x4E00 <= ord(ch) <= 0x9FFF or 0x3400 <= ord(ch) <= 0x4DBF:
                chinese_word_count += 1
                break

    # 英文单词数
    english_word_count = 0
    for token in seg_list:
        if token and all('a' <= c <= 'z' or 'A' <= c <= 'Z' for c in token):
            english_word_count += 1

    return chinese_word_count, english_word_count

# 算出分词结果总数（仅中文和所有）
def third_statistic(seg_result_list):
    only_chinese_count = 0
    all_count = 0

    for seg_result in seg_result_list:
        all_count += 1
        for ch in seg_result.word_name:
            if 0x4E00 <= ord(ch) <= 0x9FFF or 0x3400 <= ord(ch) <= 0x4DBF:
                only_chinese_count += 1
                break

    return only_chinese_count, all_count

# 算出自定义词典数
def last_statistic(word_dic_datas):
    custom_dict_count = len(word_dic_datas.return_word_dic_list())
    return custom_dict_count