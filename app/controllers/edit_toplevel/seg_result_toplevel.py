# 编辑分词结果控制器
from tkinter import messagebox
import app.controllers.left_frame

# Treeview 注意有三种要素：选项、iid、索引。分别对应 item iid index

# 方法控制保存状态
def is_saved(seg_result_toplevel):
    seg_result_toplevel.seg_result_save_state = True
def not_saved(seg_result_toplevel):
    seg_result_toplevel.seg_result_save_state = False
def return_saved(seg_result_toplevel):
    if seg_result_toplevel.seg_result_save_state: return True
    else: return False

# 将分词结果数据导入至编辑分词结果窗口
def input_data(seg_result_toplevel):
    number = 1 # 用来记录序号
    for data in seg_result_toplevel.main_window.word_seg_result_datas.return_word_seg_result_list(): # 遍历分词结果数据
        seg_result_toplevel.show_word_seg_result_toplevel.insert('', "end",  # 添加到表格中
                                                                 values=(number, data.word_name, data.word_frequency, data.word_class))
        number += 1
    return True

# 将编辑分词结果窗口数据导出至分词结果数据
def output_data(seg_result_toplevel):
    seg_result_toplevel.main_window.word_seg_result_datas.delete_all_word_seg_result() # 首先删除data中全部元素
    start_iid = seg_result_toplevel.show_word_seg_result_toplevel.insert('', 0)  # 先在开头创建一个元素，存到变量中
    temp_iid = seg_result_toplevel.show_word_seg_result_toplevel.next(start_iid)  # 循环用到的变量，将开头元素赋值进去
    seg_result_toplevel.show_word_seg_result_toplevel.delete(start_iid)  # 随后把开头元素删除
    while temp_iid:
        word_name = seg_result_toplevel.show_word_seg_result_toplevel.set(temp_iid, column="word_name") # 获取词名
        word_frequency = seg_result_toplevel.show_word_seg_result_toplevel.set(temp_iid, column="word_frequency") # 获取词频
        word_class = seg_result_toplevel.show_word_seg_result_toplevel.set(temp_iid, column="word_class") # 获取词性
        seg_result_toplevel.main_window.word_seg_result_datas.add_word_seg_result(word_name, word_frequency, word_class) # 将数据传入分词结果data中
        next_temp_iid = seg_result_toplevel.show_word_seg_result_toplevel.next(temp_iid)  # 利用当前元素iid找下一个元素的iid
        temp_iid = next_temp_iid  # 开启下一个循环
    is_saved(seg_result_toplevel)

    left_frame = seg_result_toplevel.main_window.paned_window.left_frame
    app.controllers.left_frame.input_seg_result_data(left_frame)
    return True

# 对序号进行排序
def sort_number(seg_result_toplevel):
    start_iid = seg_result_toplevel.show_word_seg_result_toplevel.insert('', 0)  # 先在开头创建一个元素，存到变量中
    temp_iid = seg_result_toplevel.show_word_seg_result_toplevel.next(start_iid)  # 循环用到的变量，将开头元素赋值进去
    seg_result_toplevel.show_word_seg_result_toplevel.delete(start_iid)  # 随后把开头元素删除
    number = 1 # 用来记录序号
    while temp_iid:
        seg_result_toplevel.show_word_seg_result_toplevel.set(temp_iid, column="id", value=number) # 改变序号
        next_temp_iid = seg_result_toplevel.show_word_seg_result_toplevel.next(temp_iid) # 利用当前元素iid找下一个元素的iid
        number += 1
        temp_iid = next_temp_iid # 开启下一个循环
    return True

# 移至最前方法
def move_pgup(seg_result_toplevel):
    if seg_result_toplevel.show_word_seg_result_toplevel.selection(): seg_result_toplevel.select_result_iid = seg_result_toplevel.show_word_seg_result_toplevel.selection() # 获取当前选中iid
    if len(seg_result_toplevel.select_result_iid) == 1: # 如果只选中一个选项
        select_result = seg_result_toplevel.show_word_seg_result_toplevel.item(seg_result_toplevel.select_result_iid[0])  # 获取对应选项
        seg_result_toplevel.show_word_seg_result_toplevel.delete(seg_result_toplevel.select_result_iid[0])  # 删除旧选项
        new_select_result = seg_result_toplevel.show_word_seg_result_toplevel.insert('', 0, values=select_result['values'], iid=seg_result_toplevel.select_result_iid[0])  # 在表格头部插入新选项，并复制原来选项的iid
        seg_result_toplevel.show_word_seg_result_toplevel.selection_set(new_select_result) # 象征性地选中移动项
        seg_result_toplevel.show_word_seg_result_toplevel.see(new_select_result)  # 视图转到新项
        sort_number(seg_result_toplevel)  # 对序号进行排序
        not_saved(seg_result_toplevel)
        return True
    elif len(seg_result_toplevel.select_result_iid) > 1: # 如果选中了多个选项
        messagebox.showerror("错误", "只可选中一个选项进行移动！")
        return False
    else: # 如果没有选中任何选项
        messagebox.showerror("错误", "没有可移动的选项！")
        return False

# 移至最后方法
def move_pgdn(seg_result_toplevel):
    if seg_result_toplevel.show_word_seg_result_toplevel.selection(): seg_result_toplevel.select_result_iid = seg_result_toplevel.show_word_seg_result_toplevel.selection() # 获取当前选中iid
    if len(seg_result_toplevel.select_result_iid) == 1: # 如果只选中一个选项
        select_result = seg_result_toplevel.show_word_seg_result_toplevel.item(seg_result_toplevel.select_result_iid[0]) # 获取对应选项
        seg_result_toplevel.show_word_seg_result_toplevel.delete(seg_result_toplevel.select_result_iid[0])  # 删除旧选项
        new_select_result = seg_result_toplevel.show_word_seg_result_toplevel.insert('', "end", values=select_result['values'], iid=seg_result_toplevel.select_result_iid[0]) # 在表格尾部插入新选项，并复制原来选项的iid
        seg_result_toplevel.show_word_seg_result_toplevel.selection_set(new_select_result) # 象征性地选中移动项
        seg_result_toplevel.show_word_seg_result_toplevel.see(new_select_result)  # 视图转到新项
        sort_number(seg_result_toplevel)  # 对序号进行排序
        not_saved(seg_result_toplevel)
        return True
    elif len(seg_result_toplevel.select_result_iid) > 1: # 如果选中了多个选项
        messagebox.showerror("错误", "只可选中一个选项进行移动！")
        return False
    else: # 如果没有选中任何选项
        messagebox.showerror("错误", "没有可移动的选项！")
        return False

# 向前移动
def move_up(seg_result_toplevel):
    if seg_result_toplevel.show_word_seg_result_toplevel.selection(): seg_result_toplevel.select_result_iid = seg_result_toplevel.show_word_seg_result_toplevel.selection() # 获取当前选中iid
    if len(seg_result_toplevel.select_result_iid) == 1:
        select_result = seg_result_toplevel.show_word_seg_result_toplevel.item(seg_result_toplevel.select_result_iid[0]) # 获取对应选项
        prev_select_result_index = seg_result_toplevel.show_word_seg_result_toplevel.index(seg_result_toplevel.show_word_seg_result_toplevel.prev(seg_result_toplevel.select_result_iid[0])) # 获取前一个元素的索引
        seg_result_toplevel.show_word_seg_result_toplevel.delete(seg_result_toplevel.select_result_iid[0])  # 删除原来元素
        new_select_result = seg_result_toplevel.show_word_seg_result_toplevel.insert('', prev_select_result_index, values=select_result['values'], iid=seg_result_toplevel.select_result_iid[0]) # 在索引处添加想要移动的对象，并复制原来选项的iid
        seg_result_toplevel.show_word_seg_result_toplevel.selection_set(new_select_result) # 象征性地选中移动项
        seg_result_toplevel.show_word_seg_result_toplevel.see(new_select_result)  # 视图转到新项
        sort_number(seg_result_toplevel) # 对序号进行排序
        not_saved(seg_result_toplevel)
        return True
    elif len(seg_result_toplevel.select_result_iid) > 1:
        messagebox.showerror("错误", "只可选中一个选项进行移动！")
        return False
    else:
        messagebox.showerror("错误", "没有可移动的选项！")
        return False

# 向后移动
def move_down(seg_result_toplevel):
    if seg_result_toplevel.show_word_seg_result_toplevel.selection(): seg_result_toplevel.select_result_iid = seg_result_toplevel.show_word_seg_result_toplevel.selection() # 获取当前选中iid
    if len(seg_result_toplevel.select_result_iid) == 1:
        select_result = seg_result_toplevel.show_word_seg_result_toplevel.item(seg_result_toplevel.select_result_iid[0])  # 获取对应选项
        next_select_result_index = seg_result_toplevel.show_word_seg_result_toplevel.index(
            seg_result_toplevel.show_word_seg_result_toplevel.next(seg_result_toplevel.select_result_iid[0]))  # 获取后一个元素的索引
        seg_result_toplevel.show_word_seg_result_toplevel.delete(seg_result_toplevel.select_result_iid[0])  # 删除原来元素
        new_select_result = seg_result_toplevel.show_word_seg_result_toplevel.insert('', next_select_result_index, values=select_result['values'], iid=seg_result_toplevel.select_result_iid[0])  # 在索引处添加想要移动的对象，并复制原来选项的iid
        seg_result_toplevel.show_word_seg_result_toplevel.selection_set(new_select_result)  # 象征性地选中移动项
        seg_result_toplevel.show_word_seg_result_toplevel.see(new_select_result) # 视图转到新项
        sort_number(seg_result_toplevel)  # 对序号进行排序
        not_saved(seg_result_toplevel)
        return True
    elif len(seg_result_toplevel.select_result_iid) > 1:
        messagebox.showerror("错误", "只可选中一个选项进行移动！")
        return False
    else:
        messagebox.showerror("错误", "没有可移动的选项！")
        return False

# 删除所选元素
def delete_select_results(seg_result_toplevel):
    if seg_result_toplevel.show_word_seg_result_toplevel.selection(): seg_result_toplevel.select_result_iid = seg_result_toplevel.show_word_seg_result_toplevel.selection() # 获取对应选项
    if seg_result_toplevel.select_result_iid:
        ask_delete_yesno = messagebox.askyesno("确认", "是否删除所选内容（不可恢复）？")
        if ask_delete_yesno:
            for temp_select_result_iid in seg_result_toplevel.select_result_iid: # 遍历选中元组
                seg_result_toplevel.show_word_seg_result_toplevel.delete(temp_select_result_iid) # 删除元素
            seg_result_toplevel.select_result_iid = () # 将选中元素列表置空
            sort_number(seg_result_toplevel)  # 对序号进行排序
            not_saved(seg_result_toplevel)
            return True
        else:
            return False
    else:
        messagebox.showerror("错误", "没有可删除的选项！")
        return False

# 查找分词结果
def search_result(seg_result_toplevel):
    search_entry = seg_result_toplevel.search_entry.get() # 获取输入框中的文本
    if not search_entry:
        messagebox.showinfo("提示", "当前搜索框内容为空！")
        return False

    start_iid = seg_result_toplevel.show_word_seg_result_toplevel.insert('', 0) # 先在开头创建一个元素，存到变量中
    temp_iid = seg_result_toplevel.show_word_seg_result_toplevel.next(start_iid) # 循环用到的变量，将开头元素赋值进去
    seg_result_toplevel.show_word_seg_result_toplevel.delete(start_iid)  # 随后把开头元素删除

    search_result_select = [] # 列表，用来记录查找结果的iid
    while temp_iid:
        temp_result = seg_result_toplevel.show_word_seg_result_toplevel.item(temp_iid) # 返回当前元素item
        if search_entry in temp_result['values'][1]: # 如果当前词名中含有搜索文本
            search_result_select.append(temp_iid) # 将对应iid加入列表
        next_temp_iid = seg_result_toplevel.show_word_seg_result_toplevel.next(temp_iid) # 利用当前元素iid找下一个元素的iid
        temp_iid = next_temp_iid # 开启下一个循环

    if not search_result_select: # 如果没找到分词结果
        ask_search_yesno = messagebox.askyesno("确认", "未找到结果，是否创建？")
        if ask_search_yesno: # 如果用户选择查找
            '''在此添加在分词中查找的逻辑'''
            messagebox.showinfo("提示", "正在查找分词结果……")
            return True
        else:
            return False
    else:
        seg_result_toplevel.select_result_iid = tuple(search_result_select) # 将查找结果iid给全局变量，选中元素元组
        seg_result_toplevel.show_word_seg_result_toplevel.selection_set(seg_result_toplevel.select_result_iid) # 象征性选中查找结果
        seg_result_toplevel.show_word_seg_result_toplevel.see(seg_result_toplevel.select_result_iid[0]) # 视图转到查找结果的第一项
        return True