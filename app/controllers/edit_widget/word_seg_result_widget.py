# 编辑分词结果控制器
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QInputDialog

from service.pyside6.numeric_table_item import NumericTableItem
import app.service.word_class_name as s_wcn
import app.controllers.preview_window as c_pw


# 导入新行函数
def insert_table(table, word_name, word_frequency, word_class):
    current_row = table.rowCount() # 当前行数
    table.insertRow(current_row) # 插入新行
    table.setItem(current_row, 0, QTableWidgetItem(str(word_name)))
    table.setItem(current_row, 1, NumericTableItem(str(word_frequency)))
    table.setItem(current_row, 2, QTableWidgetItem(str(word_class)))
    return True

# 删除所有行函数
def delete_all_table(table):
    table.clearContents() # 清除所有单元格
    table.setRowCount(0) # 重置行数为0
    return True

# 将数据集中的数据导入至表格中
def input_seg_result_data(word_seg_result_widget):
    chinese_word_class_setting_data = word_seg_result_widget.main_window.seg_settings_datas.get_chinese_word_class_data()
    seg_result_datas = word_seg_result_widget.main_window.word_seg_result_datas.return_word_seg_result_list()
    table = word_seg_result_widget.word_seg_result_table

    delete_all_table(table)
    table.setSortingEnabled(False)

    for data in seg_result_datas:
        if chinese_word_class_setting_data:
            insert_table(table, data.word_name, data.word_frequency, s_wcn.chinese_word_class(data.word_class))
        else:
            insert_table(table, data.word_name, data.word_frequency, data.word_class)
    status_refresh(word_seg_result_widget)
    table.setSortingEnabled(True)
    return True

# 将表格中的数据导出至数据集中
def output_seg_result_data(word_seg_result_widget):
    table = word_seg_result_widget.word_seg_result_table
    word_seg_result_datas = word_seg_result_widget.main_window.word_seg_result_datas
    seg_settings_datas = word_seg_result_widget.main_window.seg_settings_datas

    row_count = table.rowCount()

    word_seg_result_datas.delete_all_word_seg_result()
    for row in range(row_count):
        word_name = table.item(row, 0).text()
        word_frequency = int(table.item(row, 1).text())
        if seg_settings_datas.get_chinese_word_class_data():
            word_class = s_wcn.simple_word_class(table.item(row, 2).text())
        else:
            word_class = table.item(row, 2).text()
        word_seg_result_datas.add_word_seg_result(word_name, word_frequency, word_class)

    status_refresh(word_seg_result_widget)
    save_refresh(word_seg_result_widget, True)
    c_pw.input_seg_result_data(word_seg_result_widget.main_window.dock_widget.preview_window)
    word_seg_result_widget.main_window.change_saved(False)

# 删除数据方法
def delete_current_row(word_seg_result_widget):
    widget = word_seg_result_widget.word_seg_result_widget
    table = word_seg_result_widget.word_seg_result_table

    selected_rows = set()
    for index in table.selectedIndexes():
        selected_rows.add(index.row())

    if not selected_rows:
        QMessageBox.warning(widget, "提示", "未选中任何数据！")
        return False

    reply = QMessageBox.question(widget, "确认", "确定删除所选项吗？", QMessageBox.Yes | QMessageBox.No)
    if reply == QMessageBox.No:
        return False
    else:
        for row in sorted(selected_rows, reverse=True):
            table.removeRow(row)
        widget.statusBar().showMessage(f"成功删除 {len(selected_rows)} 项", 2000)
        save_refresh(word_seg_result_widget, False)
        status_refresh(word_seg_result_widget)
        return True

# 查找数据方法
def check_datas(word_seg_result_widget):
    widget = word_seg_result_widget.word_seg_result_widget

    if not word_seg_result_widget.check_action.isChecked():
        search_datas(word_seg_result_widget, "", True)
    else:
        search_data, ok = QInputDialog.getText(widget, "查找", "请输入想要查找的内容：")
        search_datas(word_seg_result_widget, search_data, ok)

# 关键字查找方法
def search_datas(word_seg_result_widget, search_data, ok):
    table = word_seg_result_widget.word_seg_result_table
    row_count = table.rowCount()

    if not ok:
        word_seg_result_widget.check_action.setChecked(False)
        return

    if not search_data or not search_data.strip():
        for row in range(row_count):
            table.setRowHidden(row, False)
        return

    search_data = search_data.strip()
    col_count = table.columnCount()
    for row in range(row_count):
        if not search_data:
            table.setRowHidden(row, False)
            continue
        found = False
        for col in range(col_count):
            item = table.item(row, col)
            if item is None:
                continue
            if search_data in item.text():
                found = True
                break
        table.setRowHidden(row, not found)
    return

# 状态栏更新函数
def status_refresh(word_seg_result_widget):
    table = word_seg_result_widget.word_seg_result_table

    row_count = table.rowCount()
    select_count = on_selection_changed(word_seg_result_widget)
    if select_count == 0:
        word_seg_result_widget.state_label.setText(f"总计 {row_count} 项")
    else:
        word_seg_result_widget.state_label.setText(f"总计 {row_count} 项  选中 {select_count} 项")

# 保存更新函数
def save_refresh(word_seg_result_widget, state):
    if state:
        word_seg_result_widget.saved = True
        word_seg_result_widget.save_state.setText("已保存")
    else:
        word_seg_result_widget.saved = False
        word_seg_result_widget.save_state.setText("未保存")

# 选中行数统计方法
def on_selection_changed(word_seg_result_widget):
    table = word_seg_result_widget.word_seg_result_table

    selected_rows = set()
    for index in table.selectedIndexes():
        selected_rows.add(index.row())
    row_count = len(selected_rows)
    return row_count