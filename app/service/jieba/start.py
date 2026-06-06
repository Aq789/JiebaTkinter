# jieba分词函数
import jieba
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
    if seg_settings.auto_seg_result_frequency_data: # 如果开启词频统计
        if seg_settings.auto_seg_result_class_data: # 如果开启词性标注
            for seg in seg_dict:
                word_seg_result_datas.add_word_seg_result(seg, seg_dict[seg], s_jwc.pos_tag(seg))
        else:
            for seg in seg_dict:
                word_seg_result_datas.add_word_seg_result(seg, seg_dict[seg], "")
    else:
        if seg_settings.auto_seg_result_class_data:  # 如果开启词性标注
            for seg in seg_dict:
                word_seg_result_datas.add_word_seg_result(seg, "", s_jwc.pos_tag(seg))
        else:
            for seg in seg_dict:
                word_seg_result_datas.add_word_seg_result(seg, "", "")