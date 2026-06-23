import tkinter as tk
from tkinter import ttk
from tkinter import font


class FontEditorPanel:
    def __init__(self, root):
        self.root = root
        root.title("自定义字体界面")

        # 1. 获取系统所有字体族（用于下拉框）
        self.families = sorted(font.families())

        # 2. 创建字体对象（用于管理当前字体）
        self.current_font = font.Font(family="微软雅黑", size=20, weight="normal", slant="roman")

        # ---------- 搭建界面控件 ----------
        # 控制区域（放在顶部）
        control_frame = ttk.Frame(root, padding=10)
        control_frame.pack(fill="x")

        # 字体族下拉框
        ttk.Label(control_frame, text="字体:").pack(side="left", padx=5)
        self.family_var = tk.StringVar(value="微软雅黑")
        family_combo = ttk.Combobox(control_frame, textvariable=self.family_var,
                                    values=self.families, width=20, state="readonly")
        family_combo.pack(side="left", padx=5)
        family_combo.bind("<<ComboboxSelected>>", self.update_font)

        # 字号微调框
        ttk.Label(control_frame, text="字号:").pack(side="left", padx=5)
        self.size_var = tk.IntVar(value=20)
        size_spin = ttk.Spinbox(control_frame, from_=8, to=72, textvariable=self.size_var,
                                width=5, command=self.update_font)
        size_spin.pack(side="left", padx=5)
        size_spin.bind("<KeyRelease>", self.update_font)  # 手动输入时触发

        # 粗体复选框
        self.bold_var = tk.BooleanVar(value=False)
        bold_check = ttk.Checkbutton(control_frame, text="粗体", variable=self.bold_var,
                                     command=self.update_font)
        bold_check.pack(side="left", padx=10)

        # 斜体复选框
        self.italic_var = tk.BooleanVar(value=False)
        italic_check = ttk.Checkbutton(control_frame, text="斜体", variable=self.italic_var,
                                       command=self.update_font)
        italic_check.pack(side="left", padx=10)

        # 预览区域（放在中间，内容可编辑）
        preview_frame = ttk.Frame(root, padding=10)
        preview_frame.pack(fill="both", expand=True)

        self.preview_text = tk.Text(preview_frame, height=8, wrap="word")
        self.preview_text.pack(fill="both", expand=True)
        self.preview_text.insert("1.0", "欢迎来到字体编辑器！\n你可以在这里实时预览字体变化。")

        # 初始应用字体
        self.update_font()

    def update_font(self, event=None):
        """根据当前控件状态，更新字体并应用到预览框"""
        family = self.family_var.get()
        size = self.size_var.get()

        # 处理粗体 (weight: normal / bold)
        weight = "bold" if self.bold_var.get() else "normal"
        # 处理斜体 (slant: roman / italic)
        slant = "italic" if self.italic_var.get() else "roman"

        # 配置字体对象
        self.current_font.config(family=family, size=size, weight=weight, slant=slant)
        # 将字体应用到 Text 控件
        self.preview_text.config(font=self.current_font)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x300")
    app = FontEditorPanel(root)
    root.mainloop()