import tkinter as tk

class MenuCheck:
    '''Preset Check Button object.'''
    def __init__(self, master_param: tk.Frame, displayed_text: str = '', variable_param = None, command_param = None):
        self.btn = tk.Checkbutton(master=master_param, text=displayed_text if displayed_text else '', variable=variable_param if variable_param else None, command=command_param if command_param else None, relief='solid', width=15)
    def MainButton(self) -> tk.Button:
        self.btn.config(bg='red', font=('Verdana', 12), borderwidth=2)
        self.btn.pack(padx=10, pady=4)
        return(self.btn)