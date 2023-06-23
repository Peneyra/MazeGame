import tkinter as tk
import time

root = tk.Tk()
root.geometry("300x300")
root.title("   M a z e   ")

t = "0"
s = "123456789012345678901234567890"

pg = tk.Text(root, height = 30, width = 30)

pg.pack()


for i in s:
    t = i
    pg.insert(tk.END, t)
    tk.mainloop()

