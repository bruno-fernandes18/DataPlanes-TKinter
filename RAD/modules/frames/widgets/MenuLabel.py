import tkinter as tk

class MenuLabel:
    '''Preset Label object.'''
    def __init__(self, master_param: tk.Frame, displayed_text: str = '', bg_param:str = 'white', fg_param:str = 'black'):
        self.lbl = tk.Label(master=master_param, text=displayed_text if displayed_text else '', bg=bg_param if bg_param else 'white', fg=fg_param if fg_param else 'black')
    def GenericLabel(self, padx_param: int = 10, pady_param: int = 6, width_param: int = 31) -> tk.Label:
        self.lbl.config(font=('Courier', 9), width=width_param if width_param else 31)
        self.lbl.pack(padx=padx_param if padx_param else 10, pady= pady_param if pady_param else 6)
        return(self.lbl)
    def CategoryLabel(self, side_param: str = 'top') -> tk.Label:
        self.lbl.config(font=('Courier', 9))
        self.lbl.pack(padx=15, side=side_param if side_param else 'top')
        return(self.lbl)
    def ImageLabel(self, img: tk.PhotoImage = None):
        self.lbl.config(image=img if img else None, borderwidth=0)
        self.lbl.pack()
        return(self.lbl)
    def LoginLabel(self, side_param: str = 'top') -> tk.Label:
        self.lbl.config(fg = 'darkblue', bg = 'cyan', font=('Helvetica', 9), relief='solid', width=10)
        self.lbl.pack(side= side_param if side_param else 'top')
        return(self.lbl)
    def AccountLabel(self, side_param: str = 'top') -> tk.Label:
        self.lbl.config(width=20, bg='#f0f0f0', font=('Verdana', 10))
        self.lbl.pack(side= side_param if side_param else 'top')
        return(self.lbl)
    def SelectionLabel(self) -> tk.Label:
        self.lbl.config(bg='darkblue', fg='lightgreen', font=('Zapf Chancery', 48))
        self.lbl.pack(pady=5, anchor='center')
        return(self.lbl)