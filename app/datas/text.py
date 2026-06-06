# 文本数据

class Text:
    def __init__(self, main_window):
        self.main_window = main_window
        self.text_data = ""

    def set_text_data(self, text):
        self.text_data = text

    def delete_text_data(self):
        self.text_data = ""

    def get_text_data(self):
        return self.text_data