# 窗口设置标签页
import tkinter as tk
from tkinter import ttk

class WindowNotebook:
    def __init__(self, notebook, window, toplevel):
        self.toplevel = toplevel
        self.main_window = window
        self.saved = True

        # 从数据集中加载数据
        self.window_weight_data = window.window_settings_datas.get_window_weight_data()
        self.window_height_data = window.window_settings_datas.get_window_height_data()

        self.window_frame = tk.Frame(notebook)
        self.window_frame.pack(fill="both", expand=True)
        self.window_frame.grid_columnconfigure(0, weight=1)

        """窗口选项标签栏"""
        self.window_label_frame = tk.LabelFrame(self.window_frame, text="主窗口选项", labelanchor="nw", relief="groove")
        self.window_label_frame.grid(row=0, column=0, sticky="new", padx=5, pady=5)
        self.window_label_frame.grid_columnconfigure(0, weight=1)

        self.frame1 = tk.Frame(self.window_label_frame)
        self.frame1.grid(row=0, column=0, sticky="nw", padx=10, pady=3)
        self.label1 = tk.Label(self.frame1, text="窗口大小：")
        self.label1.grid(row=0, column=0)
        self.label2 = tk.Label(self.frame1, text="宽度")
        self.label2.grid(row=0, column=1, padx=3)
        self.window_weight = ttk.Entry(self.frame1, width=10)
        self.window_weight.grid(row=0, column=2, padx=3)
        self.window_weight.insert("end", self.window_weight_data)
        self.label3 = tk.Label(self.frame1, text="高度")
        self.label3.grid(row=0, column=3, padx=3)
        self.window_height = ttk.Entry(self.frame1, width=10)
        self.window_height.grid(row=0, column=4, padx=3)
        self.window_height.insert("end", self.window_height_data)

        self.frame2 = tk.Frame(self.window_label_frame)
        self.frame2.grid(row=1, column=0, sticky="ne", padx=10, pady=3)
        self.read_window_size = ttk.Button(self.frame2, text="读取当前窗口", command=self.get_window_size)
        self.read_window_size.grid(row=0, column=0, padx=3)

        self.window_height.bind('<Key>', self.on_refresh_entry)
        self.window_weight.bind('<Key>', self.on_refresh_entry)

    def on_refresh_entry(self, event):
        self.saved = False
        self.toplevel.has_changed()

    def get_window_size(self):
        window_weight, window_height = self.main_window.get_window_size()
        self.window_weight.delete(first=0, last="end")
        self.window_height.delete(first=0, last="end")
        self.window_weight.insert("0", window_weight)
        self.window_height.insert("0", window_height)
        self.toplevel.apply_button_enabled()
