# 主窗口创建
import tkinter as tk
view_root = None # 全局变量，用来记录根窗口

def create_new_window(): # 创建窗口实例方法
    global view_root
    new_window = MainWindow(view_root) # 创建窗口实例
    MainWindow.windows.append(new_window) # 添加窗口到列表

def delete_new_window(): # 删除窗口实例方法
    last_window = MainWindow.windows.pop() # 将列表中最后一个窗口去掉并记录下来
    last_window.destroy_window() # 销毁最后一个窗口

class MainWindow:
    windows = [] # 公共属性：用来记录创建的窗口

    def __init__(self, root): # 主界面构造函数
        self.main_window = tk.Toplevel(root)
        self.main_window.title("中文分词工具")
        self.main_window.geometry("400x300")
        self.main_window.protocol("WM_DELETE_WINDOW", self.close_window)

    def destroy_window(self):
        if self.main_window:
            self.main_window.destroy()

    def close_window(self):
        """后续需要在这里添加关闭确认机制"""
        if len(MainWindow.windows) == 1: exit()
        else:
            self.windows.remove(self)
            self.main_window.destroy()