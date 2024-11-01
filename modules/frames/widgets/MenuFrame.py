import tkinter as tk

class MenuFrame:
    '''Preset Frame object.'''
    def __init__(self, master_param: tk.Frame):
        self.frm = tk.Frame(master=master_param, relief='solid')
    def GenericFrame(self) -> tk.Frame:
        self.frm.pack()
        return(self.frm)
    def MainFrame(self, fill_both_param: bool = False, anchor_center_param: bool = True) -> tk.Frame:
        self.frm.pack(expand=True, fill='both' if fill_both_param is True else 'none', anchor='center' if anchor_center_param is True else None)
        return(self.frm)
    def GridFrame(self, row_param: int = 0, column_param: int = 0):
        self.frm.config(bg= 'lightblue', borderwidth=1, width=60, height=60)
        self.frm.grid(row=row_param if row_param else 0, column=column_param if column_param else 0, sticky='nsew')
        return(self.frm)
    def AccountFrame(self) -> tk.Frame:
        self.frm.config(borderwidth=1)
        self.frm.place(relx=0.98, rely=0.05, anchor='e')
        return(self.frm)
    def ProfileFrame(self) -> tk.Frame:
        self.frm.config(bg='blue')
        self.frm.pack(padx=20, side='left', anchor='w')
        return(self.frm)
    def AvatarFrame(self) -> tk.Frame:
        self.frm.config(bg='darkgray', borderwidth=2)
        self.frm.pack()
        return(self.frm)
    def ProfileDescFrame(self) -> tk.Frame:
        self.frm.config(borderwidth=2)
        self.frm.pack(expand=True, fill='both')
        return(self.frm)