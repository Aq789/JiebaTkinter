import os
from pathlib import Path
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QApplication

ROOT_DIR = Path(__file__).parent.parent
ICON_DIR = ROOT_DIR / "resources" / "icons"

_icon_cache = {}

# 加载svg并自动染色
def get_icon(filename: str, size: int = 128) -> QIcon:
    app = QApplication.instance()
    if not app:
        return QIcon()  # 容错处理

    color = app.palette().text().color() # 获取当前主题的文字颜色

    cache_key = f"{filename}_{color.name()}_{size}" # 构建缓存键
    if cache_key in _icon_cache:
        return _icon_cache[cache_key]

    svg_path = ICON_DIR / filename # 加载svg
    if not svg_path.exists():
        return QIcon()

    renderer = QSvgRenderer(str(svg_path))
    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.GlobalColor.transparent)  # 透明背景

    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
    painter.fillRect(pixmap.rect(), color)
    painter.end()

    icon = QIcon(pixmap)
    _icon_cache[cache_key] = icon
    return icon

def clear_icon_cache():
    _icon_cache.clear()