# !/usr/bin/python3
from tkinter import *
from .menubar import Menubar


class Application:
    def __init__(self):
        root = Tk()
        root.geometry('{}x{}'.format(800, 600))

        Menubar(root)

        root.mainloop()


