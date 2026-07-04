import tkinter as tk
from tkinter import font, ttk, messagebox

class ClassicFontDialog:
    def __init__(self, root):
        self.root = root
        root.title("经典字体选择器")
        root.geometry("520x460")  # 高度比之前增加一点，容纳新控件
        # 让网格的第三列和第三行可以拉伸
        root.columnconfigure(2, weight=1)
        root.rowconfigure(1, weight=1)

        # 1. 创建“中央中枢”——共享字体对象
        self.preview_font = font.Font(family="微软雅黑", size=16, weight="normal", slant="roman")

        # 2. 准备数据源
        self.families = sorted(font.families())
        self.sizes = list(range(8, 73, 2)) + [80, 100]
        self.styles = ["常规", "粗体", "斜体", "粗斜体"]

        # 3. 搭建界面控件
        self._build_widgets()
        # 4. 设置默认选中项
        self._set_default_selections()

    def _build_widgets(self):
        """绘制所有控件"""
        # ---------- 第一行：标签 ----------
        tk.Label(self.root, text="字体(F):", font=("", 9)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.root, text="字号(S):", font=("", 9)).grid(row=0, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self.root, text="字形(Y):", font=("", 9)).grid(row=0, column=2, sticky="w", padx=5, pady=5)

        # ---------- 第二行：三个带滚动条的列表框 ----------
        # 字体列表框
        self.family_list = tk.Listbox(self.root, height=12, exportselection=False)
        family_scroll = ttk.Scrollbar(self.root, orient="vertical", command=self.family_list.yview)
        self.family_list.config(yscrollcommand=family_scroll.set)
        for f in self.families:
            self.family_list.insert("end", f)

        # 字号列表框
        self.size_list = tk.Listbox(self.root, height=12, exportselection=False, width=8)
        size_scroll = ttk.Scrollbar(self.root, orient="vertical", command=self.size_list.yview)
        self.size_list.config(yscrollcommand=size_scroll.set)
        for s in self.sizes:
            self.size_list.insert("end", str(s))

        # 样式列表框
        self.style_list = tk.Listbox(self.root, height=12, exportselection=False, width=10)
        style_scroll = ttk.Scrollbar(self.root, orient="vertical", command=self.style_list.yview)
        self.style_list.config(yscrollcommand=style_scroll.set)
        for s in self.styles:
            self.style_list.insert("end", s)

        # 放置列表和滚动条
        self.family_list.grid(row=1, column=0, sticky="nsew", padx=5)
        family_scroll.grid(row=1, column=0, sticky="ns", padx=(0, 5))

        self.size_list.grid(row=1, column=1, sticky="nsew", padx=5)
        size_scroll.grid(row=1, column=1, sticky="ns", padx=(0, 5))

        self.style_list.grid(row=1, column=2, sticky="nsew", padx=5)
        style_scroll.grid(row=1, column=2, sticky="ns", padx=(0, 5))

        # 为三栏绑定点击事件
        self.family_list.bind("<<ListboxSelect>>", self.update_preview)
        self.size_list.bind("<<ListboxSelect>>", self.update_preview)
        self.style_list.bind("<<ListboxSelect>>", self.update_preview)

        # ---------- 在样式列表下方添加“下划线”和“删除线”复选框 ----------
        extra_frame = ttk.Frame(self.root)
        extra_frame.grid(row=2, column=2, sticky="n", padx=5, pady=2)

        self.underline_var = tk.BooleanVar(value=False)
        self.overstrike_var = tk.BooleanVar(value=False)

        ttk.Checkbutton(extra_frame, text="下划线(_U)",
                        variable=self.underline_var,
                        command=self.update_preview).pack(anchor="w")
        ttk.Checkbutton(extra_frame, text="删除线(_D)",
                        variable=self.overstrike_var,
                        command=self.update_preview).pack(anchor="w")

        # ---------- 第三行：实时预览区域 (横跨三列) ----------
        preview_frame = ttk.LabelFrame(self.root, text="预览", padding=10)
        preview_frame.grid(row=3, column=0, columnspan=3, sticky="ew", padx=5, pady=10)

        self.preview_label = tk.Label(preview_frame, text="字体范例 123 ABC",
                                      font=self.preview_font,
                                      relief="sunken", bg="white", anchor="center")
        self.preview_label.pack(fill="both", expand=True, padx=5, pady=5)

        # ---------- 第四行：操作按钮 (横跨三列) ----------
        btn_frame = tk.Frame(self.root)
        btn_frame.grid(row=4, column=0, columnspan=3, sticky="e", padx=10, pady=10)

        ttk.Button(btn_frame, text="确定", command=self.on_ok).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="取消", command=self.root.destroy).pack(side="left", padx=5)

    def _set_default_selections(self):
        """初始化默认高亮：字体选中第一个，字号选中16，样式选中常规"""
        self.family_list.selection_set(0)
        self.family_list.see(0)

        try:
            size_idx = self.sizes.index(16)
        except ValueError:
            size_idx = 0
        self.size_list.selection_set(size_idx)
        self.size_list.see(size_idx)

        self.style_list.selection_set(0)  # 常规
        self.style_list.see(0)

        # 触发首次更新
        self.update_preview()

    def update_preview(self, event=None):
        """核心联动函数：从三个列表和复选框取值，配置中枢Font"""
        # 1. 获取选中的字体名
        family_selection = self.family_list.curselection()
        if family_selection:
            family = self.family_list.get(family_selection[0])
        else:
            family = self.preview_font.cget("family")

        # 2. 获取选中的字号
        size_selection = self.size_list.curselection()
        if size_selection:
            size = int(self.size_list.get(size_selection[0]))
        else:
            size = self.preview_font.cget("size")

        # 3. 获取选中的样式 (映射为 weight 和 slant)
        style_selection = self.style_list.curselection()
        if style_selection:
            style_text = self.style_list.get(style_selection[0])
            if style_text == "粗体":
                weight, slant = "bold", "roman"
            elif style_text == "斜体":
                weight, slant = "normal", "italic"
            elif style_text == "粗斜体":
                weight, slant = "bold", "italic"
            else:  # 常规
                weight, slant = "normal", "roman"
        else:
            weight = self.preview_font.cget("weight")
            slant = self.preview_font.cget("slant")

        # 4. 从复选框获取下划线和删除线状态
        underline = self.underline_var.get()
        overstrike = self.overstrike_var.get()

        # 5. 配置中枢 (预览标签自动刷新)
        self.preview_font.config(
            family=family,
            size=size,
            weight=weight,
            slant=slant,
            underline=underline,
            overstrike=overstrike
        )

        # 6. 窗口自适应
        self.root.geometry("")

    def on_ok(self):
        """点击确定时，弹出当前字体信息"""
        current = self.preview_font.actual()
        msg = (f"你选择了：\n字体: {current['family']}\n大小: {current['size']}\n"
               f"粗体: {current['weight']}\n斜体: {current['slant']}\n"
               f"下划线: {current['underline']}\n删除线: {current['overstrike']}")
        messagebox.showinfo("选择的字体", msg)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClassicFontDialog(root)
    root.mainloop()