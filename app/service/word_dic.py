# 词典数据有关算法

# 文本转换为词典列表
def txt_to_dic(text):
    text_list = text.splitlines()
    result_list = []

    for line in text_list:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        line = line.split("#", 1)[0].rstrip()
        try:
            parts = line.split()
            if len(parts) == 0:
                continue
            elif len(parts) == 1:
                result_list.append([parts[0], "", ""])
            elif len(parts) == 2:
                if not parts[1].isdigit():
                    raise ValueError
                result_list.append([parts[0], int(parts[1]), ""])
            else:
                if not parts[1].isdigit():
                    raise ValueError
                result_list.append([parts[0], int(parts[1]), parts[2]])
        except ValueError:
            return None

    return result_list

# csv转换为词典列表
def csv_to_dic(text):
    text_list = text.splitlines()
    result_list = []

    for line in text_list:
        line_list = line.split(",")
        result_list.append(line_list)

    return result_list