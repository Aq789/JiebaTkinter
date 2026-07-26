# 主窗口创建
from PySide6.QtWidgets import QMainWindow
import app.widget_s.menu
import app.widget_s.dock_widget
import app.widget_s.central_widget
import app.widget_s.status_widget
import app.widget_s.edit_widget.word_seg_result_widget
import app.widget_s.edit_widget.word_dic_widget

import app.datas.word_seg_result
import app.datas.word_dic
import app.datas.text
import app.datas.seg_settings
import app.datas.window_settings
import app.datas.font_settings
import app.datas.statistic

import app.service.settings

def create_new_window(): # 创建窗口实例方法
    new_window = MainWindow() # 创建窗口实例
    MainWindow.windows.append(new_window) # 添加窗口到列表

def delete_new_window(): # 删除窗口实例方法
    last_window = MainWindow.windows.pop() # 将列表中最后一个窗口去掉并记录下来

class MainWindow:
    windows = []

    def __init__(self):
        self.window = QMainWindow()
        self.window.setWindowTitle("中文分词工具")
        self.window.resize(1000, 600)
        self.window.show()

        # 初始化数据集
        self.seg_settings_datas = app.datas.seg_settings.SegSettings(self)
        self.window_settings_datas = app.datas.window_settings.WindowSettings(self)
        self.font_settings_datas = app.datas.font_settings.FontSettings(self)
        self.word_seg_result_datas = app.datas.word_seg_result.WordSegResultDatas(self)
        self.word_dic_datas = app.datas.word_dic.WordDicDatas(self)
        self.text_datas = app.datas.text.Text(self)
        self.statistic_datas = app.datas.statistic.Statistic(self)

        # 加载配置文件
        app.service.settings.seg_settings_to_data(self)
        app.service.settings.window_settings_to_data(self)
        app.service.settings.font_settings_to_data(self)

        # 主窗口应用配置
        self.set_window_size()

        # 加载模块
        self.menu = app.widget_s.menu.Menu(self)
        self.central_widget = app.widget_s.central_widget.CentralWidget(self)
        self.dock_widget = app.widget_s.dock_widget.DockWidget(self)
        self.status_widget = app.widget_s.status_widget.StatusWidget(self)

    # 销毁窗口
    def destroy_window(self):
        if self.window:
            self.window.close()

    # 获取主窗口大小
    def get_window_size(self):
        return self.window.width(), self.window.height()

    # 改变主窗口大小
    def set_window_size(self):
        weight = self.window_settings_datas.get_window_weight_data()
        height = self.window_settings_datas.get_window_height_data()
        self.window.resize(weight, height)

    # 创建编辑分词结果窗口
    def create_word_seg_result_widget(self):
        return app.widget_s.edit_widget.word_seg_result_widget.WordSegResultWidget(self)

    # 创建编辑词典窗口
    def create_word_dic_widget(self):
        return app.widget_s.edit_widget.word_dic_widget.WordDicWidget(self)