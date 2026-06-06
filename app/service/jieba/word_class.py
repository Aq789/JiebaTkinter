# 词性有关函数
import jieba.posseg as pseg

# 词性标注函数
def pos_tag(seg_word):
    words = pseg.cut(seg_word)
    for word, flag in words:
        return flag
    return None