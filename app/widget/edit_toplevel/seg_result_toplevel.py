# 编辑分词结果窗口
import tkinter as tk
import app.controllers.edit_toplevel.seg_result_toplevel as c_srt
from tkinter import ttk

class SegResultToplevel:
    def __init__(self, window, callback):
        self.edit_seg_result_window = tk.Toplevel(window)
        self.edit_seg_result_window.title("编辑分词结果")
        self.edit_seg_result_window.transient(window) # 子窗口在父窗口之上
        self.edit_seg_result_window.wm_attributes("-toolwindow", True) # 只保留关闭按钮
        self.edit_seg_result_window.geometry("450x350+500+200") # 窗口大小和初始位置
        self.edit_seg_result_window.wm_minsize(450, 370) # 最小窗口大小

        self.edit_seg_result_window.grid_columnconfigure(0, weight=1)
        self.edit_seg_result_window.grid_rowconfigure(1, weight=1)

        """左侧内容"""
        # 展示文字
        label_1 = tk.Label(self.edit_seg_result_window, text="当前分词结果如下：")
        label_1.grid(row=0, column=0, sticky="w", padx=10)

        # 开始创建新模块
        self.left_frame_toplevel = tk.Frame(self.edit_seg_result_window)
        self.left_frame_toplevel.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        self.left_frame_toplevel.grid_columnconfigure(0, weight=1)
        self.left_frame_toplevel.grid_rowconfigure(0, weight=1)

        # 开始创建新表格
        self.show_word_seg_result_toplevel = ttk.Treeview(self.left_frame_toplevel,
                                            columns=("id", "word_name", "word_frequency", "word_class"),
                                            show="headings")

        # 定义每一列的标题
        self.show_word_seg_result_toplevel.heading("id", text="序号")
        self.show_word_seg_result_toplevel.heading("word_name", text="词名")
        self.show_word_seg_result_toplevel.heading("word_frequency", text="词频")
        self.show_word_seg_result_toplevel.heading("word_class", text="词性")

        # 定义每一列的宽度
        self.show_word_seg_result_toplevel.column("id", width=20)
        self.show_word_seg_result_toplevel.column("word_name", width=60)
        self.show_word_seg_result_toplevel.column("word_frequency", width=30)
        self.show_word_seg_result_toplevel.column("word_class", width=30)

        self.show_word_seg_result_toplevel.grid(row=0, column=0, sticky="nsew")  # 放置表格

        # 放置纵向滚动条
        h_show_word_seg_result_scroll = tk.Scrollbar(self.left_frame_toplevel, orient="vertical", command=self.show_word_seg_result_toplevel.yview)
        h_show_word_seg_result_scroll.grid(row=0, column=1, sticky="ns")
        self.show_word_seg_result_toplevel.config(yscrollcommand=h_show_word_seg_result_scroll.set)

        """右侧内容"""
        # 右侧添加新模块
        self.right_frame_toplevel = tk.Frame(self.edit_seg_result_window)
        self.right_frame_toplevel.grid(row=1, column=1, sticky="nes", padx=10, pady=5)

        move_pgup = ttk.Button(self.right_frame_toplevel, text="移至最前")
        move_pgup.grid(row=0, column=0, pady=5)

        move_up = ttk.Button(self.right_frame_toplevel, text="向前移动")
        move_up.grid(row=1, column=0, pady=5)

        move_down = ttk.Button(self.right_frame_toplevel, text="向后移动")
        move_down.grid(row=2, column=0, pady=5)

        move_pgdn = ttk.Button(self.right_frame_toplevel, text="移至最后")
        move_pgdn.grid(row=3, column=0, pady=5)

        delete_select = ttk.Button(self.right_frame_toplevel, text="删除选中结果")
        delete_select.grid(row=4, column=0, pady=5)

        save_change = ttk.Button(self.right_frame_toplevel, text="保存更改")
        save_change.grid(row=5, column=0, pady=5)

        """底部内容"""
        # 展示文字
        label_2 = tk.Label(self.edit_seg_result_window, text="请输入要查找的词名：")
        label_2.grid(row=2, column=0, sticky="w", padx=10)

        # 底部添加新模块
        self.search_entry = ttk.Entry(self.edit_seg_result_window)
        self.search_entry.grid(row=3, column=0, sticky="ew", padx=10, pady=5)

        search_result = ttk.Button(self.edit_seg_result_window, text="查找结果")
        search_result.grid(row=3, column=1)

        tk.Frame(self.edit_seg_result_window).grid(row=5, column=0, pady=5)

        """关闭窗口事件"""
        self.callback = callback # 保存回调函数
        self.edit_seg_result_window.protocol("WM_DELETE_WINDOW", self.on_close)

        c_srt.input_data(self)

    def on_close(self): # 关闭执行的方法
        if self.callback: self.callback() # 先调用回调（恢复按钮）
        self.edit_seg_result_window.destroy()