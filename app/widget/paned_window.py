# 分隔条创建方法
import tkinter as tk
import app.view
import app.widget.left_frame
import app.widget.right_frame

class PanedWindow:
    def __init__(self, window):
        self.main_window = window

        self.paned_window = tk.PanedWindow(window.main_window, orient="horizontal", showhandle=True) # 创建可调节窗格实例
        self.paned_window.grid(row=0, column=0, sticky="nsew") # 放置可调节窗格

        self.left_frame = app.widget.left_frame.LeftFrame(self.paned_window, self.main_window) # 加载左侧模块
        self.right_frame = app.widget.right_frame.RightFrame(self.paned_window, self.main_window) # 加载右侧模块

        self.paned_window.add(self.left_frame.left_frame, minsize=20, width=240) # 放置左侧内容
        self.paned_window.add(self.right_frame.right_frame, minsize=50) # 放置右侧内容