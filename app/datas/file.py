# 文件状态数据
import os

class File:
    def __init__(self, main_window):
        self.main_window = main_window

        self.is_filed_data = False
        self.file_path_data = ""
        self.file_saved_data = True

    # 是否打开至文件
    def set_is_filed_data(self, data):
        self.is_filed_data = data

    def get_is_filed_data(self):
        return self.is_filed_data

    # 文件路径
    def set_file_path_data(self, data):
        self.file_path_data = data

    def get_file_path_data(self):
        return self.file_path_data

    # 获取文件名
    def get_file_name_data(self):
        return os.path.basename(self.get_file_path_data())

    # 保存状态
    def set_filed_saved_data(self, data):
        self.file_saved_data = data

    def get_filed_saved_data(self):
        return self.file_saved_data

    # 检查是否存在文件
    def check_is_filed(self):
        if self.is_filed_data:
            try:
                open(f"{self.file_path_data}", "r")
            except FileNotFoundError:
                return False
            except PermissionError:
                return False
            return True
        else:
            return False
