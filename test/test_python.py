import sys
import traceback

# 定义一个全局变量用于存储错误信息
last_error_message = ""

def global_exception_handler(exc_type, exc_value, exc_tb):
    global last_error_message
    # 格式化成字符串并保存到变量
    last_error_message = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print(last_error_message, "1")
    # 可选：同时打印到控制台
    print("错误已捕获并保存到变量中")
    # 不退出程序，以便后续可以访问 last_error_message
    # 如果想退出，可调用 sys.exit(1)

sys.excepthook = global_exception_handler

# 测试代码
def buggy():
    1/0

buggy()

# 此时错误信息已经保存在 last_error_message 中
print("保存的错误信息：")
print(last_error_message, "2")