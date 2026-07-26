# 统计数据
class Statistic:
    def __init__(self, main_window):
        self.main_window = main_window

        self.chinese_char_count_data = 0
        self.char_count_no_space_data = 0
        self.char_count_with_space_data = 0
        self.chinese_word_count_data = 0
        self.seg_result_count_only_chinese_data = 0
        self.seg_result_count_all_data = 0
        self.custom_dict_size_data = 0
        self.english_word_count_data = 0
        self.line_count_data = 0

    # 中文字数
    def set_chinese_char_count_data(self, data):
        self.chinese_char_count_data = data

    def get_chinese_char_count_data(self):
        return self.chinese_char_count_data

    # 字符数（不计空格）
    def set_char_count_no_space_data(self, data):
        self.char_count_no_space_data = data

    def get_char_count_no_space_data(self):
        return self.char_count_no_space_data

    # 字符数（计空格）
    def set_char_count_with_space_data(self, data):
        self.char_count_with_space_data = data

    def get_char_count_with_space_data(self):
        return self.char_count_with_space_data

    # 中文词数
    def set_chinese_word_count_frame_data(self, data):
        self.chinese_word_count_data = data

    def get_chinese_word_count_frame_data(self):
        return self.chinese_word_count_data

    # 分词结果总数（仅中文）
    def set_seg_result_count_only_chinese_data(self, data):
        self.seg_result_count_only_chinese_data = data

    def get_seg_result_count_only_chinese_data(self):
        return self.seg_result_count_only_chinese_data

    # 分词结果总数（所有）
    def set_seg_result_count_all_data(self, data):
        self.seg_result_count_all_data = data

    def get_seg_result_count_all_data(self):
        return self.seg_result_count_all_data

    # 自定义词典总数
    def set_custom_dict_size_data(self, data):
        self.custom_dict_size_data = data

    def get_custom_dict_size_data(self):
        return self.custom_dict_size_data

    # 英文单词数
    def set_english_word_count_data(self, data):
        self.english_word_count_data = data

    def get_english_word_count_data(self):
        return self.english_word_count_data

    # 行数
    def set_line_count_data(self, data):
        self.line_count_data = data

    def get_line_count_data(self):
        return self.line_count_data

    # 接收列表加入统计中
    def set_all_datas(self, ls):
        self.set_chinese_char_count_data(ls[0])
        self.set_char_count_no_space_data(ls[1])
        self.set_char_count_with_space_data(ls[2])
        self.set_chinese_word_count_frame_data(ls[3])
        self.set_seg_result_count_only_chinese_data(ls[4])
        self.set_seg_result_count_all_data(ls[5])
        self.set_custom_dict_size_data(ls[6])
        self.set_english_word_count_data(ls[7])
        self.set_line_count_data(ls[8])