# 测试窗口的打开和关闭
import tkinter as tk
import app.view
test_window_root = None

def create_test_window():
    global test_window_root
    root = test_window_root
    test_window = tk.Toplevel(root)
    test_window.title("测试窗口")
    test_window.geometry("400x300")

    tk.Button(test_window, text="点击新建窗口", command=app.view.create_new_window).pack()
    tk.Button(test_window, text="点击删除窗口", command=app.view.delete_new_window).pack()