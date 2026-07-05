# 右侧编辑文本模块
import tkinter as tk
from tkinter import font

import app.service.choose_font_shape as s_cfs

class RightFrame:
    def __init__(self, paned_window, window):
        self.main_window = window

        self.font_data = window.font_settings_datas.font_data
        self.shape_data = window.font_settings_datas.shape_data
        self.size_data = window.font_settings_datas.size_data
        self.under_line_data = window.font_settings_datas.under_line_data
        self.delete_line_data = window.font_settings_datas.delete_line_data
        self.color_data = window.font_settings_datas.color_data

        self.font = font.Font(family=self.font_data,
                              size=self.size_data,
                              weight=s_cfs.choose_shape(self.shape_data)[0],
                              slant=s_cfs.choose_shape(self.shape_data)[1],
                              underline=self.under_line_data,
                              overstrike=self.delete_line_data)

        self.right_frame = tk.Frame(paned_window) # 创建右侧模块
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        self.text = tk.Text(self.right_frame, wrap="none", undo=True) # 创建text文本编辑框
        self.text.grid(row=0, column=0, sticky="nsew") # 放置文本编辑框
        self.text.config(font=self.font)
        self.text.config(fg=self.color_data)

        # 创建纵向滚动条并与文本编辑框绑定
        height_scroll = tk.Scrollbar(self.right_frame, orient="vertical", command=self.text.yview)
        height_scroll.grid(row=0, column=1, sticky="ns")
        self.text.config(yscrollcommand=height_scroll.set)

        # 创建横向滚动条并与文本编辑框绑定
        width_scroll = tk.Scrollbar(self.right_frame, orient="horizontal", command=self.text.xview)
        width_scroll.grid(row=1, column=0, sticky="ew")
        self.text.config(xscrollcommand=width_scroll.set)

    def change_font(self, font_data, size_data, shape_data, under_line_data, delete_line_data, color_data):
        self.font = font.Font(family=font_data,
                              size=size_data,
                              weight=s_cfs.choose_shape(shape_data)[0],
                              slant=s_cfs.choose_shape(shape_data)[1],
                              underline=under_line_data,
                              overstrike=delete_line_data)
        self.text.config(font=self.font)
        self.text.config(fg=color_data)