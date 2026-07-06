# 窗口设置数据
class WindowSettings:
    def __init__(self, main_window):
        self.main_window = main_window

        self.window_weight_data = 800
        self.window_height_data = 450
        self.auto_enter_data = True

    # 窗口宽度
    def get_window_weight_data(self):
        return self.window_weight_data

    def set_window_weight_data(self, data):
        self.window_weight_data = data

    # 窗口高度
    def get_window_height_data(self):
        return self.window_height_data

    def set_window_height_data(self, data):
        self.window_height_data = data

    # 自动换行
    def open_auto_enter_data(self):
        self.auto_enter_data = True

    def close_auto_enter_data(self):
        self.auto_enter_data = False

    def get_auto_enter_data(self):
        return self.auto_enter_data