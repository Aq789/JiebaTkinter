# 底部状态栏
import tkinter as tk
main_window = None

class StatusBar:
    def __init__(self, window):
        global main_window
        self.main_window = main_window

        self.bottom_status_bar = tk.Frame(window)
        self.bottom_status_bar.pack(fill="x")

        """此后将会添加总字数，当前字体，自动换行，保存状态等状态信息"""
        point = tk.Label(self.bottom_status_bar, text="当前位置：")
        point.grid(row=0, column=0)