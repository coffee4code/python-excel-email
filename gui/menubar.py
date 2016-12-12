from tkinter import *


class Menubar:

    def __init__(self, root):
        menubar = Menu(root)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=root.quit)
        filemenu.add_command(label="Open", command=root.quit)
        filemenu.add_command(label="Save", command=root.quit)
        filemenu.add_command(label="Save as...", command=root.quit)
        filemenu.add_command(label="Close", command=root.quit)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)


        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=root.quit)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=root.quit)
        editmenu.add_command(label="Copy", command=root.quit)
        editmenu.add_command(label="Paste", command=root.quit)
        editmenu.add_command(label="Delete", command=root.quit)
        editmenu.add_command(label="Select All", command=root.quit)
        menubar.add_cascade(label="Edit", menu=editmenu)


        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=root.quit)
        helpmenu.add_command(label="About...", command=root.quit)
        menubar.add_cascade(label="Help", menu=helpmenu)

        root.config(menu=menubar)