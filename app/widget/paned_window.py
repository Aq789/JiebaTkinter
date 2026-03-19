# 分隔条创建方法
import tkinter as tk
import app.view
import app.widget.left_frame
import app.widget.right_frame

class PanedWindow:
    def __init__(self, window):
        self.new_paned_window = tk.PanedWindow(window, orient="horizontal", showhandle=True) # 创建可调节窗格实例
        self.new_paned_window.pack(fill="both", expand=True) # 放置可调节窗格

        self.new_left_frame = app.widget.left_frame.LeftFrame(self.new_paned_window) # 加载左侧模块
        self.new_right_frame = app.widget.right_frame.RightFrame(self.new_paned_window) # 加载右侧模块

        self.new_paned_window.add(self.new_left_frame.left_frame, minsize=20, width=200) # 放置左侧内容
        self.new_paned_window.add(self.new_right_frame.right_frame, minsize=50) # 放置右侧内容