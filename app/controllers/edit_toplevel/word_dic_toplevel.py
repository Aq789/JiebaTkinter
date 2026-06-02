# 编辑词典控制器
from tkinter import messagebox
import app.controllers.left_frame

# 方法控制保存状态
def is_saved(word_dic_toplevel):
    word_dic_toplevel.word_dic_save_state = True
def not_saved(word_dic_toplevel):
    word_dic_toplevel.word_dic_save_state = False
def return_saved(word_dic_toplevel):
    if word_dic_toplevel.word_dic_save_state: return True
    else: return False

# 将词典数据导入至编辑词典窗口
def input_data(word_dic_toplevel):
    number = 1  # 用来记录序号
    for data in word_dic_toplevel.main_window.word_dic_datas.return_word_dic_list():  # 遍历词典数据
        word_dic_toplevel.show_word_dic_toplevel.insert('', "end",  # 添加到表格中
                                                               values=(number, data.word_name, data.word_frequency, data.word_class))
        number += 1
    return True

# 导出至词典数据前置函数：检查词名列表是否有空值
def refresh_list(word_dic_toplevel):
    start_iid = word_dic_toplevel.show_word_dic_toplevel.insert('', 0)  # 先在开头创建一个元素，存到变量中
    temp_iid = word_dic_toplevel.show_word_dic_toplevel.next(start_iid)  # 循环用到的变量，将开头元素赋值进去
    word_dic_toplevel.show_word_dic_toplevel.delete(start_iid)  # 随后把开头元素删除
    while temp_iid:
        word_name = word_dic_toplevel.show_word_dic_toplevel.set(temp_iid, column="word_name")  # 获取词名
        if not word_name:
            messagebox.showerror("错误", "当前词典中词名存在空值，请修改")
            return False
        next_temp_iid = word_dic_toplevel.show_word_dic_toplevel.next(temp_iid)  # 利用当前元素iid找下一个元素的iid
        temp_iid = next_temp_iid  # 开启下一个循环
    return True

# 将编辑词典窗口数据导出至词典数据
def output_data(word_dic_toplevel):
    if not refresh_list(word_dic_toplevel):
        return False

    word_dic_toplevel.main_window.word_dic_datas.delete_all_word_dic() # 首先删除data中全部元素
    start_iid = word_dic_toplevel.show_word_dic_toplevel.insert('', 0)  # 先在开头创建一个元素，存到变量中
    temp_iid = word_dic_toplevel.show_word_dic_toplevel.next(start_iid)  # 循环用到的变量，将开头元素赋值进去
    word_dic_toplevel.show_word_dic_toplevel.delete(start_iid)  # 随后把开头元素删除
    while temp_iid:
        word_name = word_dic_toplevel.show_word_dic_toplevel.set(temp_iid, column="word_name") # 获取词名
        word_frequency = word_dic_toplevel.show_word_dic_toplevel.set(temp_iid, column="word_frequency") # 获取词频
        word_class = word_dic_toplevel.show_word_dic_toplevel.set(temp_iid, column="word_class") # 获取词性
        word_dic_toplevel.main_window.word_dic_datas.add_word_dic(word_name, word_frequency, word_class) # 将数据传入分词结果data中
        next_temp_iid = word_dic_toplevel.show_word_dic_toplevel.next(temp_iid)  # 利用当前元素iid找下一个元素的iid
        temp_iid = next_temp_iid  # 开启下一个循环
    is_saved(word_dic_toplevel)

    left_frame = word_dic_toplevel.main_window.paned_window.left_frame
    app.controllers.left_frame.input_dic_data(left_frame)
    return True

# 对序号进行排序
def sort_number(word_dic_toplevel):
    start_iid = word_dic_toplevel.show_word_dic_toplevel.insert('', 0)  # 先在开头创建一个元素，存到变量中
    temp_iid = word_dic_toplevel.show_word_dic_toplevel.next(start_iid)  # 循环用到的变量，将开头元素赋值进去
    word_dic_toplevel.show_word_dic_toplevel.delete(start_iid)  # 随后把开头元素删除
    number = 1 # 用来记录序号
    while temp_iid:
        word_dic_toplevel.show_word_dic_toplevel.set(temp_iid, column="id", value=number) # 改变序号
        next_temp_iid = word_dic_toplevel.show_word_dic_toplevel.next(temp_iid) # 利用当前元素iid找下一个元素的iid
        number += 1
        temp_iid = next_temp_iid # 开启下一个循环
    return True

# 移至最前方法
def move_pgup(word_dic_toplevel):
    if word_dic_toplevel.show_word_dic_toplevel.selection(): word_dic_toplevel.select_result_iid = word_dic_toplevel.show_word_dic_toplevel.selection() # 获取当前选中iid
    if len(word_dic_toplevel.select_result_iid) == 1: # 如果只选中一个选项
        select_result = word_dic_toplevel.show_word_dic_toplevel.item(word_dic_toplevel.select_result_iid[0])  # 获取对应选项
        word_dic_toplevel.show_word_dic_toplevel.delete(word_dic_toplevel.select_result_iid[0])  # 删除旧选项
        new_select_result = word_dic_toplevel.show_word_dic_toplevel.insert('', 0, values=select_result['values'], iid=word_dic_toplevel.select_result_iid[0])  # 在表格头部插入新选项，并复制原来选项的iid
        word_dic_toplevel.show_word_dic_toplevel.selection_set(new_select_result) # 象征性地选中移动项
        word_dic_toplevel.show_word_dic_toplevel.see(new_select_result)  # 视图转到新项

        sort_number(word_dic_toplevel)  # 对序号进行排序
        not_saved(word_dic_toplevel)
        refresh_entry(word_dic_toplevel) # 刷新输入框
        return True
    elif len(word_dic_toplevel.select_result_iid) > 1: # 如果选中了多个选项
        messagebox.showerror("错误", "只可选中一个选项进行移动！")
        return False
    else: # 如果没有选中任何选项
        messagebox.showerror("错误", "没有可移动的选项！")
        return False

# 移至最后方法
def move_pgdn(word_dic_toplevel):
    if word_dic_toplevel.show_word_dic_toplevel.selection(): word_dic_toplevel.select_result_iid = word_dic_toplevel.show_word_dic_toplevel.selection() # 获取当前选中iid
    if len(word_dic_toplevel.select_result_iid) == 1: # 如果只选中一个选项
        select_result = word_dic_toplevel.show_word_dic_toplevel.item(word_dic_toplevel.select_result_iid[0]) # 获取对应选项
        word_dic_toplevel.show_word_dic_toplevel.delete(word_dic_toplevel.select_result_iid[0])  # 删除旧选项
        new_select_result = word_dic_toplevel.show_word_dic_toplevel.insert('', "end", values=select_result['values'], iid=word_dic_toplevel.select_result_iid[0]) # 在表格尾部插入新选项，并复制原来选项的iid
        word_dic_toplevel.show_word_dic_toplevel.selection_set(new_select_result) # 象征性地选中移动项
        word_dic_toplevel.show_word_dic_toplevel.see(new_select_result)  # 视图转到新项

        sort_number(word_dic_toplevel)  # 对序号进行排序
        not_saved(word_dic_toplevel)
        refresh_entry(word_dic_toplevel)  # 刷新输入框
        return True
    elif len(word_dic_toplevel.select_result_iid) > 1: # 如果选中了多个选项
        messagebox.showerror("错误", "只可选中一个选项进行移动！")
        return False
    else: # 如果没有选中任何选项
        messagebox.showerror("错误", "没有可移动的选项！")
        return False

# 向前移动
def move_up(word_dic_toplevel):
    if word_dic_toplevel.show_word_dic_toplevel.selection(): word_dic_toplevel.select_result_iid = word_dic_toplevel.show_word_dic_toplevel.selection() # 获取当前选中iid
    if len(word_dic_toplevel.select_result_iid) == 1:
        select_result = word_dic_toplevel.show_word_dic_toplevel.item(word_dic_toplevel.select_result_iid[0]) # 获取对应选项
        prev_select_result_index = word_dic_toplevel.show_word_dic_toplevel.index(word_dic_toplevel.show_word_dic_toplevel.prev(word_dic_toplevel.select_result_iid[0])) # 获取前一个元素的索引
        word_dic_toplevel.show_word_dic_toplevel.delete(word_dic_toplevel.select_result_iid[0])  # 删除原来元素
        new_select_result = word_dic_toplevel.show_word_dic_toplevel.insert('', prev_select_result_index, values=select_result['values'], iid=word_dic_toplevel.select_result_iid[0]) # 在索引处添加想要移动的对象，并复制原来选项的iid
        word_dic_toplevel.show_word_dic_toplevel.selection_set(new_select_result) # 象征性地选中移动项
        word_dic_toplevel.show_word_dic_toplevel.see(new_select_result)  # 视图转到新项

        sort_number(word_dic_toplevel) # 对序号进行排序
        not_saved(word_dic_toplevel)
        refresh_entry(word_dic_toplevel)  # 刷新输入框
        return True
    elif len(word_dic_toplevel.select_result_iid) > 1:
        messagebox.showerror("错误", "只可选中一个选项进行移动！")
        return False
    else:
        messagebox.showerror("错误", "没有可移动的选项！")
        return False

# 向后移动
def move_down(word_dic_toplevel):
    if word_dic_toplevel.show_word_dic_toplevel.selection(): word_dic_toplevel.select_result_iid = word_dic_toplevel.show_word_dic_toplevel.selection() # 获取当前选中iid
    if len(word_dic_toplevel.select_result_iid) == 1:
        select_result = word_dic_toplevel.show_word_dic_toplevel.item(word_dic_toplevel.select_result_iid[0])  # 获取对应选项
        next_select_result_index = word_dic_toplevel.show_word_dic_toplevel.index(
            word_dic_toplevel.show_word_dic_toplevel.next(word_dic_toplevel.select_result_iid[0]))  # 获取后一个元素的索引
        word_dic_toplevel.show_word_dic_toplevel.delete(word_dic_toplevel.select_result_iid[0])  # 删除原来元素
        new_select_result = word_dic_toplevel.show_word_dic_toplevel.insert('', next_select_result_index, values=select_result['values'], iid=word_dic_toplevel.select_result_iid[0])  # 在索引处添加想要移动的对象，并复制原来选项的iid
        word_dic_toplevel.show_word_dic_toplevel.selection_set(new_select_result)  # 象征性地选中移动项
        word_dic_toplevel.show_word_dic_toplevel.see(new_select_result) # 视图转到新项

        sort_number(word_dic_toplevel)  # 对序号进行排序
        not_saved(word_dic_toplevel)
        refresh_entry(word_dic_toplevel)  # 刷新输入框
        return True
    elif len(word_dic_toplevel.select_result_iid) > 1:
        messagebox.showerror("错误", "只可选中一个选项进行移动！")
        return False
    else:
        messagebox.showerror("错误", "没有可移动的选项！")
        return False

# 删除所选元素
def delete_select_results(word_dic_toplevel):
    if word_dic_toplevel.show_word_dic_toplevel.selection(): word_dic_toplevel.select_result_iid = word_dic_toplevel.show_word_dic_toplevel.selection() # 获取对应选项
    if word_dic_toplevel.select_result_iid:
        ask_delete_yesno = messagebox.askyesno("确认", "是否删除所选内容（不可恢复）？")
        if ask_delete_yesno:
            for temp_select_result_iid in word_dic_toplevel.select_result_iid: # 遍历选中元组
                word_dic_toplevel.show_word_dic_toplevel.delete(temp_select_result_iid) # 删除元素
            word_dic_toplevel.select_result_iid = () # 将选中元素列表置空

            sort_number(word_dic_toplevel)  # 对序号进行排序
            not_saved(word_dic_toplevel)
            refresh_entry(word_dic_toplevel)  # 刷新输入框
            return True
        else:
            return False
    else:
        messagebox.showerror("错误", "没有可删除的选项！")
        return False

# 刷新词名输入框
def refresh_entry(word_dic_toplevel):
    word_dic_toplevel.select_result_iid = word_dic_toplevel.show_word_dic_toplevel.selection()
    if len(word_dic_toplevel.select_result_iid) == 1:
        select_list = word_dic_toplevel.show_word_dic_toplevel.item(word_dic_toplevel.select_result_iid[0])['values']
        word_dic_toplevel.word_name_entry.delete(first=0, last="end")  # 清空输入框
        word_dic_toplevel.word_frequency_entry.delete(first=0, last="end")
        word_dic_toplevel.word_class_entry.delete(first=0, last="end")
        word_dic_toplevel.word_name_entry.insert("end", select_list[1]) # 插入输入框
        word_dic_toplevel.word_frequency_entry.insert("end", select_list[2])
        word_dic_toplevel.word_class_entry.insert("end", select_list[3])
    else:
        word_dic_toplevel.word_name_entry.delete(first=0, last="end")  # 清空输入框
        word_dic_toplevel.word_frequency_entry.delete(first=0, last="end")
        word_dic_toplevel.word_class_entry.delete(first=0, last="end")

# 输入框变化事件
def entry_change(word_dic_toplevel):
    word_dic_toplevel.select_result_iid = word_dic_toplevel.show_word_dic_toplevel.selection() # 获取当前选中项并赋值

    word_name = word_dic_toplevel.word_name_var.get() # 获取文本框内容
    word_frequency = word_dic_toplevel.word_frequency_var.get()
    word_class = word_dic_toplevel.word_class_var.get()

    if word_dic_toplevel.last_word_name and word_dic_toplevel.last_word_frequency and word_dic_toplevel.last_word_class and word_name and word_frequency and word_class and word_dic_toplevel.show_word_dic_toplevel.selection() == word_dic_toplevel.last_select_result_iid: # 如果选项没有变化但是内容发生了变化
        if word_name != word_dic_toplevel.last_word_name or word_frequency != word_dic_toplevel.last_word_frequency or word_class != word_dic_toplevel.last_word_class:
            not_saved(word_dic_toplevel) # 将保存状态置为未保存状态

    if len(word_dic_toplevel.select_result_iid) == 1: # 如果只选中一项
        word_dic_toplevel.show_word_dic_toplevel.set(word_dic_toplevel.select_result_iid[0], column='word_name', value=word_name) # 改变表中内容
        word_dic_toplevel.show_word_dic_toplevel.set(word_dic_toplevel.select_result_iid[0], column='word_frequency', value=word_frequency)
        word_dic_toplevel.show_word_dic_toplevel.set(word_dic_toplevel.select_result_iid[0], column='word_class', value=word_class)

        word_dic_toplevel.last_select_result_iid = word_dic_toplevel.select_result_iid # 将上一个选项内容赋值
        word_dic_toplevel.last_word_name = word_name
        word_dic_toplevel.last_word_frequency = word_frequency
        word_dic_toplevel.last_word_class = word_class
    else:
        return

def create_word_dic(word_dic_toplevel):
    # 获取当前选中的索引，如果没有或者多选的情况下就在尾部添加
    if len(word_dic_toplevel.select_result_iid) == 1:
        select_result_index = word_dic_toplevel.show_word_dic_toplevel.index(word_dic_toplevel.show_word_dic_toplevel.next(word_dic_toplevel.select_result_iid[0])) # 获取选中元素下一个的索引
        if select_result_index == 0: new_word_dic = word_dic_toplevel.show_word_dic_toplevel.insert('', "end", values=(0, "", "", "")) # 特殊情况：如果选中元素为末尾元素，需要在最后添加
        else: new_word_dic = word_dic_toplevel.show_word_dic_toplevel.insert('', select_result_index, values=(0, "", "", ""))
    else:
        new_word_dic = word_dic_toplevel.show_word_dic_toplevel.insert('', "end", values=(0, "", "", ""))
    sort_number(word_dic_toplevel) # 对序号进行排序
    word_dic_toplevel.show_word_dic_toplevel.selection_set(new_word_dic)  # 象征性地选中新建项
    word_dic_toplevel.select_result_iid = (new_word_dic, ) # 选中新建项
    word_dic_toplevel.show_word_dic_toplevel.see(new_word_dic)  # 视图转到新项
    not_saved(word_dic_toplevel) # 未保存状态
    refresh_entry(word_dic_toplevel) # 刷新输入框
    word_dic_toplevel.word_name_entry.focus_set() # 文本框获得焦点

# 查找分词结果
def search_result(word_dic_toplevel):
    search_entry = word_dic_toplevel.search_entry.get() # 获取输入框中的文本
    if not search_entry:
        messagebox.showinfo("提示", "当前搜索框内容为空！")
        return False

    start_iid = word_dic_toplevel.show_word_dic_toplevel.insert('', 0) # 先在开头创建一个元素，存到变量中
    temp_iid = word_dic_toplevel.show_word_dic_toplevel.next(start_iid) # 循环用到的变量，将开头元素赋值进去
    word_dic_toplevel.show_word_dic_toplevel.delete(start_iid)  # 随后把开头元素删除

    search_result_select = [] # 列表，用来记录查找结果的iid
    while temp_iid:
        temp_result = word_dic_toplevel.show_word_dic_toplevel.item(temp_iid) # 返回当前元素item
        if search_entry in temp_result['values'][1]: # 如果当前词名中含有搜索文本
            search_result_select.append(temp_iid) # 将对应iid加入列表
        next_temp_iid = word_dic_toplevel.show_word_dic_toplevel.next(temp_iid) # 利用当前元素iid找下一个元素的iid
        temp_iid = next_temp_iid # 开启下一个循环

    if not search_result_select: # 如果没找到词典
        messagebox.showerror("错误", "未找到词典结果")
        return False
    else:
        word_dic_toplevel.select_result_iid = tuple(search_result_select) # 将查找结果iid给全局变量，选中元素元组
        word_dic_toplevel.show_word_dic_toplevel.selection_set(word_dic_toplevel.select_result_iid) # 象征性选中查找结果
        word_dic_toplevel.show_word_dic_toplevel.see(word_dic_toplevel.select_result_iid[0]) # 视图转到查找结果的第一项
        return True