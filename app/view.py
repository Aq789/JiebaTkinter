# 主窗口创建
from PySide6.QtGui import QAction
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QPlainTextEdit, QTableWidget, QMenu
from app import clear_icon_cache, get_icon
import app.widget.menu
import app.widget.dock_widget
import app.widget.central_widget
import app.widget.status_widget
import app.widget.edit_widget.word_seg_result_widget
import app.widget.edit_widget.word_dic_widget
import app.widget.check_widget

import app.datas.word_seg_result
import app.datas.word_dic
import app.datas.text
import app.datas.seg_settings
import app.datas.window_settings
import app.datas.font_settings
import app.datas.statistic
import app.datas.file

import app.service.settings

import app.controllers.file as c_f

def create_new_window(): # 创建窗口实例方法
    new_window = MainWindow() # 创建窗口实例
    MainWindow.windows.append(new_window) # 添加窗口到列表

def delete_new_window(): # 删除窗口实例方法
    last_window = MainWindow.windows.pop() # 将列表中最后一个窗口去掉并记录下来
    last_window.destroy_window()

def on_theme_changed(): # 系统主题切换
    QTimer.singleShot(50, do_refresh)

def do_refresh():
    clear_icon_cache()
    for widget in QApplication.topLevelWidgets():
        if isinstance(widget, QMainWindow):
            menubar = widget.menuBar()
            if not menubar:
                continue

            def get_all_actions(menu): # 递归函数：获取所有 QAction（包括子菜单里的）
                actions = []
                for action in menu.actions():
                    sub_menu = action.menu()
                    if sub_menu:  # 如果有子菜单
                        actions.extend(get_all_actions(sub_menu))
                    actions.append(action)
                return actions

            all_actions = get_all_actions(menubar)
            for action in all_actions:
                if hasattr(action, 'icon_name'):
                    action.setIcon(get_icon(action.icon_name))

            menubar.update() # 强制刷新菜单栏及其所有子菜单
            menubar.repaint()
            for menu in menubar.findChildren(QMenu):
                menu.update()
                menu.repaint()

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
        self.file_datas = app.datas.file.File(self)

        # 加载配置文件
        app.service.settings.seg_settings_to_data(self)
        app.service.settings.window_settings_to_data(self)
        app.service.settings.font_settings_to_data(self)

        # 主窗口应用配置
        self.set_window_size()
        self.change_window_title("未命名")
        self.window_move()

        # 加载模块
        self.menu = app.widget.menu.Menu(self)
        self.central_widget = app.widget.central_widget.CentralWidget(self)
        self.dock_widget = app.widget.dock_widget.DockWidget(self)
        self.status_widget = app.widget.status_widget.StatusWidget(self)

        self.window.closeEvent = self.close_event

    # 销毁窗口
    def destroy_window(self):
        if self.window:
            self.window.close()

    # 窗口偏移计算
    def window_move(self):
        max_offset = 300
        number = len(self.windows)
        offset = 30 * number
        if offset > max_offset:
            offset = max_offset
        self.window.move(300 + offset, 100 + offset)

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
        return app.widget.edit_widget.word_seg_result_widget.WordSegResultWidget(self)

    # 创建编辑词典窗口
    def create_word_dic_widget(self):
        return app.widget.edit_widget.word_dic_widget.WordDicWidget(self)

    # 创建查找窗口
    def create_check_widget(self):
        return app.widget.check_widget.CheckWidget(self)

    # 修改标题栏
    def change_window_title(self, text):
        self.window.setWindowTitle(f"{text}  -  中文分词工具")

    # 关闭窗口事件
    def close_event(self, event):
        if c_f.close_event(self, event):
            temp_window = self
            self.windows.remove(temp_window)

    # 退出事件
    def on_close(self):
        self.window.close()

    # 保存状态更改
    def change_saved(self, state):
        if state:
            self.status_widget.saved.setText("已保存")
            self.file_datas.set_filed_saved_data(True)
            self.file_datas.set_is_filed_data(True)
            self.change_window_title(self.file_datas.get_file_name_data())
        else:
            self.status_widget.saved.setText("未保存")
            self.file_datas.set_filed_saved_data(False)

    # 获取窗口焦点
    @staticmethod
    def get_focus():
        widget = QApplication.focusWidget()
        if isinstance(widget, QPlainTextEdit): # 当焦点在编辑框时
            return 0
        if isinstance(widget, QTableWidget): # 当焦点在表格时
            return 1
        return -1