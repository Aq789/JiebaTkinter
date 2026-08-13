# 根程序开始
import sys

from PySide6.QtCore import QTranslator, QLibraryInfo
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from pathlib import Path

import app.view as a_v

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.paletteChanged.connect(a_v.on_theme_changed)

    ROOT_DIR = Path(__file__).parent
    icon_path = str(ROOT_DIR / "resources" / "icons" / "ico.png")
    app.setWindowIcon(QIcon(icon_path))

    # 中文包加载
    translator = QTranslator()
    if translator.load("qt_zh_CN", QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)):
        app.installTranslator(translator)
    else:
        pass

    a_v.create_new_window()

    app.exec()