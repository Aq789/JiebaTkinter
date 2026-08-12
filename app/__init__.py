from pathlib import Path

from PySide6.QtCore import Qt, QFile, QTextStream
from PySide6.QtGui import QIcon, QPixmap, QPainter
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QToolBar

ROOT_DIR = Path(__file__).parent.parent
ICON_DIR = ROOT_DIR / "resources" / "icons"
STYLE_DIR = ROOT_DIR / "resources" / "styles"

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

# 获取样式表
def get_style(filename: str):
    style_path = STYLE_DIR / filename
    file = QFile(style_path)
    if file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(file)
        style_sheet = stream.readAll()
        return style_sheet
    return None

def do_refresh_icon():
    clear_icon_cache()
    app = QApplication.instance()

    for widget in app.allWidgets():
        if isinstance(widget, QMainWindow):
            menubar = widget.menuBar()
            if menubar:
                def get_all_actions(menu):
                    actions = []
                    for action in menu.actions():
                        sub_menu = action.menu()
                        if sub_menu:
                            actions.extend(get_all_actions(sub_menu))
                        actions.append(action)
                    return actions

                all_actions = get_all_actions(menubar)
                for action in all_actions:
                    if hasattr(action, 'icon_name'):
                        action.setIcon(get_icon(action.icon_name))

                menubar.update()
                menubar.repaint()

            all_menus = widget.findChildren(QMenu)
            for menu in all_menus:
                if hasattr(menu, 'icon_name'):
                    menu.setIcon(get_icon(menu.icon_name))
                    menu.update()
                    menu.repaint()

            for toolbar in widget.findChildren(QToolBar):
                for action in toolbar.actions():
                    if hasattr(action, 'icon_name'):
                        action.setIcon(get_icon(action.icon_name))

                toolbar.update()
                toolbar.repaint()

def clear_icon_cache():
    _icon_cache.clear()