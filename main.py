# 根程序开始
import tkinter as tk
import app.view

if __name__ == '__main__':
    root = tk.Tk()  # 创建根窗口
    root.withdraw()  # 创建之后隐藏

    app.view.view_root = root  # 将根窗口传入view.py
    app.view.create_new_window()  # 创建第一个主窗口
    """此处可添加test.test_window类的create_test_window()来测试窗口"""

    root.mainloop()  # 保持程序运行