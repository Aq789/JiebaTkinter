# 预览窗口控制器
from PySide6.QtWidgets import QTableWidgetItem
import app.service.word_class_name as s_wcn
from app.service.pyside6.numeric_table_item import NumericTableItem

# 从分词结果数据导入至左侧表格模块
def input_seg_result_data(preview_window):
    chinese_word_class_data = preview_window.main_window.seg_settings_datas.get_chinese_word_class_data()
    preview_window.seg_result_table.setSortingEnabled(False) # 关闭可排序
    delete_all_table(preview_window.seg_result_table) # 清空表格
    word_seg_result_datas = preview_window.main_window.word_seg_result_datas
    if chinese_word_class_data:
        for data in word_seg_result_datas.return_word_seg_result_list(): # 逐行插入
            insert_table(preview_window.seg_result_table, data.word_name, data.word_frequency, s_wcn.chinese_word_class(data.word_class))
    else:
        for data in word_seg_result_datas.return_word_seg_result_list(): # 逐行插入
            insert_table(preview_window.seg_result_table, data.word_name, data.word_frequency, data.word_class)
    preview_window.seg_result_table.setSortingEnabled(True) # 可排序

# 从词典数据导入至左侧表格模块
def input_dic_data(preview_window):
    delete_all_table(preview_window.dic_table) # 清空表格
    word_dic_datas = preview_window.main_window.word_dic_datas
    for data in word_dic_datas.return_word_dic_list():
        insert_table(preview_window.dic_table, data.word_name, data.word_frequency, data.word_class)

# 导入新行函数
def insert_table(table, word_name, word_frequency, word_class):
    current_row = table.rowCount() # 当前行数
    table.insertRow(current_row) # 插入新行
    table.setItem(current_row, 0, QTableWidgetItem(str(word_name)))
    table.setItem(current_row, 1, NumericTableItem(str(word_frequency)))
    table.setItem(current_row, 2, QTableWidgetItem(str(word_class)))

# 删除所有行函数
def delete_all_table(table):
    table.clearContents() # 清除所有单元格
    table.setRowCount(0) # 重置行数为0
