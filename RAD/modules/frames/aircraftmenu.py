import tkinter as tk
from .widgets import *

class AircraftMenu:
    def __init__(self, root: tk.Tk = None, aircraft: dict = None, similar_planes: tuple = ('','','','','')):
        try:
            self.root = root
            self.strvar_plane = tk.StringVar()
            self.img = tk.PhotoImage(file=aircraft['image']) if aircraft['image'] else tk.PhotoImage(file='./images/img-debug.png')
        except Exception as e:
            print(f'Error {e} when booting class Airplane Menu.')

        frm_main = MenuFrame(self.root).MainFrame(True, False)
        
        frm_profile = MenuFrame(frm_main).ProfileFrame()

        frm_upper_profile = MenuFrame(frm_profile).AvatarFrame()
        MenuLabel(frm_upper_profile).ImageLabel(self.img)
        MenuComboBox(frm_upper_profile, self.strvar_plane, ('debug')).NameComboBox().current(0)

        frm_lower_profile = MenuFrame(frm_profile).MainFrame(True)
        
        frm_identity = MenuFrame(frm_lower_profile).ProfileDescFrame()
        self.lbl_manufacturer = MenuLabel(frm_identity, f'Manufacturer: {aircraft['manufacturer']}', 'darkgray').GenericLabel()
        self.lbl_year = MenuLabel(frm_identity, f'Made in {aircraft['birth_year']}', 'lightgray').GenericLabel()
        self.lbl_model = MenuLabel(frm_identity, f'Model: {aircraft['model']}', 'darkgray').GenericLabel()

        frm_technical = MenuFrame(frm_lower_profile).ProfileDescFrame()
        self.lbl_wingspan = MenuLabel(frm_technical, f'Wingspan: {aircraft['wingspan']}m', 'lightgray').GenericLabel()
        self.lbl_lenght = MenuLabel(frm_technical, f'Length: {aircraft['length']}m', 'darkgray').GenericLabel()
        self.lbl_height = MenuLabel(frm_technical, f'Height: {aircraft['height']}m', 'lightgray').GenericLabel()

        frm_category = MenuFrame(frm_technical).ProfileDescFrame()
        self.lbl_recat_eu_p = MenuLabel(frm_category, f'RECAT-EU: "{aircraft['recat_eu']}"', 'darkgray').CategoryLabel('right')
        self.lbl_wtc_p = MenuLabel(frm_category, f'WTC: "{aircraft['wtc']}"', 'darkgray').CategoryLabel('left')

        frm_informations = MenuFrame(frm_main).MainFrame()

        frm_takeoff = MenuFrame(frm_informations).GridFrame(0,0)
        MenuLabel(frm_takeoff, 'Take Off').GenericLabel()
        self.lbl_mtow = MenuLabel(frm_takeoff, f'MTOW: {aircraft['mtow']}kg').GenericLabel()
        self.lbl_to_wtc = MenuLabel(frm_takeoff, f'WTC: "{aircraft['wtc']}"').GenericLabel()
        self.lbl_to_recat_eu = MenuLabel(frm_takeoff, f'RECAT-EU: "{aircraft['recat_eu']}"').GenericLabel()
        self.lbl_to_distance = MenuLabel(frm_takeoff, f'Distance: {aircraft['to_distance']}m').GenericLabel()
        self.lbl_v2 = MenuLabel(frm_takeoff, f'V2: {aircraft['v2']}kt').GenericLabel()

        frm_initial_climb = MenuFrame(frm_informations).GridFrame(1,0)
        MenuLabel(frm_initial_climb, 'Initial Climb (to 5.000ft)').GenericLabel()
        self.lbl_ic_ias = MenuLabel(frm_initial_climb, f'IAS: {aircraft['ic_ias']}kt').GenericLabel()
        self.lbl_ic_roc = MenuLabel(frm_initial_climb, f'ROC: {aircraft['ic_roc']}ft/min').GenericLabel()
        MenuLabel(frm_initial_climb, '').GenericLabel()
        MenuLabel(frm_initial_climb, '').GenericLabel()
        MenuLabel(frm_initial_climb, '').GenericLabel()

        frm_150FL_climb = MenuFrame(frm_informations).GridFrame(2,0)
        MenuLabel(frm_150FL_climb, 'FL 150 Climb').GenericLabel()
        self.lbl_150FLc_ias = MenuLabel(frm_150FL_climb, f'IAS: {aircraft['150_ias']}kt').GenericLabel()
        self.lbl_150FLc_roc = MenuLabel(frm_150FL_climb, f'ROC: {aircraft['150_roc']}ft/min').GenericLabel()
        MenuLabel(frm_150FL_climb, '').GenericLabel()
        MenuLabel(frm_150FL_climb, '').GenericLabel()
        MenuLabel(frm_150FL_climb, '').GenericLabel()

        frm_240FL_climb = MenuFrame(frm_informations).GridFrame(0,1)
        MenuLabel(frm_240FL_climb, 'FL 240 Climb').GenericLabel()
        self.lbl_240FLc_ias = MenuLabel(frm_240FL_climb, f'IAS: {aircraft['240_ias']}kt').GenericLabel()
        self.lbl_240FLc_roc = MenuLabel(frm_240FL_climb, f'ROC: {aircraft['240_roc']}ft/min').GenericLabel()
        MenuLabel(frm_240FL_climb, '').GenericLabel()
        MenuLabel(frm_240FL_climb, '').GenericLabel()
        MenuLabel(frm_240FL_climb, '').GenericLabel()

        frm_mach_climb = MenuFrame(frm_informations).GridFrame(1,1)
        MenuLabel(frm_mach_climb, 'MACH Climb').GenericLabel()
        self.lbl_machc_ias = MenuLabel(frm_mach_climb, f'MACH: {aircraft['machc_ias']}').GenericLabel()
        self.lbl_machc_roc = MenuLabel(frm_mach_climb, f'ROC: {aircraft['machc_roc']}ft/min').GenericLabel()
        MenuLabel(frm_mach_climb, '').GenericLabel()
        MenuLabel(frm_mach_climb, '').GenericLabel()
        MenuLabel(frm_mach_climb, '').GenericLabel()

        frm_cruise = MenuFrame(frm_informations).GridFrame(2,1)
        MenuLabel(frm_cruise, 'Cruise').GenericLabel()
        self.lbl_tas = MenuLabel(frm_cruise, f'TAS: {aircraft['tas']}kt').GenericLabel()
        self.lbl_mach_cruise = MenuLabel(frm_cruise, f'MACH: {aircraft['mach_cruise']}').GenericLabel()
        self.lbl_ceiling = MenuLabel(frm_cruise, f'Ceiling: {aircraft['ceiling']}FL').GenericLabel()
        self.lbl_range = MenuLabel(frm_cruise, f'Range: {aircraft['range']}NM').GenericLabel()
        MenuLabel(frm_cruise, '').GenericLabel()

        frm_initial_descent = MenuFrame(frm_informations).GridFrame(0,2)
        MenuLabel(frm_initial_descent, 'Initial Descent (to FL 240)').GenericLabel()
        self.lbl_id_ias = MenuLabel(frm_initial_descent, f'MACH: {aircraft['machd_ias']}kt').GenericLabel()
        self.lbl_id_rod = MenuLabel(frm_initial_descent, f'ROD: {aircraft['machd_rod']}ft/min').GenericLabel()
        MenuLabel(frm_initial_descent, '').GenericLabel()
        MenuLabel(frm_initial_descent, '').GenericLabel()
        MenuLabel(frm_initial_descent, '').GenericLabel()

        frm_100FL_descent = MenuFrame(frm_informations).GridFrame(1,2)
        MenuLabel(frm_100FL_descent, 'FL 100 Descent').GenericLabel()
        self.lbl_100FLd_ias = MenuLabel(frm_100FL_descent, f'IAS: {aircraft['100_ias']}kt').GenericLabel()
        self.lbl_100FLd_rod = MenuLabel(frm_100FL_descent, f'ROD: {aircraft['100_rod']}ft/min').GenericLabel()
        MenuLabel(frm_100FL_descent, '').GenericLabel()
        MenuLabel(frm_100FL_descent, '').GenericLabel()
        MenuLabel(frm_100FL_descent, '').GenericLabel()

        frm_approach = MenuFrame(frm_informations).GridFrame(2,2)
        MenuLabel(frm_approach, 'Approach').GenericLabel()
        self.lbl_approach_ias = MenuLabel(frm_approach, f'IAS: {aircraft['approach_ias']}kt').GenericLabel()
        self.lbl_approach_mcs = MenuLabel(frm_approach, f'MCS: {aircraft['mcs']}kt').GenericLabel()
        self.lbl_approach_rod = MenuLabel(frm_approach, f'ROD: {aircraft['approach_rod']}ft/min').GenericLabel()
        MenuLabel(frm_approach, '').GenericLabel()
        MenuLabel(frm_approach, '').GenericLabel()

        frm_landing = MenuFrame(frm_informations).GridFrame(0,3)
        MenuLabel(frm_landing, 'Landing').GenericLabel()
        self.lbl_vat = MenuLabel(frm_landing, f'VAT: {aircraft['vat']}kt').GenericLabel()
        self.lbl_apc = MenuLabel(frm_landing, f'APC: "{aircraft['apc']}"').GenericLabel()
        self.lbl_ld_distance = MenuLabel(frm_landing, f'Distance: {aircraft['ld_distance']}m').GenericLabel()
        MenuLabel(frm_landing, '').GenericLabel()
        MenuLabel(frm_landing, '').GenericLabel()

        frm_recognition = MenuFrame(frm_informations).GridFrame(1,3)
        MenuLabel(frm_recognition, 'Recognition').GenericLabel()
        self.lbl_variation = MenuLabel(frm_recognition, f'Variation: {aircraft['variation']}').GenericLabel()
        self.lbl_wing_position = MenuLabel(frm_recognition, f'Wing Position: {aircraft['wing_position']}').GenericLabel()
        self.lbl_engn_position = MenuLabel(frm_recognition, f'Engine Position: {aircraft['engine_position']}').GenericLabel()
        self.lbl_tail_config = MenuLabel(frm_recognition, f'Tail Configuration: {aircraft['tail_configuration']}').GenericLabel()
        self.lbl_land_gear = MenuLabel(frm_recognition, f'Landing Gear: {aircraft['landing_gear']}').GenericLabel()

        frm_similar = MenuFrame(frm_informations).GridFrame(2,3)
        MenuLabel(frm_similar, 'Similar Aircrafts').GenericLabel()
        for plane in similar_planes:
            MenuLabel(frm_similar, plane).GenericLabel()