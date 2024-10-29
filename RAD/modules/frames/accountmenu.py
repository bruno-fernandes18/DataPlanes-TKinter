import tkinter as tk
from .widgets import *


class AccountMenu:
    def __init__(self, root: tk.Tk = None, sender = None, on_close_callback = None):
        try:
            if root == None:
                self.root = tk.Tk()
            else:
                self.root= tk.Toplevel(root)
        except Exception as e:
            print(f'Error {e} on Account Menu class root definition.')
       
        try:
            self.root.geometry('720x405')

            self.sender = sender if sender else None
            self.on_close_callback = on_close_callback if on_close_callback else None

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
                MenuButton(frm_main, 'Login', command_param=self.credentials).MainButton()
            else:
                self.root.title('Register')
                MenuButton(frm_main, 'Register', command_param=self.credentials).MainButton()
        except Exception as e:
            print(f'Error {e} when booting Login Tab function.')

    def on_close(self):
        if self.sender:
            if self.on_close_callback:
                try:
                    self.on_close_callback(self.sender)
                except Exception as e:
                    print(f'Error {e} when emitting close signal.')
        self.root.destroy()

    def credentials(self):
        print(self.ent_nickname.get(), self.ent_password.get())