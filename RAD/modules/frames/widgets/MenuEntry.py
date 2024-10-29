import tkinter as tk

class MenuEntry:
    def __init__(self, master_param: tk.Entry):
        self.ent = tk.Entry(master=master_param, relief='solid')
    def GenericEntry(self) -> tk.Entry:
        self.ent.pack()
        return(self.ent)
    def LoginEntry(self, side_param: str = 'top', control_LR: bool = True) -> tk.Entry:
        self.ent.config(width=30)
        if control_LR == False:
            self.ent.config(show='*')
        self.ent.pack(side= side_param if side_param else 'top')
        return(self.ent)
    def TechnicalEntry(self) -> tk.Entry:
        self.ent.pack()
        return(self.ent)