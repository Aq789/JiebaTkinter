# 文本框控制器

# 此函数将文字上传至数据集
def text_to_data(right_frame):
    right_frame.main_window.text_datas.set_text_data(right_frame.text.get("1.0", "end"))