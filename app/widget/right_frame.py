# 右侧编辑文本模块
import tkinter as tk

class RightFrame:
    def __init__(self, paned_window):
        self.right_frame = tk.Frame(paned_window) # 创建右侧模块
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        text = tk.Text(self.right_frame, wrap="none", undo=True) # 创建text文本编辑框
        text.grid(row=0, column=0, sticky="nsew") # 放置文本编辑框

        # 创建纵向滚动条并与文本编辑框绑定
        height_scroll = tk.Scrollbar(self.right_frame, orient="vertical", command=text.yview)
        height_scroll.grid(row=0, column=1, sticky="ns")
        text.config(yscrollcommand=height_scroll.set)

        # 创建横向滚动条并与文本编辑框绑定
        width_scroll = tk.Scrollbar(self.right_frame, orient="horizontal", command=text.xview)
        width_scroll.grid(row=1, column=0, sticky="ew")
        text.config(xscrollcommand=width_scroll.set)