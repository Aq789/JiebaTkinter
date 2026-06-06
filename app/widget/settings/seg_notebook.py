# 分词设置标签页
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class SegNotebook:
    def __init__(self, notebook, window, toplevel):
        self.toplevel = toplevel
        self.main_window = window
        self.saved = True

        # 读取分词设置数据集中的数据
        self.seg_mode_data = window.seg_settings_datas.get_seg_mode_data()
        self.auto_seg_result_frequency_data = window.seg_settings_datas.get_auto_seg_result_frequency_data()
        self.auto_seg_result_class_data = window.seg_settings_datas.get_auto_seg_result_class_data()
        self.hmm_data = window.seg_settings_datas.get_hmm_data()
        self.ignore_sign_data = window.seg_settings_datas.get_ignore_sign_data()
        self.ignore_english_data = window.seg_settings_datas.get_ignore_english_data()
        self.dic_var_data = window.seg_settings_datas.get_dic_var_data()
        self.custom_path_data = window.seg_settings_datas.get_custom_path()

        self.seg_frame = tk.Frame(notebook)
        self.seg_frame.pack(fill="both", expand=True)
        self.seg_frame.grid_columnconfigure(0, weight=1)

        def dic_path_radiobutton():
            dic_var_changed()
            if self.dic_var.get() == 0:
                self.custom_path_entry.state(['disabled'])
                self.custom_path_button.state(['disabled'])
            else:
                self.custom_path_entry.state(['!disabled'])
                self.custom_path_button.state(['!disabled'])

        def custom_path_dialog():
            custom_file_path = filedialog.askopenfilename(title="打开自定义词典", filetypes=[("文本文件", "*.txt")])
            if custom_file_path:
                self.custom_path_entry.delete('0', 'end')
                self.custom_path_entry.insert('0', custom_file_path)
                self.toplevel.apply_button.state(['!disabled'])

        def has_changed():
            if [self.seg_mode_data, self.auto_seg_result_frequency_data, self.auto_seg_result_class_data, self.hmm_data,
                 self.ignore_sign_data, self.ignore_english_data, self.dic_var_data] != [self.seg_var.get(), self.auto_seg_result_frequency_var.get(), self.auto_seg_result_class_var.get(),
                 self.hmm_var.get(), self.ignore_sign_var.get(), self.ignore_english_var.get(), self.dic_var.get()]:
                self.toplevel.apply_button.state(['!disabled'])
            else:
                self.toplevel.apply_button.state(['disabled'])

        def dic_var_changed():
            self.toplevel.apply_button.state(['!disabled'])

        """分词选项标签栏"""
        self.seg_label_frame = tk.LabelFrame(self.seg_frame, text="分词选项", labelanchor="nw", relief="groove")
        self.seg_label_frame.grid(row=0, column=0, sticky="new", padx=5, pady=5)

        self.frame1 = tk.Frame(self.seg_label_frame)
        self.frame1.grid(row=0, column=0, sticky="nw", padx=10, pady=3)
        self.label = tk.Label(self.frame1, text="切分模式：")
        self.label.grid(row=0, column=0)
        self.seg_var = tk.IntVar()
        self.seg_var.set(self.seg_mode_data) # 应用设置
        self.full_mode = tk.Radiobutton(self.frame1, text="全模式", variable=self.seg_var, value=0, command=has_changed) # 全模式单选框
        self.exact_mode = tk.Radiobutton(self.frame1, text="精确模式", variable=self.seg_var, value=1, command=has_changed) # 精确模式单选框
        self.search_mode = tk.Radiobutton(self.frame1, text="搜索引擎模式", variable=self.seg_var, value=2, command=has_changed) # 搜索引擎模式单选框
        self.full_mode.grid(row=0, column=1)
        self.exact_mode.grid(row=0, column=2)
        self.search_mode.grid(row=0, column=3)

        self.auto_seg_result_frequency_var = tk.BooleanVar()
        self.auto_seg_result_frequency = tk.Checkbutton(self.seg_label_frame, text="是否统计词频", variable=self.auto_seg_result_frequency_var, onvalue=True, offvalue=False, command=has_changed)
        if self.auto_seg_result_frequency_data: self.auto_seg_result_frequency_var.set(True)
        else: self.auto_seg_result_frequency_var.set(False)
        self.auto_seg_result_frequency.grid(row=1, column=0, sticky="nw", padx=15, pady=3)

        self.auto_seg_result_class_var = tk.BooleanVar()
        self.auto_seg_result_class = tk.Checkbutton(self.seg_label_frame, text="是否进行词性标注", variable=self.auto_seg_result_class_var, onvalue=True, offvalue=False, command=has_changed)
        if self.auto_seg_result_class_data: self.auto_seg_result_class_var.set(True)
        else: self.auto_seg_result_class_var.set(False)
        self.auto_seg_result_class.grid(row=2, column=0, sticky="nw", padx=15, pady=3)

        self.hmm_var = tk.BooleanVar()
        self.hmm_button = tk.Checkbutton(self.seg_label_frame, text="是否开启HMM（可能增加耗时）", variable=self.hmm_var, onvalue=True, offvalue=False, command=has_changed)
        if self.hmm_data: self.hmm_var.set(True)
        else: self.hmm_var.set(False)
        self.hmm_button.grid(row=3, column=0, sticky="nw", padx=15, pady=3)

        self.frame0 = tk.Frame(self.seg_label_frame)
        self.frame0.grid(row=4, column=0, sticky="nw", padx=15, pady=3)
        self.label0 = tk.Label(self.frame0, text="忽略项：")
        self.label0.grid(row=0, column=0)

        self.ignore_sign_var = tk.BooleanVar()
        self.ignore_sign_button = tk.Checkbutton(self.frame0, text="标点符号", variable=self.ignore_sign_var, onvalue=True, offvalue=False, command=has_changed)
        if self.ignore_sign_data: self.ignore_sign_var.set(True)
        else: self.ignore_sign_var.set(False)
        self.ignore_sign_button.grid(row=0, column=1)

        self.ignore_english_var = tk.BooleanVar()
        self.ignore_english_button = tk.Checkbutton(self.frame0, text="英文单词", variable=self.ignore_english_var, onvalue=True, offvalue=False, command=has_changed)
        if self.ignore_english_data: self.ignore_english_var.set(True)
        else: self.ignore_english_var.set(False)
        self.ignore_english_button.grid(row=0, column=2)

        """词典选项标签栏"""
        self.dic_label_frame = tk.LabelFrame(self.seg_frame, text="词典选项", labelanchor="nw", relief="groove")
        self.dic_label_frame.grid(row=1, column=0, sticky="new", padx=5, pady=5)
        self.dic_label_frame.grid_columnconfigure(0, weight=1)

        self.label1 = tk.Label(self.dic_label_frame, text="主词典选项")
        self.label1.grid(row=1, column=0, sticky="nw", padx=10, pady=3)

        self.dic_var = tk.IntVar()
        self.default_dic = tk.Radiobutton(self.dic_label_frame, text="默认词典", variable=self.dic_var, value=0, command=dic_path_radiobutton)
        self.custom_path = tk.Radiobutton(self.dic_label_frame, text="自定义词典路径（不推荐）", variable=self.dic_var, value=1, command=dic_path_radiobutton)
        self.default_dic.grid(row=2, column=0, sticky="nw", padx=15, pady=0)
        self.custom_path.grid(row=3, column=0, sticky="nw", padx=15, pady=0)

        self.frame2 = tk.Frame(self.dic_label_frame)
        self.frame2.grid(row=4, column=0, sticky="new", padx=38, pady=0)
        self.frame2.grid_columnconfigure(0, weight=1)

        self.custom_path_entry = ttk.Entry(self.frame2)
        self.custom_path_entry.grid(row=0, column=0, sticky="ew")
        self.custom_path_entry.insert("0", self.custom_path_data)
        self.custom_path_entry.state(['disabled']) # 初始禁用

        self.custom_path_button = ttk.Button(self.frame2, text="浏览...", command=custom_path_dialog)
        self.custom_path_button.grid(row=0, column=1)
        self.custom_path_button.state(['disabled']) # 初始禁用

        self.label2 = tk.Label(self.dic_label_frame)
        self.label2.grid(row=5, column=0)

        if self.dic_var_data == 0:
            self.dic_var.set(0)
            self.custom_path_entry.state(['disabled'])
            self.custom_path_button.state(['disabled'])
        else:
            self.dic_var.set(1)
            self.custom_path_entry.state(['!disabled'])
            self.custom_path_button.state(['!disabled'])

        self.custom_path_entry.bind('<Key>', self.on_refresh_entry) # 当在输入框输入任何内容时，触发函数

    def on_refresh_entry(self, event):
        self.toplevel.apply_button.state(['!disabled'])