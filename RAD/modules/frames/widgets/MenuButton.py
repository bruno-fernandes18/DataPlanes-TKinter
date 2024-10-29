import tkinter as tk

class MenuButton:
    def __init__(self, master_param: tk.Frame, displayed_text: str = '', command_param = None):
        self.btn = tk.Button(master=master_param, text=displayed_text if displayed_text else '', command=command_param if command_param else None, relief='solid', width=15)
    def MainButton(self) -> tk.Button:
        self.btn.config(bg='yellow', font=('Courier', 18), borderwidth=2)
        self.btn.pack(padx=10, pady=6)
        return(self.btn)
    def AccountButton(self, side_param: str = 'top') -> tk.Button:
        self.btn.config(fg = 'darkblue', bg = 'cyan', font=('Helvetica', 9), borderwidth=1)
        self.btn.pack(side=side_param if side_param else 'top')
        return(self.btn)