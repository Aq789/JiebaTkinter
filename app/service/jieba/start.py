# jieba分词函数
import jieba
import unicodedata
import app.service.jieba.dictionary as s_jd
import app.service.jieba.word_frequency as s_jwf
import app.service.jieba.word_class as s_jwc

# 分词核心
def start(seg_settings, text_datas, word_dic_datas, word_seg_result_datas):
    s_jd.reload_jieba_dict() # 初始化jieba词典
    if seg_settings.dic_var_data == 1: # 如果主词典为自定义词典
        s_jd.load_main_dict(seg_settings.custom_path)
    s_jd.load_user_dict(word_dic_datas) # 加载用户词典

    word_seg_result_datas.delete_all_word_seg_result()  # 删除所有分词结果
    if seg_settings.seg_mode_data == 0: # 全模式
        if seg_settings.hmm_data:
            seg_result = jieba.cut(text_datas.get_text_data(), cut_all=True, HMM=True) # 如果HMM开启
        else:
            seg_result = jieba.cut(text_datas.get_text_data(), cut_all=True, HMM=False)
    elif seg_settings.seg_mode_data == 1: # 精确模式
        if seg_settings.hmm_data: seg_result = jieba.cut(text_datas.get_text_data(), cut_all=False, HMM=True)
        else: seg_result = jieba.cut(text_datas.get_text_data(), cut_all=False, HMM=False)
    else: # 搜索引擎模式
        if seg_settings.hmm_data: seg_result = jieba.cut_for_search(text_datas.get_text_data(), HMM=True)
        else: seg_result = jieba.cut_for_search(text_datas.get_text_data(), HMM=False)

    seg_dict = s_jwf.word_stat(seg_result)
    sf = seg_settings.auto_seg_result_frequency_data
    sc = seg_settings.auto_seg_result_class_data
    if sf and sc:
        for seg in seg_dict:
            if check_word_sign(seg, seg_settings): word_seg_result_datas.add_word_seg_result(seg, seg_dict[seg], s_jwc.pos_tag(seg))
    elif sf and not sc:
        for seg in seg_dict:
            if check_word_sign(seg, seg_settings): word_seg_result_datas.add_word_seg_result(seg, seg_dict[seg], "")
    elif not sf and sc:
        for seg in seg_dict:
            if check_word_sign(seg, seg_settings): word_seg_result_datas.add_word_seg_result(seg, "", s_jwc.pos_tag(seg))
    else:
        for seg in seg_dict:
            if check_word_sign(seg, seg_settings): word_seg_result_datas.add_word_seg_result(seg, "", "")

# 检查词名是否符合设置
def check_word_sign(seg, seg_settings):
    def check_sign(): # 检查是否为标点符号
        for i in seg:
            if unicodedata.category(i).startswith('P'): # 如果发现符号
                return True # 说明这个词有符号
        return False # 没发现

    def check_english(): # 检查是否为英语单词
        for ch in seg:
            if unicodedata.category(ch).startswith('L'):  # 是某种字母
                try:
                    if 'LATIN' in unicodedata.name(ch):
                        return True # 含有拉丁字母
                except ValueError:
                    continue
        return False

    isd = seg_settings.ignore_sign_data
    ied = seg_settings.ignore_english_data
    if isd and ied: # 如果用户想要忽略符号，忽略英文
        if not check_sign() and not check_english(): return True
        else: return False
    elif isd and not ied: # 忽略符号不忽略英文
        if (not check_sign() and check_english()) or (not check_sign() and not check_english()): return True
        else: return False
    elif not isd and ied: # 不忽略符号忽略英文
        if (check_sign() and not check_english()) or (not check_sign() and not check_english()): return True
        else: return False
    else:
        if (check_sign() and check_english()) or (not check_sign() and not check_english()): return True
        else: return False