import tkinter as tk
from tkinter import ttk

class MenuComboBox:
    def __init__(self, master_param: tk.Tk, txt_param: tk.StringVar, value_param: tuple):
        self.cb = ttk.Combobox(master=master_param, textvariable=txt_param)
        self.cb['values'] = value_param
    def NameComboBox(self):
        self.cb.pack(pady=5)
        return(self.cb)