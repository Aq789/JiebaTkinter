
def choose_shape(shape):
    # 映射逻辑
    if shape == "粗体":
        weight, slant = "bold", "roman"
    elif shape == "斜体":
        weight, slant = "normal", "italic"
    elif shape == "粗斜体":
        weight, slant = "bold", "italic"
    else:
        weight, slant = "normal", "roman"  # 常规
    return [weight, slant]