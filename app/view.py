# 主窗口创建
import tkinter as tk
import app.widget.menu
import app.widget.paned_window
import app.widget.status_bar
import app.widget.left_frame
import app.widget.right_frame
import app.widget.edit_toplevel.seg_result_toplevel
import app.widget.edit_toplevel.word_dic_toplevel

import app.controllers.left_frame
import app.controllers.edit_toplevel.seg_result_toplevel

import app.datas.word_seg_result
import app.datas.word_dic
import app.datas.seg_settings

import app.service.settings

def create_new_window(root): # 创建窗口实例方法
    new_window = MainWindow(root) # 创建窗口实例
    MainWindow.windows.append(new_window) # 添加窗口到列表

def delete_new_window(): # 删除窗口实例方法
    last_window = MainWindow.windows.pop() # 将列表中最后一个窗口去掉并记录下来
    last_window.destroy_window() # 销毁最后一个窗口

class MainWindow:
    windows = [] # 公共属性：用来记录创建的窗口

    def __init__(self, root): # 主界面构造函数
        self.main_window = tk.Toplevel(root)
        self.main_window.title("中文分词工具")
        self.main_window.geometry("800x450")
        self.main_window.protocol("WM_DELETE_WINDOW", self.close_window)

        # 初始化数据集
        self.seg_settings_datas = app.datas.seg_settings.SegSettings(self.main_window) # 创建分词设置数据集
        self.word_seg_result_datas = app.datas.word_seg_result.WordSegResultDatas(self.main_window)  # 创建分词结果数据集
        self.word_dic_datas = app.datas.word_dic.WordDicDatas(self.main_window) # 创建词典数据集

        # 加载配置文件
        app.service.settings.seg_settings_to_data(self) # 从磁盘中加载分词设置

        # 加载模块
        self.menu = app.widget.menu.Menu(self) # 加载menu模块
        self.paned_window = app.widget.paned_window.PanedWindow(self) # 加载分隔条模块
        self.status_bar = app.widget.status_bar.StatusBar(self) # 加载底部状态栏模块

    def destroy_window(self):
        if self.main_window:
            self.main_window.destroy()

    def close_window(self): # 关闭窗口时触发的函数
        """后续需要在这里添加关闭确认机制"""
        if len(MainWindow.windows) == 1: exit()
        else:
            self.windows.remove(self)
            self.main_window.destroy()