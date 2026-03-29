# 分词结果数据结构
class WordSegResult:
    def __init__(self, word_name, word_frequency, word_class):
        self.word_name = word_name
        self.word_frequency = word_frequency
        self.word_class = word_class

# 分词结果数据集
class WordSegResultDatas:
    def __init__(self, main_window):
        self.main_window = main_window
        self.word_seg_result_list = []

    def add_word_seg_result(self, word_name, word_frequency, word_class):
        temp = WordSegResult(word_name, word_frequency, word_class)
        self.word_seg_result_list.append(temp)

    def delete_all_word_seg_result(self):
        while self.word_seg_result_list:
            self.word_seg_result_list.pop()

    def return_word_seg_result_list(self):
        return self.word_seg_result_list