import tkinter as tk
from widgets import *

class PlaneCreator:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title('Plane Creator')
        self.frm_main = MenuFrame(self.root).MainFrame(True)
        self.TechnicalCreator()

    def TechnicalCreator(self):
        self.frm_tec = MenuFrame(self.frm_main).MainFrame(True)
        frm_a = MenuFrame(self.frm_tec).GridFrame(0,0)
        MenuLabel(frm_a,'MANUFACTURER:', '#f0f0f0').GenericLabel()
        self.manufacturer = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'CREATION YEAR:', '#f0f0f0').GenericLabel()
        self.birth_year = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'MODEL:', '#f0f0f0').GenericLabel()
        self.model = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'VARIATION:', '#f0f0f0').GenericLabel()
        self.variation = MenuEntry(frm_a).TechnicalEntry()

        frm_b = MenuFrame(self.frm_tec).GridFrame(0,1)
        MenuLabel(frm_b,'WINGSPAN IN METERS:', '#f0f0f0').GenericLabel()
        self.wingspan = MenuEntry(frm_b).TechnicalEntry()
        MenuLabel(frm_b,'WING POSITION:', '#f0f0f0').GenericLabel()
        self.wingposition = MenuEntry(frm_b).TechnicalEntry()
        MenuLabel(frm_b,'ENGINE POSITION:', '#f0f0f0').GenericLabel()
        self.engn_position = MenuEntry(frm_b).TechnicalEntry()
        MenuLabel(frm_b,'TAIL CONFIGURATION:', '#f0f0f0').GenericLabel()
        self.tail_config = MenuEntry(frm_b).TechnicalEntry()

        frm_c = MenuFrame(self.frm_tec).GridFrame(1,0)
        MenuLabel(frm_c,'LENGTH IN METERS:', '#f0f0f0').GenericLabel()
        self.length = MenuEntry(frm_c).TechnicalEntry()
        MenuLabel(frm_c,'HEIGHT IN METERS:', '#f0f0f0').GenericLabel()
        self.height = MenuEntry(frm_c).TechnicalEntry()

        frm_d = MenuFrame(self.frm_tec).GridFrame(1,1)
        MenuLabel(frm_d,'LANDING GEAR:', '#f0f0f0').GenericLabel()
        self.land_gear = MenuEntry(frm_d).TechnicalEntry()
        MenuLabel(frm_d,'SPECIFIC EU ANALYSIS:', '#f0f0f0').GenericLabel()
        self.eu_specific_analysis = MenuEntry(frm_d).TechnicalEntry()
        MenuButton(self.frm_main, 'NEXT').MainButton()

window = tk.Tk()
PlaneCreator(window)
window.mainloop()