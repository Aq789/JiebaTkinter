# 根程序开始
import tkinter as tk
import app.view
import app.datas.word_seg_result as d_wsr
import test.test_window

if __name__ == '__main__':
    root = tk.Tk()  # 创建根窗口
    root.withdraw()  # 创建之后隐藏

    app.view.view_root = root  # 将根窗口传入view.py
    app.view.create_new_window()  # 创建第一个主窗口

    """此处可添加test.test_window类的create_test_window()来测试窗口"""
    d_wsr.add_word_seg_result('000', 0, 'n')
    d_wsr.add_word_seg_result('111', 1, 'n')
    d_wsr.add_word_seg_result('222', 2, 'n')
    d_wsr.add_word_seg_result('333', 3, 'n')
    d_wsr.add_word_seg_result('444', 4, 'n')
    d_wsr.add_word_seg_result('555', 5, 'n')
    d_wsr.add_word_seg_result('666', 6, 'n')
    d_wsr.add_word_seg_result('777', 7, 'n')
    d_wsr.add_word_seg_result('888', 8, 'n')
    d_wsr.add_word_seg_result('999', 9, 'n')
    d_wsr.add_word_seg_result('101010', 10, 'n')
    d_wsr.add_word_seg_result('111111', 11, 'n')
    d_wsr.add_word_seg_result('121212', 12, 'n')
    d_wsr.add_word_seg_result('131313', 13, 'n')
    d_wsr.add_word_seg_result('141414', 14, 'n')

    root.mainloop()  # 保持程序运行