# 左侧窗口模块
import tkinter as tk
from tkinter import ttk

class LeftFrame:
    def __init__(self, paned_window):
        self.left_frame = tk.Frame(paned_window) # 创建左侧模块实例

        notebook = ttk.Notebook(self.left_frame) # 创建notebook标签页
        notebook.pack(fill="both", expand=True) # 放置标签页

        tab_word_seg_result = ttk.Frame(notebook) # 创建分词结果标签页
        tab_word_dic = ttk.Frame(notebook) # 创建字典标签页

        tab_word_seg_result.grid_rowconfigure(0, weight=1)
        tab_word_seg_result.grid_columnconfigure(0, weight=1)
        tab_word_dic.grid_rowconfigure(0, weight=1)
        tab_word_dic.grid_columnconfigure(0, weight=1)

        # 加入notebook标签页中
        notebook.add(tab_word_seg_result, text="分词结果")
        notebook.add(tab_word_dic, text="字典")

        """分词结果"""
        # 开始创建新表格
        show_word_seg_result = ttk.Treeview(tab_word_seg_result, columns=("id", "word_name", "word_frequency", "word_class"), show="headings")

        # 定义每一列的标题
        show_word_seg_result.heading("id", text="序号")
        show_word_seg_result.heading("word_name", text="词名")
        show_word_seg_result.heading("word_frequency", text="词频")
        show_word_seg_result.heading("word_class", text="词性")

        # 定义每一列的宽度
        show_word_seg_result.column("id", width=20)
        show_word_seg_result.column("word_name", width=60)
        show_word_seg_result.column("word_frequency", width=30)
        show_word_seg_result.column("word_class", width=30)

        show_word_seg_result.grid(row=0, column=0, sticky="nsew", pady=10, padx=10) # 放置表格

        height_scroll_seg_result = tk.Scrollbar(tab_word_seg_result, orient="vertical", command=show_word_seg_result.yview) # 创建纵向滚动条
        height_scroll_seg_result.grid(row=0, column=1, sticky="ns")
        show_word_seg_result.config(yscrollcommand=height_scroll_seg_result.set)

        edit_word_seg_result = ttk.Button(tab_word_seg_result, text="编辑分词结果")
        edit_word_seg_result.grid(row=1, column=0, sticky="e", pady=5, padx=10)

        start_word_seg_result = ttk.Button(tab_word_seg_result, text="开始分词")
        start_word_seg_result.grid(row=1, column=0, sticky="w", pady=5, padx=10)

        """词典"""
        show_word_dic = ttk.Treeview(tab_word_dic, columns=("id", "word_name", "word_frequency", "word_class"), show="headings")

        # 定义每一列的标题
        show_word_dic.heading("id", text="序号")
        show_word_dic.heading("word_name", text="词名")
        show_word_dic.heading("word_frequency", text="词频")
        show_word_dic.heading("word_class", text="词性")

        # 定义每一列的宽度
        show_word_dic.column("id", width=20)
        show_word_dic.column("word_name", width=60)
        show_word_dic.column("word_frequency", width=30)
        show_word_dic.column("word_class", width=30)

        show_word_dic.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)  # 放置表格

        height_scroll_word_dic = tk.Scrollbar(tab_word_dic, orient="vertical",
                                                command=show_word_dic.yview)  # 创建纵向滚动条
        height_scroll_word_dic.grid(row=0, column=1, sticky="ns")
        show_word_dic.config(yscrollcommand=height_scroll_word_dic.set)

        edit_word_dic = ttk.Button(tab_word_dic, text="编辑词典")
        edit_word_dic.grid(row=1, column=0, sticky="e", pady=5, padx=10)