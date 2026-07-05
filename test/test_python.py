import tkinter as tk
from tkinter import ttk

def on_slide(val):
    label.config(text=f"数值: {int(float(val))}")

root = tk.Tk()
root.title("现代化滑块示例")

# 使用 clam 主题以获得更好看的扁平化外观（可选，但很好）
style = ttk.Style()

scale = ttk.Scale(root, from_=0, to_=100, orient="horizontal",
                  command=on_slide, length=300)
scale.pack(pady=20)

label = ttk.Label(root, text="数值: 0", font=("Arial", 14))
label.pack()

root.mainloop()