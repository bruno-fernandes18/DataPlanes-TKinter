import tkinter as tk

plane_objects = {
    'approach': ('ias', 'mcs', 'rod'),
    'climb150': ('ias', 'roc'),
    'climb240': ('ias', 'roc'),
    'climbmach': ('ias', 'roc'),
    'cruise': ('tas', 'mach', 'ceiling', 'range'),
    'descent100': ('ias', 'rod'),
    'initialclimb': ('ias', 'roc'),
    'initialdescent': ('ias', 'roc'),
    'landing': ('vat', 'distance'),
    'takeoff': ('mtow', 'distance', 'v2'),
    'technical': ('manufacturer', 'birth', 'model', 'variation', 'wingspan', 'wingposition', 'engineposition', 'tailconfiguration', 'landinggear', 'length', 'height')
}

class UpdateInputs:
    def __init__(self,root: tk.Tk, module: str, info_callback):
        self.master = root
        self.master.withdraw()
        self.root = tk.Toplevel(root)
        self.root.resizable(False,False)

        self.info_callback = info_callback
        
        self.frm_main = tk.Frame(self.root)
        self.frm_main.pack()

        self.module = module
        self.entries = {}

        for item in plane_objects[module]:
            frame = tk.Frame(self.frm_main, bg='black')
            frame.pack(pady=5)
            label = tk.Label(frame,text=item + ':', bg='darkgray', fg='white', width=40, borderwidth=2, relief='solid')
            label.pack(fill='x')
            entry = tk.Entry(frame, bg='lightgray', fg='black')
            entry.pack(pady=1,padx=2,fill='x')
            self.entries[item] = entry

        tk.Button(self.frm_main,text='SUBMIT',bg='yellow',fg='black', command=self.send_info).pack(pady=3)
    
    def information_to_tuple(self):
        info_tuple = tuple(information.get() for information in self.entries.values())
        return info_tuple
    
    def send_info(self):
        self.master.deiconify()
        self.info_callback(self.module,self.information_to_tuple())
        self.root.destroy()