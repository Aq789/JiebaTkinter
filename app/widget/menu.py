# 菜单栏
import tkinter as tk

class Menu:
    def __init__(self, window):
        self.menubar = tk.Menu(window)

        # 文件菜单 - file_menu
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="文件", menu=self.file_menu)
        self.file_menu.add_command(label="新建")
        self.file_menu.add_command(label="打开")
        self.file_menu.add_command(label="保存")
        self.file_menu.add_command(label="另存为")
        self.file_menu.add_separator()

        import_file = tk.Menu(self.file_menu, tearoff=0)
        self.file_menu.add_cascade(label="导入...", menu=import_file)
        import_file.add_command(label="导入文本文件")
        import_file.add_command(label="导入字典文件")

        export_file = tk.Menu(self.file_menu, tearoff=0)
        self.file_menu.add_cascade(label="导出...", menu=export_file)
        export_file.add_command(label="导出文本文件")
        export_file.add_command(label="导出字典文件")
        export_file.add_command(label="导出分词结果")

        # 编辑菜单
        self.edit_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="编辑", menu=self.edit_menu)
        self.edit_menu.add_command(label="撤销")
        self.edit_menu.add_command(label="恢复")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="复制")
        self.edit_menu.add_command(label="剪切")
        self.edit_menu.add_command(label="粘贴")
        self.edit_menu.add_command(label="查找")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="编辑分词结果")
        self.edit_menu.add_command(label="编辑词典")

        # 查看菜单
        self.check_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="查看", menu=self.check_menu)
        self.check_menu.add_command(label="字体")
        self.check_menu.add_command(label="隐藏状态栏")
        self.check_menu.add_command(label="自动换行")
        self.check_menu.add_command(label="统计")

        # 帮助菜单
        self.help_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="帮助", menu=self.help_menu)
        self.help_menu.add_command(label="欢迎")
        self.help_menu.add_separator()
        self.help_menu.add_command(label="帮助")
        self.help_menu.add_command(label="关于...")

        window.config(menu=self.menubar)