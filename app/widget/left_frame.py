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

        # 加入notebook标签页中
        notebook.add(tab_word_seg_result, text="分词结果")
        notebook.add(tab_word_dic, text="字典")