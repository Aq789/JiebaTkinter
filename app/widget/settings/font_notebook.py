# 字体设置标签页
import tkinter as tk
from tkinter import ttk, TclError
from tkinter import font
from tkinter import colorchooser

import app.service.choose_font_shape as s_cfs

class FontNotebook:
    def __init__(self, notebook, window, toplevel):
        self.font_color = None
        self.toplevel = toplevel
        self.main_window = window
        self.saved = True

        # 读取数据
        self.font_data = window.font_settings_datas.get_font_data()
        self.shape_data = window.font_settings_datas.get_shape_data()
        self.size_data = window.font_settings_datas.get_size_data()
        self.under_line_data = window.font_settings_datas.get_under_line_data()
        self.delete_line_data = window.font_settings_datas.get_delete_line_data()
        self.color_data = window.font_settings_datas.get_color_data()

        self.font_frame = tk.Frame(notebook)
        self.font_frame.pack(fill="both", expand=True)
        self.font_frame.grid_columnconfigure(0, weight=1)
        self.font_color = self.color_data
        self.initial_color = self.color_data

        self.preview_font = font.Font(family=self.font_data,
                                      size=self.size_data,
                                      weight=s_cfs.choose_shape(self.shape_data)[0],
                                      slant=s_cfs.choose_shape(self.shape_data)[1],
                                      underline=self.under_line_data,
                                      overstrike=self.delete_line_data)

        self.families = sorted(font.families()) # 系统所有字体
        self.sizes = list(range(8, 73, 2)) + [80, 100] # 字号大小
        self.styles = ["常规", "粗体", "斜体", "粗斜体"] # 样式映射表

        """文本框标签栏"""
        self.font_label_frame = tk.LabelFrame(self.font_frame, text="编辑器选项", labelanchor="nw", relief="groove")
        self.font_label_frame.grid(row=0, column=0, sticky="new", padx=5, pady=5)
        self.font_label_frame.grid_rowconfigure(0, weight=1)
        self.font_label_frame.grid_columnconfigure(0, weight=1)

        self.frame1 = tk.Frame(self.font_label_frame)
        self.frame1.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.frame1.grid_columnconfigure(0, weight=1)
        self.label1 = tk.Label(self.frame1, text="字体")
        self.label1.grid(row=0, column=0, sticky="nw")
        self.font_entry = ttk.Entry(self.frame1)
        self.font_entry.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.font_entry.insert(0, self.font_data)
        self.font_entry.config(state="readonly")
        self.font_listbox = tk.Listbox(self.frame1, height=8)
        self.font_listbox.grid(row=2, column=0, pady=5, sticky="ew")
        self.scrollbar1 = tk.Scrollbar(self.frame1, orient="vertical", command=self.font_listbox.yview)
        self.scrollbar1.grid(row=2, column=1, sticky="nes")
        self.font_listbox.config(yscrollcommand=self.scrollbar1.set)
        # 填充数据
        for f in self.families:
            self.font_listbox.insert("end", f)

        self.frame2 = tk.Frame(self.font_label_frame)
        self.frame2.grid(row=0, column=1, padx=5, pady=5)
        self.label2 = tk.Label(self.frame2, text="字形")
        self.label2.grid(row=0, column=0, sticky="nw")
        self.shape_entry = ttk.Entry(self.frame2, width=12)
        self.shape_entry.grid(row=1, column=0)
        self.shape_entry.insert(0, self.shape_data)
        self.shape_entry.config(state="readonly")
        self.shape_listbox = tk.Listbox(self.frame2, width=12, height=8)
        self.shape_listbox.grid(row=2, column=0, pady=5)
        # 填充数据
        for s in self.styles:
            self.shape_listbox.insert("end", s)

        self.frame3 = tk.Frame(self.font_label_frame)
        self.frame3.grid(row=0, column=2, padx=5, pady=5)
        self.label3 = tk.Label(self.frame3, text="大小")
        self.label3.grid(row=0, column=0, sticky="nw")
        self.size_entry = ttk.Entry(self.frame3, width=10)
        self.size_entry.grid(row=1, column=0, columnspan=2)
        self.size_entry.insert(0, self.size_data)
        self.size_entry.config(state="readonly")
        self.size_listbox = tk.Listbox(self.frame3, width=8, height=8)
        self.size_listbox.grid(row=2, column=0, pady=5)
        self.scrollbar2 = tk.Scrollbar(self.frame3, orient="vertical", command=self.size_listbox.yview)
        self.scrollbar2.grid(row=2, column=1, sticky="nes")
        self.size_listbox.config(yscrollcommand=self.scrollbar2.set)
        # 填充数据
        for s in self.sizes:
            self.size_listbox.insert("end", str(s))

        self.frame4 = tk.Frame(self.font_label_frame)
        self.frame4.grid(row=1, column=1, columnspan=2, sticky="ew", pady=5, padx=5)
        self.label_frame1 = tk.LabelFrame(self.frame4, text="效果", labelanchor="nw", relief="groove")
        self.label_frame1.pack(fill="both", expand=True)
        self.delete_line_var = tk.BooleanVar(value=self.delete_line_data)
        self.delete_line = ttk.Checkbutton(self.label_frame1, text="删除线", variable=self.delete_line_var, command=self.update_preview)
        self.delete_line.grid(row=0, column=0)
        self.under_line_var = tk.BooleanVar(value=self.under_line_data)
        self.under_line = ttk.Checkbutton(self.label_frame1, text="下划线", variable=self.under_line_var, command=self.update_preview)
        self.under_line.grid(row=1, column=0)
        self.choose_color = ttk.Button(self.label_frame1, text="选择颜色", command=self.choose_color)
        self.choose_color.grid(row=2, column=0, padx=5, pady=5)

        self.frame5 = tk.Frame(self.font_label_frame)
        self.frame5.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.label_frame2 = tk.LabelFrame(self.frame5, text="示例", labelanchor="nw", relief="groove")
        self.label_frame2.pack(fill="both", expand=True)
        self.label4 = tk.Label(self.label_frame2, text="示例文本AaBb", font=self.preview_font, bg="white", fg=self.color_data)
        self.label4.pack(anchor="center", fill="both", expand=True)

        self.font_listbox.bind("<<ListboxSelect>>", self.update_preview)
        self.shape_listbox.bind("<<ListboxSelect>>", self.update_preview)
        self.size_listbox.bind("<<ListboxSelect>>", self.update_preview)

    def has_changed(self):
        if ([self.font_data, self.shape_data, self.size_data, self.under_line_data, self.delete_line_data,
             self.color_data] !=
                [self.font_entry.get(), self.shape_entry.get(), int(self.size_entry.get()), self.under_line_var.get(),
                 self.delete_line_var.get(), self.font_color]):
            self.saved = False
            self.toplevel.has_changed()
        else:
            self.saved = True
            self.toplevel.has_changed()

    def choose_color(self):
        try:
            color = colorchooser.askcolor(title="请选择字体颜色")
            if color:
                hex_color = color[1]
                self.font_color = hex_color
                self.label4.config(fg=str(hex_color))
        except TclError:
            return
        self.has_changed()

    def update_preview(self, event=None):
        # 获取字体名
        family_selection = self.font_listbox.curselection()
        if family_selection:
            family = self.font_listbox.get(family_selection[0])
        else:
            family = self.preview_font.cget("family")

        # 获取选中的字号
        size_selection = self.size_listbox.curselection()
        if size_selection:
            size = int(self.size_listbox.get(size_selection[0]))
        else:
            size = self.preview_font.cget("size")

        # 获取选中的样式
        style_selection = self.shape_listbox.curselection()
        if style_selection:
            style_text = self.shape_listbox.get(style_selection[0])
            # 映射逻辑
            if style_text == "粗体":
                self.shape_entry.config(state='normal')
                self.shape_entry.delete("0", "end")
                self.shape_entry.insert(0, style_text)
                self.shape_entry.config(state='readonly')
                weight, slant = "bold", "roman"
            elif style_text == "斜体":
                self.shape_entry.config(state='normal')
                self.shape_entry.delete("0", "end")
                self.shape_entry.insert(0, style_text)
                self.shape_entry.config(state='readonly')
                weight, slant = "normal", "italic"
            elif style_text == "粗斜体":
                self.shape_entry.config(state='normal')
                self.shape_entry.delete("0", "end")
                self.shape_entry.insert(0, style_text)
                self.shape_entry.config(state='readonly')
                weight, slant = "bold", "italic"
            else:  # 常规
                self.shape_entry.config(state='normal')
                self.shape_entry.delete("0", "end")
                self.shape_entry.insert(0, style_text)
                self.shape_entry.config(state='readonly')
                weight, slant = "normal", "roman"
        else:
            # 未选中则保持当前
            weight = self.preview_font.cget("weight")
            slant = self.preview_font.cget("slant")

        self.font_entry.config(state='normal')
        self.font_entry.delete("0", "end")
        self.font_entry.insert(0, family)
        self.font_entry.config(state='readonly')
        self.size_entry.config(state='normal')
        self.size_entry.delete("0", "end")
        self.size_entry.insert(0, str(size))
        self.size_entry.config(state='readonly')

        underline = self.under_line_var.get()
        overstrike = self.delete_line_var.get()

        self.has_changed()

        self.preview_font.config(family=family,
                                 size=size,
                                 weight=weight,
                                 slant=slant,
                                 underline=underline,
                                 overstrike=overstrike)
        self.toplevel.settings_window.geometry("")