# 测试窗口的打开和关闭
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
import app.view_s as a_v

def create_test_window():
    test_window = QWidget()
    test_window.setWindowTitle("测试窗口")
    test_window.resize(400, 300)

    new_button = QPushButton("点击新建窗口")
    delete_button = QPushButton("点击删除窗口")

    new_button.clicked.connect(a_v.create_new_window)
    delete_button.clicked.connect(a_v.delete_new_window)

    t_layout = QVBoxLayout()
    t_layout.addWidget(new_button)
    t_layout.addWidget(delete_button)

    test_window.setLayout(t_layout)
    test_window.show()

    return test_window