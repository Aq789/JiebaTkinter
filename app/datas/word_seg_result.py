# 分词结果数据

class WordSegResult:
    def __init__(self, word_name, word_frequency, word_class):
        self.word_name = word_name
        self.word_frequency = word_frequency
        self.word_class = word_class

word_seg_result_list = []

def add_word_seg_result(word_name, word_frequency, word_class):
    temp = WordSegResult(word_name, word_frequency, word_class)
    word_seg_result_list.append(temp)

def delete_all_word_seg_result():
    while word_seg_result_list:
        word_seg_result_list.pop()