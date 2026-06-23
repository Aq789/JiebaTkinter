# 设置总窗口
import tkinter as tk
from tkinter import ttk

import app.widget.settings.seg_notebook
import app.widget.settings.window_notebook
import app.controllers.settings.setting_toplevel as c_sst

class SettingsToplevel:
    def __init__(self, window):
        self.main_window = window

        self.settings_window = tk.Toplevel(window.main_window)
        self.settings_window.title("全局设置")
        self.settings_window.transient(window.main_window)  # 子窗口在父窗口之上
        self.settings_window.wm_attributes("-toolwindow", True)  # 只保留关闭按钮
        self.settings_window.geometry("370x450+500+200")  # 窗口大小和初始位置
        self.settings_window.wm_minsize(370, 450)  # 最小窗口大小

        self.settings_window.grid_rowconfigure(0, weight=1)
        self.settings_window.grid_columnconfigure(0, weight=1)

        """顶部内容"""
        self.top_frame = tk.Frame(self.settings_window)
        self.top_frame.grid(row=0, column=0, sticky="nsew")

        self.settings_notebook = ttk.Notebook(self.top_frame)
        self.settings_notebook.pack(fill="both", expand=True, padx=10) # 放置标签页

        self.seg_settings = ttk.Frame(self.settings_notebook) # 创建分词设置标签页
        self.window_settings = ttk.Frame(self.settings_notebook) # 创建窗口设置标签页

        self.seg_notebook = app.widget.settings.seg_notebook.SegNotebook(self.seg_settings, self.main_window, self)
        self.window_notebook = app.widget.settings.window_notebook.WindowNotebook(self.window_settings, self.main_window, self)

        # 加入notebook标签页中
        self.settings_notebook.add(self.seg_settings, text=" 分词选项 ")
        self.settings_notebook.add(self.window_settings, text=" 窗口选项 ")

        """底部内容"""
        self.bottom_frame = tk.Frame(self.settings_window)
        self.bottom_frame.grid(row=1, column=0, sticky="nsew")

        frame = tk.Frame(self.bottom_frame)
        frame.pack(side="right")

        self.ok_button = ttk.Button(frame, text="确定", command=lambda :c_sst.ok(self))
        self.ok_button.grid(row=0, column=0, pady=10, padx=5)

        self.cancel_button = ttk.Button(frame, text="取消", command=lambda :c_sst.cancel(self))
        self.cancel_button.grid(row=0, column=1, pady=10, padx=5)

        self.apply_button = ttk.Button(frame, text="应用", command=lambda :c_sst.apply(self))
        self.apply_button.grid(row=0, column=2, pady=10, padx=5)
        self.apply_button.state(['disabled'])   # 设置禁用状态

        self.settings_window.grab_set() # 阻止父窗口操作
        self.settings_window.focus_set() # 子窗口获得焦点

        self.settings_window.wait_window() # 等待此窗口关闭

    # 设置禁用方法
    def apply_button_disabled(self):
        self.apply_button.state(['disabled'])

    def apply_button_enabled(self):
        self.apply_button.state(['!disabled'])

    # 检测所有标签页的状态
    def has_changed(self):
        if self.seg_notebook.saved and self.window_notebook.saved:
            self.apply_button_disabled()
            self.seg_notebook.saved = True
            self.window_notebook.saved = True
        else:
            self.apply_button_enabled()