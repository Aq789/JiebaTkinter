# 根程序开始
import sys
import app.view_s as a_v
import test.test_window_s as t_tw
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    a_v.create_new_window()
    test_win = t_tw.create_test_window()

    app.exec()