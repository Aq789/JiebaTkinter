# 词频有关函数
import jieba
from collections import Counter

# 自动收集词频
def word_stat(seg_result):
    seg_list = ",".join(seg_result).split(",")
    seg_dict = dict(Counter(seg_list))
    return seg_dict

# 词典词频动态调整
def suggest_word_frequency(word):
    jieba.suggest_freq(word, tune=True)