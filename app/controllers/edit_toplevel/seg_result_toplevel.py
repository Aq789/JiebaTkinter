# 编辑分词结果控制器
import app.datas.word_seg_result as d_wsr

# 将分词结果数据导入编辑分词结果窗口
def input_data(edit_window):
    number = 1
    for data in d_wsr.word_seg_result_list:
        edit_window.show_word_seg_result_toplevel.insert('', "end",
                                                         values=(number, data.word_name, data.word_frequency, data.word_class))
        number += 1