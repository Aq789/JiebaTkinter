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
    d_wsr.add_word_seg_result('空格', 0, 'n')
    d_wsr.add_word_seg_result('输入', 1, 'n')
    d_wsr.add_word_seg_result('故事', 2, 'n')
    d_wsr.add_word_seg_result('词典', 3, 'n')
    d_wsr.add_word_seg_result('百科', 4, 'n')
    d_wsr.add_word_seg_result('学校', 5, 'n')
    d_wsr.add_word_seg_result('百草园', 6, 'n')
    d_wsr.add_word_seg_result('窗口', 7, 'n')
    d_wsr.add_word_seg_result('隐藏', 8, 'n')
    d_wsr.add_word_seg_result('移动', 9, 'n')
    d_wsr.add_word_seg_result('三味书屋', 10, 'n')
    d_wsr.add_word_seg_result('程序', 11, 'n')
    d_wsr.add_word_seg_result('编辑', 12, 'n')
    d_wsr.add_word_seg_result('哔哩哔哩大学', 13, 'n')
    d_wsr.add_word_seg_result('拼音', 14, 'n')

    root.mainloop()  # 保持程序运行