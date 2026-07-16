# 词典数据结构
class WordDic:
    def __init__(self, word_name, word_frequency, word_class):
        self.word_name = word_name
        self.word_frequency = word_frequency
        self.word_class = word_class

# 词典数据集
class WordDicDatas:
    def __init__(self, main_window):
        self.main_window = main_window
        self.word_dic_list = []

    def add_word_dic(self, word_name, word_frequency, word_class):
        temp = WordDic(word_name, word_frequency, word_class)
        self.word_dic_list.append(temp)

    def delete_all_word_dic(self):
        while self.word_dic_list:
            self.word_dic_list.pop()

    def return_word_dic_list(self):
        return self.word_dic_list

    def return_len_word_dic_list(self):
        return len(self.word_dic_list)