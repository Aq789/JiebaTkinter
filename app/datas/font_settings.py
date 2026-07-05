# 字体设置数据
class FontSettings:
    def __init__(self, main_window):
        self.main_window = main_window

        self.font_data = "宋体"
        self.shape_data = "常规"
        self.size_data = 14
        self.under_line_data = False
        self.delete_line_data = False
        self.color_data = "#000000"

    # 字体
    def set_font_data(self, font):
        self.font_data = font

    def get_font_data(self):
        return self.font_data

    # 字形
    def set_shape_data(self, shape):
        self.shape_data = shape

    def get_shape_data(self):
        return self.shape_data

    # 字号
    def set_size_data(self, size):
        self.size_data = size

    def get_size_data(self):
        return self.size_data

    # 下划线
    def open_under_line_data(self):
        self.under_line_data = True

    def close_under_line_data(self):
        self.under_line_data = False

    def get_under_line_data(self):
        return self.under_line_data

    # 删除线
    def open_delete_line_data(self):
        self.delete_line_data = True

    def close_delete_line_data(self):
        self.delete_line_data = False

    def get_delete_line_data(self):
        return self.delete_line_data

    # 颜色
    def set_color_data(self, color):
        self.color_data = color

    def get_color_data(self):
        return self.color_data