import tkinter as tk
try:
    import winsound as ws
    winsound = True
except:
    winsound = False

class MenuButton:
    def __init__(self, master_param: tk.Frame, displayed_text: str, command_param = None) -> tk.Button:
        self.btn = tk.Button(master=master_param, text=displayed_text, command=command_param if command_param else None, relief='solid', width=15)
    def MainButton(self):
        self.btn.config(bg='yellow', font=('Courier', 18), borderwidth=2)
        self.btn.pack(padx=10, pady=6)
        return(self.btn)
    def AccountButton(self, side_param: str):
        self.btn.config(fg = 'darkblue', bg = 'cyan', font=('Helvetica', 9), borderwidth=1)
        self.btn.pack(side=side_param)
        return(self.btn)

class AccountMenu:
    def __init__(self, root: tk.Tk, sender ,on_close_callback):
        self.root= tk.Toplevel(root)
        self.root.geometry('720x405')

        self.sender = sender
        self.on_close_callback = on_close_callback

        self.root.protocol('WM_DELETE_WINDOW', self.on_close)

    def on_close(self):
        self.on_close_callback(self.sender)
        self.root.destroy()

    def login_tab(self, control_LR: bool):
        self.root.title('Login')

        self.frm_main = tk.Frame(master=self.root)
        self.frm_main. pack()

        self.frm_nickname = tk.Frame(master=self.frm_main)
        self.frm_nickname.pack()
        self.frm_password = tk.Frame(master=self.frm_main)
        self.frm_password.pack()

        self.lbl_nickname = tk.Label(master=self.frm_nickname, text='Name:', width=10).pack(side='left')
        self.lbl_password = tk.Label(master=self.frm_password, text='Password:', width=10).pack(side='left')

        self.ent_nickname = tk.Entry(master=self.frm_nickname)
        self.ent_nickname.pack(side='right')

        self.ent_password = tk.Entry(master=self.frm_password)
        self.ent_password.pack(side='right')

        if control_LR == True:
            self.btn_login = MenuButton(self.frm_main, 'Login', command_param=self.credentials).MainButton()
        else:
            self.btn_regis = MenuButton(self.frm_main, 'Register', command_param=self.credentials).MainButton()

    def credentials(self):
        print(self.ent_nickname.get())

class AircraftMenu:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.geometry('1280x720')
        frm_main = tk.Frame(master=self.root, bg='blue')
        frm_main.pack(expand=True, fill='both')

        self.img = tk.PhotoImage(file='img-debug.png')
        
        frm_profile = tk.Frame(master=frm_main, bg='darkgray', borderwidth=2, relief='solid')
        frm_profile.pack(pady=100, padx=20, anchor='w')

        lbl_image = tk.Label(master=frm_profile, image=self.img, borderwidth=0)
        lbl_image.pack()

        lbl_name = tk.Label(master=frm_profile, text='Debug Airplane', borderwidth=1, relief='solid', padx=5)
        lbl_name.pack(pady=5)

class MainMenu:
    def __init__(self,root: tk.Tk):
        self.root= root

        self.root.title('DataPlanes')
        self.root.geometry('1280x720')
        self.root.iconphoto(True,tk.PhotoImage(file='img-lg.png'))

        self.frm_account = tk.Frame(master=self.root, borderwidth=1, relief='solid')
        self.frm_account.place(relx=0.98, rely=0.05, anchor='e')

        self.lbl_account = tk.Label(master=self.frm_account,text='Not Logged!', width=31)
        self.lbl_account.pack()

        self.btn_login = MenuButton(self.frm_account, 'Login', command_param=self.open_login).AccountButton('right')
        self.btn_register = MenuButton(self.frm_account, 'Register', command_param=self.open_register).AccountButton('left')

        self.frm_main = tk.Frame(master=self.root)
        self.frm_main.pack(expand=True, anchor='center')
        
        self.btn_data = MenuButton(self.frm_main, 'Database', command_param=self.redirect).MainButton()
        self.btn_addplane = MenuButton(self.frm_main, 'Add Plane').MainButton()
        self.btn_manage = MenuButton(self.frm_main, 'Manage Plane').MainButton()
        self.btn_exit = MenuButton(self.frm_main, 'Exit', command_param=self.close).MainButton()

    def enable_button(self, receiver):
        receiver.config(state=tk.NORMAL)
    
    def redirect(self):
        self.frm_main.destroy()
        self.btn_debug = MenuButton(self.root, 'Debug', command_param=self.func_debug).MainButton()

    def func_debug(self):
        self.btn_debug.destroy()
        self.frm_account.destroy()
        MainMenu(self.root)

    def open_login(self):
        self.btn_login.config(state=tk.DISABLED)          
        AccountMenu(self.root, self.btn_login, self.enable_button).login_tab(True)

    def open_register(self):
        self.btn_register.config(state=tk.DISABLED)          
        AccountMenu(self.root, self.btn_register, self.enable_button).login_tab(False)

    def close(self):
        self.root.destroy()

if __name__ == '__main__':
    str_control = input('Select Class: ')
    if str_control == 'MainMenu':
        window = MainMenu(tk.Tk())
    elif str_control == 'Aircraft':
        window = AircraftMenu(tk.Tk())
    window.root.mainloop()