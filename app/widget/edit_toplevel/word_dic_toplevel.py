# 编辑词典窗口
import tkinter as tk
from tkinter import ttk
main_window = None

class WordDicToplevel:
    def __init__(self, window, callback):
        global main_window
        self.main_window = main_window

        self.edit_word_dic_window = tk.Toplevel(window)
        self.edit_word_dic_window.title("编辑词典")
        self.edit_word_dic_window.transient(window) # 子窗口在父窗口之上
        self.edit_word_dic_window.wm_attributes("-toolwindow", True) # 只保留关闭按钮
        self.edit_word_dic_window.geometry("400x300+480+180") # 窗口大小和初始位置
        self.edit_word_dic_window.wm_minsize(480, 410) # 最小窗口大小

        self.edit_word_dic_window.grid_columnconfigure(0, weight=1)
        self.edit_word_dic_window.grid_rowconfigure(1, weight=1)

        """左侧内容"""
        # 展示文字
        label_1 = tk.Label(self.edit_word_dic_window, text="当前词典如下：")
        label_1.grid(row=0, column=0, sticky="w", padx=10)

        # 开始创建新模块
        self.left_frame_toplevel = tk.Frame(self.edit_word_dic_window)
        self.left_frame_toplevel.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        self.left_frame_toplevel.grid_columnconfigure(0, weight=1)
        self.left_frame_toplevel.grid_rowconfigure(0, weight=1)

        # 开始创建新表格
        self.show_word_dic_toplevel = ttk.Treeview(self.left_frame_toplevel,
                                                   columns=("id", "word_name", "word_frequency", "word_class"),
                                                   show="headings")

        # 定义每一列的标题
        self.show_word_dic_toplevel.heading("id", text="序号")
        self.show_word_dic_toplevel.heading("word_name", text="词名")
        self.show_word_dic_toplevel.heading("word_frequency", text="词频")
        self.show_word_dic_toplevel.heading("word_class", text="词性")

        # 定义每一列的宽度
        self.show_word_dic_toplevel.column("id", width=20)
        self.show_word_dic_toplevel.column("word_name", width=60)
        self.show_word_dic_toplevel.column("word_frequency", width=30)
        self.show_word_dic_toplevel.column("word_class", width=30)

        self.show_word_dic_toplevel.grid(row=0, column=0, sticky="nsew")  # 放置表格

        # 放置纵向滚动条
        h_show_word_dic_scroll = tk.Scrollbar(self.left_frame_toplevel, orient="vertical", command=self.show_word_dic_toplevel.yview)
        h_show_word_dic_scroll.grid(row=0, column=1, sticky="ns")
        self.show_word_dic_toplevel.config(yscrollcommand=h_show_word_dic_scroll.set)

        """右侧内容"""
        # 右侧添加新模块
        self.right_frame_toplevel = tk.Frame(self.edit_word_dic_window)
        self.right_frame_toplevel.grid(row=1, column=1, sticky="nes", padx=10, pady=5)

        move_pgup = ttk.Button(self.right_frame_toplevel, text="移至最前")
        move_pgup.grid(row=0, column=0, pady=5)

        move_up = ttk.Button(self.right_frame_toplevel, text="向前移动")
        move_up.grid(row=1, column=0, pady=5)

        move_down = ttk.Button(self.right_frame_toplevel, text="向后移动")
        move_down.grid(row=2, column=0, pady=5)

        move_pgdn = ttk.Button(self.right_frame_toplevel, text="移至最后")
        move_pgdn.grid(row=3, column=0, pady=5)

        create_word_dic = ttk.Button(self.right_frame_toplevel, text="创建词典条目")
        create_word_dic.grid(row=4, column=0, pady=5)

        delete_select = ttk.Button(self.right_frame_toplevel, text="删除选中词典")
        delete_select.grid(row=5, column=0, pady=5)

        save_change = ttk.Button(self.right_frame_toplevel, text="保存更改")
        save_change.grid(row=6, column=0, pady=5)

        """底部内容"""
        # 展示文字
        self.bottom_frame_toplevel = tk.LabelFrame(self.edit_word_dic_window, text="当前词条", labelanchor="nw", relief="groove")
        self.bottom_frame_toplevel.grid(row=2, column=0, pady=10, padx=10, columnspan=2, sticky="ew")
        self.bottom_frame_toplevel.grid_columnconfigure(0, weight=1)
        self.bottom_frame_toplevel.grid_columnconfigure(1, weight=1)
        self.bottom_frame_toplevel.grid_columnconfigure(2, weight=1)

        bottom_frame_1 = tk.Frame(self.bottom_frame_toplevel)
        bottom_frame_1.grid(row=0, column=0, padx=5, pady=5)
        bottom_frame_1.grid_columnconfigure(1, weight=1)
        bottom_label_1 = tk.Label(bottom_frame_1, text="词名：")
        bottom_label_1.grid(row=0, column=0)
        self.word_name_entry = ttk.Entry(bottom_frame_1)
        self.word_name_entry.grid(row=0, column=1, sticky="ew")

        bottom_frame_2 = tk.Frame(self.bottom_frame_toplevel)
        bottom_frame_2.grid(row=0, column=1, padx=5, pady=5)
        bottom_frame_2.grid_columnconfigure(1, weight=1)
        bottom_label_2 = tk.Label(bottom_frame_2, text="词频：")
        bottom_label_2.grid(row=0, column=0)
        self.word_frequency_entry = ttk.Entry(bottom_frame_2)
        self.word_frequency_entry.grid(row=0, column=1, sticky="ew")

        bottom_frame_3 = tk.Frame(self.bottom_frame_toplevel)
        bottom_frame_3.grid(row=0, column=2, padx=5, pady=5)
        bottom_frame_3.grid_columnconfigure(1, weight=1)
        bottom_label_3 = tk.Label(bottom_frame_3, text="词性：")
        bottom_label_3.grid(row=0, column=0)
        self.word_class_entry = ttk.Entry(bottom_frame_3)
        self.word_class_entry.grid(row=0, column=1, sticky="ew")

        # 底部查询
        self.bottom_search_toplevel = tk.Frame(self.edit_word_dic_window)
        self.bottom_search_toplevel.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10)
        self.bottom_search_toplevel.grid_columnconfigure(1, weight=1)

        # 展示文字
        label_2 = tk.Label(self.bottom_search_toplevel, text="查询词典")
        label_2.grid(row=0, column=0, sticky="w")

        # 底部添加新模块
        self.search_entry = ttk.Entry(self.bottom_search_toplevel)
        self.search_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        search_result = ttk.Button(self.bottom_search_toplevel, text="查找结果")
        search_result.grid(row=0, column=2)

        self.callback = callback # 保存回调函数
        self.edit_word_dic_window.protocol("WM_DELETE_WINDOW", self.on_close)

        tk.Frame(self.edit_word_dic_window).grid(row=5, column=0, pady=5)

    def on_close(self): # 关闭执行的方法
        if self.callback: self.callback() # 先调用回调（恢复按钮）
        self.edit_word_dic_window.destroy()