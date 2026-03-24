# 编辑词典窗口
import tkinter as tk

class WordDicToplevel:
    def __init__(self, window, callback):
        self.edit_word_dic_window = tk.Toplevel(window)
        self.edit_word_dic_window.title("编辑词典")
        self.edit_word_dic_window.transient(window) # 子窗口在父窗口之上
        self.edit_word_dic_window.wm_attributes("-toolwindow", True) # 只保留关闭按钮
        self.edit_word_dic_window.geometry("400x300+480+180") # 窗口大小和初始位置
        self.edit_word_dic_window.resizable(False, False) # 禁止调整窗口大小

        self.callback = callback # 保存回调函数
        self.edit_word_dic_window.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self): # 关闭执行的方法
        if self.callback: self.callback() # 先调用回调（恢复按钮）
        self.edit_word_dic_window.destroy()