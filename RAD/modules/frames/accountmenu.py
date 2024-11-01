import tkinter as tk
from .widgets import *


class AccountMenu:
    def __init__(self, root: tk.Tk, on_close_callback, button_callback):     
        try:
            self.root= tk.Toplevel(root)
            self.root.geometry('720x405')

            self.on_close_callback = on_close_callback if on_close_callback else None
            self.button_callback = button_callback

            try:
                self.root.protocol('WM_DELETE_WINDOW', self.on_close)
            except Exception as e:
                print(f'Error {e} while setting window deletion protocol.')
        
        except Exception as e: ## Make Tkinter MessasgeBox
            print(f'Error {e} when booting class Account Menu.')

    def open_tab(self, control_LR: bool = True):
        try:
            frm_main = MenuFrame(self.root).GenericFrame()

            frm_nickname = MenuFrame(frm_main).GenericFrame()
            frm_password = MenuFrame(frm_main).GenericFrame()

            MenuLabel(frm_nickname,'Name:').LoginLabel('left')
            MenuLabel(frm_password,'Password:').LoginLabel('left')

            self.ent_nickname = MenuEntry(frm_nickname).LoginEntry('right', True)
            self.ent_password = MenuEntry(frm_password).LoginEntry('right', False)

            if control_LR == True:
                self.root.title('Login')
                MenuButton(frm_main, 'Login', command_param=self.login).MainButton()
            else:
                self.root.title('Register')
                MenuButton(frm_main, 'Register', command_param=self.register).MainButton()
        except Exception as e:
            print(f'Error {e} when booting Login Tab function.')

    def login(self):
        self.button_callback(self.ent_nickname.get(), self.ent_password.get())
        self.on_close()
    def register(self):
        self.button_callback(self.ent_nickname.get(), self.ent_password.get())
        self.on_close()
    
    def on_close(self):
        try:
            self.on_close_callback()
        except Exception as e:
            print(f'Error {e} when emitting close signal.')
        self.root.destroy()