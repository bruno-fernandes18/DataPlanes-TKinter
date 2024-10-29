import tkinter as tk
try:
    import modules as m
except Exception as e:
    print(f'Error {e} when importing modules.')

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.default()
        self.window = m.MainMenu(self.root, self.open_airplane)
        self.root.mainloop()
    def default(self):
        self.root.geometry('1920x1080')
        self.root.state('zoomed')
        self.root.iconphoto(True, tk.PhotoImage(file='./images/img-lg.png'))
    def open_airplane(self):
        self.aircraft = m.Aircraft().debug_airplane()
        self.airplane = m.AircraftMenu(self.root, self.aircraft.plane_to_dict())

try:
    app = App()
    #aircraft = m.Aircraft().debug_airplane()
    #frame = m.AircraftMenu(root, aircraft.plane_to_dict())

except Exception as e:
    print(f'Error {e} when starting Main script.')
    input()