# 将设置配置保存到磁盘中
from pathlib import Path
import json
import app.service.settings

# 获得配置目录
def get_user_config_path():
    base = Path.home() / "AppData" / "Local"
    config_dir = base / "JiebaTool"
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir

# 保存分词配置
def save_seg_settings(seg_settings):
    with open(f"{get_user_config_path()}/seg_settings.json", "w", encoding="utf-8") as f:
        json.dump(app.service.settings.seg_settings_to_dict(seg_settings), f, indent=4, ensure_ascii=False)

# 保存窗口配置
def save_window_settings(window_settings):
    with open(f"{get_user_config_path()}/window_settings.json", "w", encoding="utf-8") as f:
        json.dump(app.service.settings.window_settings_to_dict(window_settings), f, indent=4, ensure_ascii=False)

# 保存字体配置
def save_font_settings(font_settings):
    with open(f"{get_user_config_path()}/font_settings.json", "w", encoding="utf-8") as f:
        json.dump(app.service.settings.font_settings_to_dict(font_settings), f, indent=4, ensure_ascii=False)

# 加载分词配置
def load_seg_settings():
    try:
        with open(f"{get_user_config_path()}/seg_settings.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {
            "seg_mode_data": 0,
            "auto_seg_result_frequency_data": True,
            "auto_seg_result_class_data": True,
            "hmm_data": False,
            "chinese_word_class_data": False,
            "ignore_sign_data": True,
            "ignore_english_data": False,
            "dic_var_data": 0,
            "custom_path": ""
        }
    return data

# 加载窗口配置
def load_window_settings():
    try:
        with open(f"{get_user_config_path()}/window_settings.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {
            "window_weight_data": 800,
            "window_height_data": 450
        }
    return data

# 加载字体配置
def load_font_settings():
    try:
        with open(f"{get_user_config_path()}/font_settings.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {
            "font_data": "宋体",
            "shape_data": "常规",
            "size_data": 14,
            "under_line_data": False,
            "delete_line_data": False,
            "color_data": "#000000"
        }
    return data