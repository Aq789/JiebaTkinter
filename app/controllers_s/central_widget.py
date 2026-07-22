# 文本框控制器

# 将文本上传至数据集
def text_to_data(central_widget):
    central_widget.main_window.text_datas.set_text_data(central_widget.text_edit.toPlainText())