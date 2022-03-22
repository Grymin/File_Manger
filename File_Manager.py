import easygui
import os
import shutil
import tkinter as tk
from tkinter import filedialog


class Box:
    def __init__(self):
        self.fpath = None

    def window(self):
        # TO DO FILL THIS
        self.fpath = easygui.fileopenbox()
        self.fname =

    def f_open(self):
        os.startfile(self.fpath)

    def f_copy(self):
        dest = filedialog.askdirectory()
        shutil.copy(self.fpath, dest)
        tk.messagebox.showinfo('ok', "ok")

a = Box()
a.window()
a.f_copy()