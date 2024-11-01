import tkinter as tk
from.accountmenu import AccountMenu
from .widgets import *

class MainMenu:
    def __init__(self,root: tk.Tk, user, plane_callback, creator_callback, manager_callback, register_callback, login_callback, logoff_callback):
        try:
            self.root = root
            self.root.title('DataPlanes')

            self.user = user if user else 'Not Logged!'

            self.plane_callback = plane_callback
            self.creator_callback = creator_callback
            self.manager_callback = manager_callback
            self.register_callback = register_callback
            self.login_callback = login_callback
            self.logoff_callback = logoff_callback

            self.frm_account = MenuFrame(self.root).AccountFrame()

            self.lbl_user = MenuLabel(self.frm_account, self.user).AccountLabel()

            self.btn_right = MenuButton(self.frm_account, 'Login', self.open_login).AccountButton('right') if self.user == 'Not Logged!' else MenuButton(self.frm_account, 'Logoff', self.do_logoff).LogoffButton()
            self.btn_left = MenuButton(self.frm_account, 'Register', self.open_register).AccountButton('left') if self.user == 'Not Logged!' else None

            self.frm_main = MenuFrame(self.root).MainFrame()
            
            self.btn_database = MenuButton(self.frm_main, 'Database', self.redirect_plane).MainButton()
            self.btn_creator = MenuButton(self.frm_main, 'Add Plane', self.open_creator).MainButton()
            self.btn_manager = MenuButton(self.frm_main, 'Manage Plane', self.open_manager).MainButton()
            self.btn_exit = MenuButton(self.frm_main, 'Exit', self.close).MainButton()
        except Exception as e:
            print(f'Error {e} when booting class Main Menu.')
    
    def close(self):
        self.root.destroy()
    def redirect_plane(self):
        if self.plane_callback() == True:
            self.default_redirect()
    def open_creator(self):
        self.creator_callback()
    def open_manager(self):
        self.manager_callback()
    def open_register(self):
        self.disable_buttons
        self.toplevel = AccountMenu(self.root, self.reenable_buttons, self.do_regis).open_tab(False)
    def open_login(self):
        self.disable_buttons
        AccountMenu(self.root, self.reenable_buttons, self.do_login).open_tab(True)
    def do_login(self,user: str, password: str):
        if self.login_callback(user,password) == True:
            self.user = user
        self.reset_buttons()
    def do_regis(self, user: str, password: str):
        if self.register_callback(user, password) == True:
            self.user = user
        self.reset_buttons()
    def do_logoff(self):
        self.user = 'Not Logged!'
        self.logoff_callback()
        self.reset_buttons()
        
    def reset_buttons(self):
        if self.lbl_user:
            self.lbl_user.destroy()
        if self.btn_right:
            self.btn_right.destroy()
        if self.btn_left:
            self.btn_left.destroy()
        
        self.lbl_user = MenuLabel(self.frm_account, self.user).AccountLabel()
        
        self.btn_right = MenuButton(self.frm_account, 'Login', self.open_login).AccountButton('right') if self.user == 'Not Logged!' else MenuButton(self.frm_account, 'Logoff', self.do_logoff).LogoffButton()
        self.btn_left = MenuButton(self.frm_account, 'Register', self.open_register).AccountButton('left') if self.user == 'Not Logged!' else None

    def disable_buttons(self):
        self.btn_database.config(state=tk.DISABLED)
        self.btn_creator.config(state=tk.DISABLED)
        self.btn_manager.config(state=tk.DISABLED)
        self.btn_exit.config(state=tk.DISABLED)
        self.btn_right.config(state=tk.DISABLED)
        self.btn_left.config(state=tk.DISABLED)
    def reenable_buttons(self):
        if self.btn_database:
            self.btn_database.config(state=tk.NORMAL)
        if self.btn_creator:
            self.btn_creator.config(state=tk.NORMAL)
        if self.btn_manager:
            self.btn_manager.config(state=tk.NORMAL)
        if self.btn_exit:
            self.btn_exit.config(state=tk.NORMAL)
        if self.btn_right:
            self.btn_right.config(state=tk.NORMAL)
        if self.btn_left:
            self.btn_left.config(state=tk.NORMAL)
    def default_redirect(self):
        self.frm_main.destroy()
        self.frm_account.destroy()