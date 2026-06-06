# 结巴库词典有关方法
import jieba
import app.service.jieba.word_frequency as s_jwf
import os

# 初始化jieba词典（会丢失用户词典）
def reload_jieba_dict():
    default_dict_path = os.path.join(os.path.dirname(jieba.__file__), 'dict.txt') # 获取 jieba 包所在目录下的默认词典文件路径
    jieba.set_dictionary(default_dict_path)
    jieba.initialize() # 重新初始化分词器

# 向jieba词典中添加新词
def add_user_dict(word_name, word_frequency, word_class):
    jieba.add_word(word_name, word_frequency, word_class)

# 从数据集中加载用户词典
def load_user_dict(word_dic_datas):
    for word_dic in word_dic_datas.word_dic_list:
        if word_dic.word_frequency == "":
            add_user_dict(word_dic.word_name, 10000, word_dic.word_class)
            s_jwf.suggest_word_frequency(word_dic.word_frequency)
        else:
            add_user_dict(word_dic.word_name, word_dic.word_frequency, word_dic.word_class)

# 从数据集中加载主词典目录
def load_main_dict(seg_settings):
    jieba.set_dictionary(seg_settings.custom_path)