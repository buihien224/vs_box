
import tkinter as tk
from ctypes import windll
try:
    import win32mica as mc
except ImportError:
    import os
    os.system("pip install win32mica")


app=tk.Tk()
app.title("Tk Dark")
app.configure(bg="#000000") # Please use BLACK as background color, otherwhise render issues might appear
app.wm_attributes("-transparent", "#000000")
app.update()
HWND=windll.user32.GetParent(app.winfo_id())
mc.ApplyMica(HWND, ColorMode=mc.MICAMODE.DARK)



app.mainloop()