# 底部状态栏
import tkinter as tk

class StatusBar:
    def __init__(self, window):
        self.main_window = window

        self.bottom_status_bar = tk.Frame(window.main_window)
        self.bottom_status_bar.grid(row=1, column=0, sticky="ews")

        """此后将会添加总字数，当前字体，自动换行，保存状态等状态信息"""
        point = tk.Label(self.bottom_status_bar, text="当前位置：")
        point.grid(row=0, column=0)