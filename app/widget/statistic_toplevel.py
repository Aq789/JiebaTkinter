# 统计窗口
import tkinter as tk
from tkinter import ttk

import app.controllers.statistic_toplevel as c_st
# 添加信息：中文字数，字符数（不计空格），字符数（计空格），中文词数，
# 分词结果总数，自定义词典总数，英文单词数，行数

class StatisticToplevel:
    def __init__(self, window):
        self.main_window = window

        self.statistic_window = tk.Toplevel(window.main_window)
        self.statistic_window.title("统计")
        self.statistic_window.transient(window.main_window)
        self.statistic_window.wm_attributes("-toolwindow", True)
        self.statistic_window.geometry("240x300+630+200")
        self.statistic_window.resizable(False, False)
        self.statistic_window.grab_set()

        self.statistic_window.grid_columnconfigure(0, weight=1)

        """内容"""
        self.statistic_label_frame = tk.LabelFrame(self.statistic_window, text="统计信息", labelanchor="nw", relief="groove")
        self.statistic_label_frame.grid(row=0, column=0, sticky="new", padx=5, pady=5)
        self.statistic_label_frame.grid_columnconfigure(0, weight=1)

        self.chinese_char_count_frame = tk.Frame(self.statistic_label_frame)
        self.chinese_char_count_frame.grid(row=0, column=0, sticky="new", padx=5)
        self.chinese_char_count_frame.grid_columnconfigure(0, weight=1)
        self.chinese_char_count_label = tk.Label(self.chinese_char_count_frame, text="中文字数")
        self.chinese_char_count_label.grid(row=0, column=0, sticky="w", padx=5)
        self.chinese_char_count = tk.Label(self.chinese_char_count_frame, text="-")
        self.chinese_char_count.grid(row=0, column=1, sticky="e", padx=5)

        self.char_count_no_space_frame = tk.Frame(self.statistic_label_frame)
        self.char_count_no_space_frame.grid(row=1, column=0, sticky="new", padx=5)
        self.char_count_no_space_frame.grid_columnconfigure(0, weight=1)
        self.char_count_no_space_label = tk.Label(self.char_count_no_space_frame, text="字符数（不计空格）")
        self.char_count_no_space_label.grid(row=0, column=0, sticky="w", padx=5)
        self.char_count_no_space = tk.Label(self.char_count_no_space_frame, text="-")
        self.char_count_no_space.grid(row=0, column=1, sticky="e", padx=5)

        self.char_count_with_space_frame = tk.Frame(self.statistic_label_frame)
        self.char_count_with_space_frame.grid(row=2, column=0, sticky="new", padx=5)
        self.char_count_with_space_frame.grid_columnconfigure(0, weight=1)
        self.char_count_with_space_label = tk.Label(self.char_count_with_space_frame, text="字符数（计空格）")
        self.char_count_with_space_label.grid(row=0, column=0, sticky="w", padx=5)
        self.char_count_with_space = tk.Label(self.char_count_with_space_frame, text="-")
        self.char_count_with_space.grid(row=0, column=1, sticky="e", padx=5)

        self.chinese_word_count_frame = tk.Frame(self.statistic_label_frame)
        self.chinese_word_count_frame.grid(row=3, column=0, sticky="new", padx=5)
        self.chinese_word_count_frame.grid_columnconfigure(0, weight=1)
        self.chinese_word_count_label = tk.Label(self.chinese_word_count_frame, text="中文词数")
        self.chinese_word_count_label.grid(row=0, column=0, sticky="w", padx=5)
        self.chinese_word_count = tk.Label(self.chinese_word_count_frame, text="-")
        self.chinese_word_count.grid(row=0, column=1, sticky="e", padx=5)

        self.seg_result_count_only_chinese_frame = tk.Frame(self.statistic_label_frame)
        self.seg_result_count_only_chinese_frame.grid(row=4, column=0, sticky="new", padx=5)
        self.seg_result_count_only_chinese_frame.grid_columnconfigure(0, weight=1)
        self.seg_result_count_only_chinese_label = tk.Label(self.seg_result_count_only_chinese_frame, text="分词结果总数（仅中文）")
        self.seg_result_count_only_chinese_label.grid(row=0, column=0, sticky="w", padx=5)
        self.seg_result_count_only_chinese = tk.Label(self.seg_result_count_only_chinese_frame, text="-")
        self.seg_result_count_only_chinese.grid(row=0, column=1, sticky="e", padx=5)

        self.seg_result_count_all_frame = tk.Frame(self.statistic_label_frame)
        self.seg_result_count_all_frame.grid(row=5, column=0, sticky="new", padx=5)
        self.seg_result_count_all_frame.grid_columnconfigure(0, weight=1)
        self.seg_result_count_all_label = tk.Label(self.seg_result_count_all_frame, text="分词结果总数（所有）")
        self.seg_result_count_all_label.grid(row=0, column=0, sticky="w", padx=5)
        self.seg_result_count_all = tk.Label(self.seg_result_count_all_frame, text="-")
        self.seg_result_count_all.grid(row=0, column=1, sticky="e", padx=5)

        self.custom_dict_size_frame = tk.Frame(self.statistic_label_frame)
        self.custom_dict_size_frame.grid(row=6, column=0, sticky="new", padx=5)
        self.custom_dict_size_frame.grid_columnconfigure(0, weight=1)
        self.custom_dict_size_label = tk.Label(self.custom_dict_size_frame, text="自定义词典总数")
        self.custom_dict_size_label.grid(row=0, column=0, sticky="w", padx=5)
        self.custom_dict_size = tk.Label(self.custom_dict_size_frame, text="-")
        self.custom_dict_size.grid(row=0, column=1, sticky="e", padx=5)

        self.english_word_count_frame = tk.Frame(self.statistic_label_frame)
        self.english_word_count_frame.grid(row=7, column=0, sticky="new", padx=5)
        self.english_word_count_frame.grid_columnconfigure(0, weight=1)
        self.english_word_count_label = tk.Label(self.english_word_count_frame, text="英文单词数")
        self.english_word_count_label.grid(row=0, column=0, sticky="w", padx=5)
        self.english_word_count = tk.Label(self.english_word_count_frame, text="-")
        self.english_word_count.grid(row=0, column=1, sticky="e", padx=5)

        self.line_count_frame = tk.Frame(self.statistic_label_frame)
        self.line_count_frame.grid(row=8, column=0, sticky="new", padx=5)
        self.line_count_frame.grid_columnconfigure(0, weight=1)
        self.line_count_label = tk.Label(self.line_count_frame, text="行数")
        self.line_count_label.grid(row=0, column=0, sticky="w", padx=5)
        self.line_count = tk.Label(self.line_count_frame, text="-")
        self.line_count.grid(row=0, column=1, sticky="e", padx=5)

        self.label = tk.Label(self.statistic_window, text="* 部分数据需分词后可见")
        self.label.grid(row=1, column=0, sticky="nw", padx=5)

        self.close_window = ttk.Button(self.statistic_window, text="关闭", command=self.on_close)
        self.close_window.grid(row=2, column=0, sticky="ne", padx=5, pady=5)

        c_st.statistic_start(self)

    # 关闭方法
    def on_close(self):
        self.statistic_window.destroy()