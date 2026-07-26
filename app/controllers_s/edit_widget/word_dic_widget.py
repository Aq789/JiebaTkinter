# 编辑词典控制器
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QInputDialog, QAbstractItemView

from service.pyside6.numeric_table_item import NumericTableItem
import app.controllers_s.preview_window as c_pw


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
def input_dic_data(word_dic_widget):
    dic_datas = word_dic_widget.main_window.word_dic_datas.return_word_dic_list()
    table = word_dic_widget.word_dic_table

    delete_all_table(table)
    table.setSortingEnabled(False)

    for data in dic_datas:
        insert_table(table, data.word_name, data.word_frequency, data.word_class)
    status_refresh(word_dic_widget)
    table.setSortingEnabled(True)
    return True

# 将表格中的数据导出至数据集中
def output_dic_data(word_dic_widget):
    table = word_dic_widget.word_dic_table
    word_dic_datas = word_dic_widget.main_window.word_dic_datas

    row_count = table.rowCount()

    word_dic_datas.delete_all_word_dic()
    for row in range(row_count):
        word_name = table.item(row, 0).text()
        word_frequency = int(table.item(row, 1).text())
        word_class = table.item(row, 2).text()
        word_dic_datas.add_word_dic(word_name, word_frequency, word_class)

    status_refresh(word_dic_widget)
    save_refresh(word_dic_widget, True)
    c_pw.input_dic_data(word_dic_widget.main_window.dock_widget.preview_window)

# 在表格中添加数据方法
def new_row(table, row):
    table.insertRow(row)
    table.setItem(row, 0, QTableWidgetItem("新词典"))
    table.selectRow(row)
    table.scrollTo(table.currentIndex(), QAbstractItemView.ScrollHint.PositionAtCenter)
    table.edit(table.currentIndex())

# 新建数据方法
def create_dic_data(word_dic_widget):
    table = word_dic_widget.word_dic_table

    selected_rows = set()
    for index in table.selectedIndexes():
        selected_rows.add(index.row())

    if len(selected_rows) == 1:
        selected_row = next(iter(selected_rows))
        new_row(table, selected_row + 1)
    else:
        new_row(table, table.rowCount())

# 删除数据方法
def delete_current_row(word_dic_widget):
    widget = word_dic_widget.word_dic_widget
    table = word_dic_widget.word_dic_table

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
        save_refresh(word_dic_widget, False)
        status_refresh(word_dic_widget)
        return True

# 查找数据方法
def check_datas(word_dic_widget):
    widget = word_dic_widget.word_dic_widget

    if not word_dic_widget.check_action.isChecked():
        search_datas(word_dic_widget, "", True)
    else:
        search_data, ok = QInputDialog.getText(widget, "查找", "请输入想要查找的内容：")
        search_datas(word_dic_widget, search_data, ok)

# 关键字查找方法
def search_datas(word_dic_widget, search_data, ok):
    table = word_dic_widget.word_dic_table
    row_count = table.rowCount()

    if not ok:
        word_dic_widget.check_action.setChecked(False)
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
def status_refresh(word_dic_widget):
    table = word_dic_widget.word_dic_table

    row_count = table.rowCount()
    select_count = on_selection_changed(word_dic_widget)
    if select_count == 0:
        word_dic_widget.state_label.setText(f"总计 {row_count} 项")
    else:
        word_dic_widget.state_label.setText(f"总计 {row_count} 项  选中 {select_count} 项")

# 选中行数统计方法
def on_selection_changed(word_dic_widget):
    table = word_dic_widget.word_dic_table

    select_rows = set()
    for index in table.selectedIndexes():
        select_rows.add(index.row())
    row_count = len(select_rows)
    return row_count

# 保存更新函数
def save_refresh(word_dic_widget, state):
    if state:
        word_dic_widget.saved = True
        word_dic_widget.save_state.setText("已保存")
    else:
        word_dic_widget.saved = False
        word_dic_widget.save_state.setText("未保存")
