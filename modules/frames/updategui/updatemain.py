import tkinter as tk
from .updateinput import UpdateInputs

class UpdateMain:
    def __init__(self, root: tk.Tk, id: int, on_submit_callback) -> None:
        self.root = tk.Toplevel(root)
        self.root.title('UpdateGUI')
        self.root.resizable(False,False)

        self.aircraft_dict = {}
        self.id = id
        self.on_submit_callback = on_submit_callback

        self.frm_main = tk.Frame(self.root)
        self.frm_main.pack()
        
        self.btn_tch = tk.Button(self.frm_main,bg='yellow',text='Technical',width=20, height=8, command=self.open_tch)
        self.btn_tch.grid(row=0,column=0)

        self.btn_tko = tk.Button(self.frm_main,bg='yellow',text='Take Off',width=20, height=8, command=self.open_tko)
        self.btn_tko.grid(row=1,column=0)

        self.btn_inc = tk.Button(self.frm_main,bg='yellow',text='Initial Climb',width=20, height=8, command=self.open_inc)
        self.btn_inc.grid(row=2,column=0)

        self.btn_15c = tk.Button(self.frm_main,bg='yellow',text='FL 150 Climb',width=20, height=8, command=self.open_15c)
        self.btn_15c.grid(row=0,column=1)

        self.btn_24c = tk.Button(self.frm_main,bg='yellow',text='FL 240 Climb',width=20, height=8, command=self.open_24c)
        self.btn_24c.grid(row=1,column=1)

        self.btn_mhc = tk.Button(self.frm_main,bg='yellow',text='MACH Climb',width=20, height=8, command=self.open_mhc)
        self.btn_mhc.grid(row=2,column=1)

        self.btn_cru = tk.Button(self.frm_main,bg='yellow',text='Cruise',width=20, height=8, command=self.open_cru)
        self.btn_cru.grid(row=0,column=2)

        self.btn_ind = tk.Button(self.frm_main,bg='yellow',text='Initial Descent',width=20, height=8, command=self.open_ind)
        self.btn_ind.grid(row=1,column=2)

        self.btn_10d = tk.Button(self.frm_main,bg='yellow',text='FL 100 Descent',width=20, height=8, command=self.open_10d)
        self.btn_10d.grid(row=2,column=2)

        self.btn_apr = tk.Button(self.frm_main,bg='yellow',text='Approach',width=20, height=8, command=self.open_apr)
        self.btn_apr.grid(row=0,column=3)

        self.btn_lan = tk.Button(self.frm_main,bg='yellow',text='Landing',width=20, height=8, command=self.open_lan)
        self.btn_lan.grid(row=1,column=3)

        self.btn_sbm = tk.Button(self.frm_main,bg='black',fg='white',text='OK',width=20, height=8, command=self.submit)
        self.btn_sbm.grid(row=2,column=3)

    def tuple_receiver(self, module: str, info_tuple: tuple):
        self.aircraft_dict[module] = info_tuple
    def open_tch(self):
        UpdateInputs(self.root,'technical',self.tuple_receiver)
    def open_tko(self):
        UpdateInputs(self.root, 'takeoff', self.tuple_receiver)
    def open_inc(self):
        UpdateInputs(self.root, 'initialclimb', self.tuple_receiver)
    def open_15c(self):
        UpdateInputs(self.root, 'climb150', self.tuple_receiver)
    def open_24c(self):
        UpdateInputs(self.root, 'climb240', self.tuple_receiver)
    def open_mhc(self):
        UpdateInputs(self.root, 'climbmach', self.tuple_receiver)
    def open_cru(self):
        UpdateInputs(self.root, 'cruise', self.tuple_receiver)
    def open_ind(self):
        UpdateInputs(self.root, 'initialdescent', self.tuple_receiver)
    def open_10d(self):
        UpdateInputs(self.root, 'descent100', self.tuple_receiver)
    def open_apr(self):
        UpdateInputs(self.root, 'approach', self.tuple_receiver)
    def open_lan(self):
        UpdateInputs(self.root, 'landing', self.tuple_receiver)
    
    def submit(self):
        self.on_submit_callback(self.id,self.aircraft_dict)
        self.root.destroy()