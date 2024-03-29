import easygui
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class FileManager:
    """
    TKinter app to manage files
    """

    def __init__(self):

        # Chosen file information
        self.fpath = None
        self.fname = None
        self.path = None
        self.extension = None

        # Initialize the window
        self.root = tk.Tk()
        self.root.geometry("780x100")
        self.root.title("File Manager")

        # Buttons with possibilities in the manager
        h = 2
        w = 13
        px = 5
        tk.Button(height=h, width=w, bg="white", command=lambda: self.open_file(),
                  text="Open file").grid(row=1, column=1, padx=px, pady=30)
        tk.Button(height=h, width=w, bg="white", command=lambda: self.rename_file(),
                  text="Rename file").grid(row=1, column=2, padx=px)
        tk.Button(height=h, width=w, bg="white", command=lambda: self.move_file(),
                  text="Move file").grid(row=1, column=3, padx=px)
        tk.Button(height=h, width=w, bg="white", command=lambda: self.copy_file(),
                  text="Copy file").grid(row=1, column=4, padx=px)
        tk.Button(height=h, width=w, bg="white", command=lambda: self.delete_file(),
                  text="Delete file").grid(row=1, column=5, padx=px)
        tk.Button(height=h, width=w, bg="white", command=lambda: self.create_folder(),
                  text="Create folder").grid(row=1, column=6, padx=px)
        tk.Button(height=h, width=w, bg="white", command=lambda: self.delete_folder(),
                  text="Delete folder").grid(row=1, column=7, padx=px)

        self.root.mainloop()

    def choose_file(self):
        self.fpath = easygui.fileopenbox()
        self.fname = os.path.basename(self.fpath)
        self.path = os.path.dirname(self.fpath)
        self.extension = self.fname.split('.')[1]
        print("CHOOSE_FILE:", self.fpath, self.fname, self.path, self.extension)

    def open_file(self):
        self.choose_file()
        os.startfile(self.fpath)

    def rename_file(self):
        self.choose_file()
        name = easygui.enterbox("New name of the file:", "New name", "New_name")
        new_fpath = os.path.join(self.path, '.'.join((name, self.extension)))
        if os.path.exists(new_fpath):
            tk.messagebox.showerror("UPS!", "File exists!")
        else:
            os.rename(self.fpath, new_fpath)
            tk.messagebox.showinfo("ok!", "File renamed")

    def move_file(self):
        self.choose_file()
        dest = filedialog.askdirectory()
        new_fpath = os.path.join(dest, self.fname)
        if os.path.exists(new_fpath):
            tk.messagebox.showerror("UPS!", "Such a file exists in this direction!")
        else:
            shutil.move(self.fpath, dest)
            tk.messagebox.showinfo("ok!", "File moved")

    def copy_file(self):
        self.choose_file()
        dest = filedialog.askdirectory()
        new_fpath = os.path.join(dest, self.fname)
        if os.path.exists(new_fpath):
            tk.messagebox.showerror("UPS!", "Such a file exists in this direction!")
        else:
            shutil.copy(self.fpath, dest)
            tk.messagebox.showinfo('SUCCESS', "File copied")

    def delete_file(self):
        self.choose_file()
        os.remove(self.fpath)
        tk.messagebox.showinfo('SUCCESS', "File deleted")

    @staticmethod
    def create_folder():
        dest = filedialog.askdirectory()
        name = easygui.enterbox("Name of the folder:", "New folder", "New_folder")
        os.mkdir(os.path.join(dest, name))
        tk.messagebox.showinfo('SUCCESS', "Direction created")

    @staticmethod
    def delete_folder():
        dest = filedialog.askdirectory()
        os.rmdir(os.path.join(dest, dest))
        tk.messagebox.showinfo('SUCCESS', "Direction deleted")

a = FileManager()
