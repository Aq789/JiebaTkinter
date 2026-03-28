# 编辑分词结果控制器
from tkinter import messagebox
import app.datas.word_seg_result as d_wsr
select_result_iid = None
# Treeview 注意有三种要素：选项、iid、索引。分别对应 item iid index

# 将分词结果数据导入编辑分词结果窗口
def input_data(edit_window):
    number = 1 # 用来记录序号
    for data in d_wsr.word_seg_result_list: # 遍历分词结果数据
        edit_window.show_word_seg_result_toplevel.insert('', "end", # 添加到表格中
                                                         values=(number, data.word_name, data.word_frequency, data.word_class))
        number += 1
    return True

# 移至最前方法
def move_pgup(edit_window):
    global select_result_iid
    if edit_window.show_word_seg_result_toplevel.selection(): select_result_iid = edit_window.show_word_seg_result_toplevel.selection() # 获取当前选中iid
    if len(select_result_iid) == 1: # 如果只选中一个选项
        select_result = edit_window.show_word_seg_result_toplevel.item(select_result_iid[0])  # 获取对应选项
        edit_window.show_word_seg_result_toplevel.delete(select_result_iid[0])  # 删除旧选项
        new_select_result = edit_window.show_word_seg_result_toplevel.insert('', 0, values=select_result['values'], iid=select_result_iid[0])  # 在表格头部插入新选项，并复制原来选项的iid
        edit_window.show_word_seg_result_toplevel.selection_set(new_select_result) # 象征性地选中移动项
        edit_window.show_word_seg_result_toplevel.see(new_select_result)  # 视图转到新项
        return True
    elif len(select_result_iid) > 1: # 如果选中了多个选项
        messagebox.showerror("错误", "只可选中一个选项进行移动！")
        return False
    else: # 如果没有选中任何选项
        messagebox.showerror("错误", "没有可移动的选项！")
        return False

# 移至最后方法
def move_pgdn(edit_window):
    global select_result_iid
    if edit_window.show_word_seg_result_toplevel.selection(): select_result_iid = edit_window.show_word_seg_result_toplevel.selection() # 获取当前选中iid
    if len(select_result_iid) == 1: # 如果只选中一个选项
        select_result = edit_window.show_word_seg_result_toplevel.item(select_result_iid[0]) # 获取对应选项
        edit_window.show_word_seg_result_toplevel.delete(select_result_iid[0])  # 删除旧选项
        new_select_result = edit_window.show_word_seg_result_toplevel.insert('', "end", values=select_result['values'], iid=select_result_iid[0]) # 在表格尾部插入新选项，并复制原来选项的iid
        edit_window.show_word_seg_result_toplevel.selection_set(new_select_result) # 象征性地选中移动项
        edit_window.show_word_seg_result_toplevel.see(new_select_result)  # 视图转到新项
        return True
    elif len(select_result_iid) > 1: # 如果选中了多个选项
        messagebox.showerror("错误", "只可选中一个选项进行移动！")
        return False
    else: # 如果没有选中任何选项
        messagebox.showerror("错误", "没有可移动的选项！")
        return False

# 向前移动
def move_up(edit_window):
    global select_result_iid
    if edit_window.show_word_seg_result_toplevel.selection(): select_result_iid = edit_window.show_word_seg_result_toplevel.selection() # 获取当前选中iid
    if len(select_result_iid) == 1:
        select_result = edit_window.show_word_seg_result_toplevel.item(select_result_iid[0]) # 获取对应选项
        prev_select_result_index = edit_window.show_word_seg_result_toplevel.index(edit_window.show_word_seg_result_toplevel.prev(select_result_iid[0])) # 获取前一个元素的索引
        edit_window.show_word_seg_result_toplevel.delete(select_result_iid[0])  # 删除原来元素
        new_select_result = edit_window.show_word_seg_result_toplevel.insert('', prev_select_result_index, values=select_result['values'], iid=select_result_iid[0]) # 在索引处添加想要移动的对象，并复制原来选项的iid
        edit_window.show_word_seg_result_toplevel.selection_set(new_select_result) # 象征性地选中移动项
        edit_window.show_word_seg_result_toplevel.see(new_select_result)  # 视图转到新项
        return True
    elif len(select_result_iid) > 1:
        messagebox.showerror("错误", "只可选中一个选项进行移动！")
        return False
    else:
        messagebox.showerror("错误", "没有可移动的选项！")
        return False

# 向后移动
def move_down(edit_window):
    global select_result_iid
    if edit_window.show_word_seg_result_toplevel.selection(): select_result_iid = edit_window.show_word_seg_result_toplevel.selection() # 获取当前选中iid
    if len(select_result_iid) == 1:
        select_result = edit_window.show_word_seg_result_toplevel.item(select_result_iid[0])  # 获取对应选项
        next_select_result_index = edit_window.show_word_seg_result_toplevel.index(
            edit_window.show_word_seg_result_toplevel.next(select_result_iid[0]))  # 获取后一个元素的索引
        edit_window.show_word_seg_result_toplevel.delete(select_result_iid[0])  # 删除原来元素
        new_select_result = edit_window.show_word_seg_result_toplevel.insert('', next_select_result_index, values=select_result['values'], iid=select_result_iid[0])  # 在索引处添加想要移动的对象，并复制原来选项的iid
        edit_window.show_word_seg_result_toplevel.selection_set(new_select_result)  # 象征性地选中移动项
        edit_window.show_word_seg_result_toplevel.see(new_select_result) # 视图转到新项
        return True
    elif len(select_result_iid) > 1:
        messagebox.showerror("错误", "只可选中一个选项进行移动！")
        return False
    else:
        messagebox.showerror("错误", "没有可移动的选项！")
        return False