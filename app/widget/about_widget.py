# 关于窗口
from PySide6.QtGui import QPixmap, QDesktopServices
from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QVBoxLayout, QPushButton, QApplication, QMessageBox
from PySide6.QtCore import Qt, QUrl

from app import ICON_DIR

version = "v0.6.6-alpha (Build 20260813)"

class AboutWidget:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = self.main_window.window
        self.about_widget = QDialog()
        self.about_widget.setWindowTitle("关于")
        self.about_widget.setModal(True)
        self.about_widget.setFixedSize(320, 240)

        self.layout1 = QVBoxLayout()

        self.layout = QHBoxLayout()

        self.pixmap = QPixmap(f"{ICON_DIR}/ico.png").scaled(
            70, 70,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.label = QLabel()
        self.label.setPixmap(self.pixmap)
        self.layout.addWidget(self.label)

        text = f'''
        JiebaTool 中文分词工具
        
        {version}
        MIT License
        邮件：
        wangjingqian123@outlook.com
        '''
        self.label1 = QLabel(text)
        self.layout.addWidget(self.label1)
        self.layout.addStretch()

        self.layout2 = QHBoxLayout()
        self.button1 = QPushButton("复制版本号")
        self.button2 = QPushButton("跳转至Github")
        self.button3 = QPushButton("关闭")

        self.layout2.addStretch()
        self.layout2.addWidget(self.button1)
        self.layout2.addWidget(self.button2)
        self.layout2.addWidget(self.button3)

        self.layout1.addLayout(self.layout)
        self.layout1.addStretch()
        self.layout1.addLayout(self.layout2)

        self.about_widget.setLayout(self.layout1)

        # 信号槽
        self.button1.clicked.connect(self.copy)
        self.button2.clicked.connect(self.to_github)
        self.button3.clicked.connect(self.close)

        self.about_widget.exec()

    @staticmethod
    def copy():
        QApplication.clipboard().setText(version)

    def to_github(self):
        url = QUrl("https://github.com/Aq789/JiebaTool")
        if not QDesktopServices.openUrl(url):
            QMessageBox.critical(self.about_widget, "错误", "无法打开浏览器，请检查系统设置")

    def close(self):
        self.about_widget.close()