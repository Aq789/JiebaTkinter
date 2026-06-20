# 分词设置数据
class SegSettings:
    def __init__(self, main_window):
        self.main_window = main_window

        self.seg_mode_data = 0 # 0, 1, 2
        self.auto_seg_result_frequency_data = True
        self.auto_seg_result_class_data = True
        self.hmm_data = False
        self.chinese_word_class_data = False
        self.ignore_sign_data = True
        self.ignore_english_data = False

        self.dic_var_data = 0
        self.custom_path = ""

    # 分词模式
    def set_seg_mode_data(self, mode):
        self.seg_mode_data = mode

    def get_seg_mode_data(self):
        return self.seg_mode_data

    # 自动统计词频
    def open_auto_seg_result_frequency_data(self):
        self.auto_seg_result_frequency_data = True

    def close_auto_seg_result_frequency_data(self):
        self.auto_seg_result_frequency_data = False

    def get_auto_seg_result_frequency_data(self):
        return self.auto_seg_result_frequency_data

    # 自动进行词性标注
    def open_auto_seg_result_class_data(self):
        self.auto_seg_result_class_data = True

    def close_auto_seg_result_class_data(self):
        self.auto_seg_result_class_data = False

    def get_auto_seg_result_class_data(self):
        return self.auto_seg_result_class_data

    # 开启HMM
    def open_hmm_data(self):
        self.hmm_data = True

    def close_hmm_data(self):
        self.hmm_data = False

    def get_hmm_data(self):
        return self.hmm_data

    # 开启中文词性
    def open_chinese_word_class_data(self):
        self.chinese_word_class_data = True

    def close_chinese_word_class_data(self):
        self.chinese_word_class_data = False

    def get_chinese_word_class_data(self):
        return self.chinese_word_class_data

    # 忽略标点符号
    def open_ignore_sign_data(self):
        self.ignore_sign_data = True

    def close_ignore_sign_data(self):
        self.ignore_sign_data = False

    def get_ignore_sign_data(self):
        return self.ignore_sign_data

    # 忽略英文单词
    def open_ignore_english_data(self):
        self.ignore_english_data = True

    def close_ignore_english_data(self):
        self.ignore_english_data = False

    def get_ignore_english_data(self):
        return self.ignore_english_data

    # 主词典选项
    def set_dic_var_data(self, number):
        self.dic_var_data = number

    def get_dic_var_data(self):
        return self.dic_var_data

    # 自定义词典路径
    def set_custom_path(self, path):
        self.custom_path = path

    def get_custom_path(self):
        return self.custom_path