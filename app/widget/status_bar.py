# 底部状态栏
import tkinter as tk
import _tkinter

import app.service.statistic as s_s


class StatusBar:
    def __init__(self, window):
        self.main_window = window

        # 初始数据加载
        self.len_word_dic_list_data = window.word_dic_datas.return_len_word_dic_list()

        self.bottom_status_bar = tk.Frame(window.main_window)
        self.bottom_status_bar.grid(row=1, column=0, sticky="ews", padx=5, pady=3)
        self.bottom_status_bar.grid_columnconfigure(2, weight=1)

        self.point = tk.Label(self.bottom_status_bar, text="当前位置：行0, 列0")
        self.point.grid(row=0, column=0)

        self.chinese_char_count = tk.Label(self.bottom_status_bar, text="总字数：0")
        self.chinese_char_count.grid(row=0, column=1, padx=8)

        self.custom_dict_count = tk.Label(self.bottom_status_bar, text=f"自定义词典数：{self.len_word_dic_list_data}")
        self.custom_dict_count.grid(row=0, column=2, sticky="w", padx=8)

        self.frame1 = tk.Frame(self.bottom_status_bar)
        self.frame1.grid(row=0, column=3, padx=8)

        self.status = tk.Label(self.frame1, text="就绪")
        self.status.grid(row=0, column=0, padx=8, sticky="e")

        self.main_window.paned_window.right_frame.text.bind("<KeyRelease>", self.get_point)
        self.main_window.paned_window.right_frame.text.bind("<ButtonRelease-1>", self.get_point)
        self.main_window.paned_window.right_frame.text.bind("<<Selection>>", self.get_selection)
        self.main_window.paned_window.right_frame.text.bind("<<Modified>>", self.modified)

    # 获取光标位置
    def get_point(self, event):
        text = self.main_window.paned_window.right_frame.text
        pos = text.index("insert").split(".")
        self.point.config(text=f"当前位置：行{pos[0]}, 列{pos[1]}")

    # 重新统计字数，当文本框选中文本时
    def get_selection(self, event):
        text = self.main_window.paned_window.right_frame.text
        try:
            self.chinese_char_count.config(text=f"总字数：{s_s.first_statistic(text.get(tk.SEL_FIRST, tk.SEL_LAST))[0]}/{s_s.first_statistic(text.get("1.0", "end"))[0]}")
            text.edit_modified(False)
        except _tkinter.TclError:
            self.chinese_char_count.config(text=f"总字数：{s_s.first_statistic(text.get("1.0", "end"))[0]}")
            text.edit_modified(False)

    # 文本框改变
    def modified(self, event):
        text = self.main_window.paned_window.right_frame.text
        self.chinese_char_count.config(text=f"总字数：{s_s.first_statistic(text.get("1.0", "end"))[0]}")
        text.edit_modified(False)

    # 就绪状态设置
    def set_ready_status(self, message):
        self.status.config(text=message)