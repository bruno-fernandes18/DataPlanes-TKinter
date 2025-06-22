import tkinter as tk
from tkinter import messagebox
from .widgets import *
from .forms import TechnicalForm, TakeoffForm, InitClimbForm, Climb150Form, Climb240Form, ClimbMachForm, CruiseForm, InitDescentForm, Descent100Form, ApproachForm, LandingForm
from ..helpers import validate_image, duplicate_image, validate_parts
from ..builder import AircraftBuilder

class PlaneCreator:
    def __init__(self, root: tk.Tk, username: str, on_close_callback):
        self.root = tk.Toplevel(root)
        self.root.title('Plane Creator')
        self.root.resizable(False, False)
        self.user = username
        self.plne = None

        self.on_close_callback = on_close_callback
        self.root.protocol('WM_DELETE_WINDOW', self.on_close)

        self.builder = AircraftBuilder()
        self.frm_main = MenuFrame(self.root).MainFrame(True)
        self.show_technical()

    def show_technical(self):
        self.default_init('TECHNICAL')
        widgets = {
            'MenuLabel': MenuLabel,
            'MenuEntry': MenuEntry,
            'MenuFrame': MenuFrame,
            'MenuButton': MenuButton,
            'next_callback': self.goto_takeoff
        }
        fields = TechnicalForm(self.frm_creator, widgets).build()
        self.img_path = fields['img_path']
        self.manufacturer = fields['manufacturer']
        self.birth_year = fields['birth_year']
        self.model = fields['model']
        self.variation = fields['variation']
        self.wingspan = fields['wingspan']
        self.wingposition = fields['wingposition']
        self.engn_position = fields['engn_position']
        self.tail_config = fields['tail_config']
        self.length = fields['length']
        self.height = fields['height']
        self.land_gear = fields['land_gear']
        self.eu_specific_analysis = fields['eu_specific_analysis']
    
    def show_takeoff(self):
        self.default_init('TAKE OFF')
        widgets = {
            'MenuLabel': MenuLabel,
            'MenuEntry': MenuEntry,
            'MenuFrame': MenuFrame,
            'MenuButton': MenuButton,
            'next_callback': self.goto_init_climb
        }
        fields = TakeoffForm(self.frm_creator, widgets).build()
        self.mtow = fields['mtow']
        self.to_distance = fields['to_distance']
        self.v2 = fields['v2']
    
    def show_init_climb(self):
        self.default_init('INITIAL CLIMB')
        widgets = {
            'MenuLabel': MenuLabel,
            'MenuEntry': MenuEntry,
            'MenuFrame': MenuFrame,
            'MenuButton': MenuButton,
            'next_callback': self.goto_150_climb
        }
        fields = InitClimbForm(self.frm_creator, widgets).build()
        self.inc_ias = fields['inc_ias']
        self.inc_roc = fields['inc_roc']

    def show_climb_150(self):
        self.default_init('CLIMB TO FL 150')
        widgets = {
            'MenuLabel': MenuLabel,
            'MenuEntry': MenuEntry,
            'MenuFrame': MenuFrame,
            'MenuButton': MenuButton,
            'MenuCheck': MenuCheck,
            'next_callback': self.goto_240_climb
        }
        fields = Climb150Form(self.frm_creator, widgets).build()
        self.has_150_data = fields['has_data']
        self.c150_ias = fields['c150_ias']
        self.c150_roc = fields['c150_roc']

    def show_climb_240(self):
        self.default_init('CLIMB TO FL 240')
        widgets = {
            'MenuLabel': MenuLabel,
            'MenuEntry': MenuEntry,
            'MenuFrame': MenuFrame,
            'MenuButton': MenuButton,
            'MenuCheck': MenuCheck,
            'next_callback': self.goto_mach_climb
        }
        fields = Climb240Form(self.frm_creator, widgets).build()
        self.has_240_data = fields['has_data']
        self.c240_ias = fields['c240_ias']
        self.c240_roc = fields['c240_roc']

    def show_climb_mach(self):
        self.default_init('MACH CLIMB')
        widgets = {
            'MenuLabel': MenuLabel,
            'MenuEntry': MenuEntry,
            'MenuFrame': MenuFrame,
            'MenuButton': MenuButton,
            'MenuCheck': MenuCheck,
            'next_callback': self.goto_cruise
        }
        fields = ClimbMachForm(self.frm_creator, widgets).build()
        self.has_cmach_data = fields['has_data']
        self.cmach_ias = fields['cmach_ias']
        self.cmach_roc = fields['cmach_roc']

    def show_cruise(self):
        self.default_init('CRUISE')
        widgets = {
            'MenuLabel': MenuLabel,
            'MenuEntry': MenuEntry,
            'MenuFrame': MenuFrame,
            'MenuButton': MenuButton,
            'next_callback': self.goto_init_dsct
        }
        fields = CruiseForm(self.frm_creator, widgets).build()
        self.tas = fields['tas']
        self.mach = fields['mach']
        self.ceiling = fields['ceiling']
        self.range = fields['range']

    def show_init_descent(self):
        self.default_init('INITIAL DESCENT')
        widgets = {
            'MenuLabel': MenuLabel,
            'MenuEntry': MenuEntry,
            'MenuFrame': MenuFrame,
            'MenuButton': MenuButton,
            'MenuCheck': MenuCheck,
            'next_callback': self.goto_100_dsct
        }
        fields = InitDescentForm(self.frm_creator, widgets).build()
        self.has_dmach_data = fields['has_data']
        self.dmach_ias = fields['dmach_ias']
        self.dmach_rod = fields['dmach_rod']

    def show_descent_100(self):
        self.default_init('DESCENT TO FL 100')
        widgets = {
            'MenuLabel': MenuLabel,
            'MenuEntry': MenuEntry,
            'MenuFrame': MenuFrame,
            'MenuButton': MenuButton,
            'next_callback': self.goto_approach
        }
        fields = Descent100Form(self.frm_creator, widgets).build()
        self.d100_ias = fields['d100_ias']
        self.d100_rod = fields['d100_rod']

    def show_approach(self):
        self.default_init('APPROACH')
        widgets = {
            'MenuLabel': MenuLabel,
            'MenuEntry': MenuEntry,
            'MenuFrame': MenuFrame,
            'MenuButton': MenuButton,
            'next_callback': self.goto_landing
        }
        fields = ApproachForm(self.frm_creator, widgets).build()
        self.appr_ias = fields['appr_ias']
        self.mcs = fields['mcs']
        self.appr_rod = fields['appr_rod']

    def show_landing(self):
        self.default_init('LANDING')
        widgets = {
            'MenuLabel': MenuLabel,
            'MenuEntry': MenuEntry,
            'MenuFrame': MenuFrame,
            'MenuButton': MenuButton,
            'next_callback': self.create_plane
        }
        fields = LandingForm(self.frm_creator, widgets).build()
        self.vat = fields['vat']
        self.ld_distance = fields['ld_distance']
        
    def goto_takeoff(self):
        self.frm_creator.pack_forget()
        if validate_image(self.img_path.get()):
            self.show_takeoff()

    def goto_init_climb(self):
        self.frm_creator.pack_forget()
        self.show_init_climb()

    def goto_150_climb(self):
        self.frm_creator.pack_forget()
        self.show_climb_150()

    def goto_240_climb(self):
        if self.has_150_data.get() == False:
            self.c150_ias = None
            self.c150_roc = None
        self.frm_creator.pack_forget()
        self.show_climb_240()

    def goto_mach_climb(self):
        if self.has_240_data.get() == False:
            self.c240_ias = None
            self.c240_roc = None
        self.frm_creator.pack_forget()
        self.show_climb_mach()

    def goto_cruise(self):
        if self.has_cmach_data.get() == False:
            self.cmach_ias = None
            self.cmach_roc = None
        self.frm_creator.pack_forget()
        self.show_cruise()

    def goto_init_dsct(self):
        self.frm_creator.pack_forget()
        self.show_init_descent()

    def goto_100_dsct(self):
        if self.has_dmach_data.get() == False:
            self.dmach_ias = None
            self.dmach_rod = None
        self.frm_creator.pack_forget()
        self.show_descent_100()

    def goto_approach(self):
        self.frm_creator.pack_forget()
        self.show_approach()

    def goto_landing(self):
        self.frm_creator.pack_forget()
        self.show_landing()
    
    def create_plane(self):
        dest = './images/' + str(self.model.get()) + '-' + str(self.variation.get()) + '.png'
        if duplicate_image(self.img_path.get(), dest):
            if self.validate_parts():
                try:
                    aircraft = self.info_to_dictionary()
                    messagebox.showinfo('Sucess!', 'Plane has been successfully created!')
                    self.plne = aircraft
                    self.on_close()
                except Exception as e:
                    messagebox.showerror('Error', e)
            else:
                self.on_close()
                self.root.destroy()

    def validate_parts(self) -> bool:
        information = (self.manufacturer, self.birth_year, self.model, self.variation, self.wingspan, self.wingposition, self.engn_position, self.tail_config, self.length, self.height, self.land_gear, self.eu_specific_analysis, self.mtow, self.to_distance, self.v2, self.inc_ias, self.inc_roc, self.tas, self.mach, self.ceiling, self.range, self.d100_ias, self.d100_rod, self.appr_ias, self.mcs, self.appr_rod, self.vat, self.ld_distance)
        optional = {0: (self.has_150_data.get(), self.c150_ias, self.c150_roc), 1: (self.has_240_data.get(), self.c240_ias, self.c240_roc), 2: (self.has_cmach_data.get(), self.cmach_ias, self.cmach_roc), 3: (self.has_dmach_data.get(), self.dmach_ias, self.dmach_rod)}
        str_information = (self.manufacturer, self.model, self.variation, self.wingposition, self.engn_position, self.tail_config, self.land_gear, self.eu_specific_analysis)
        int_information = (self.birth_year, self.mtow, self.to_distance, self.v2, self.inc_ias, self.inc_roc, self.tas, self.ceiling, self.range, self.d100_ias, self.d100_rod, self.appr_ias, self.mcs, self.appr_rod, self.vat, self.ld_distance)
        flt_information = (self.wingspan, self.length, self.height, self.mach)
        return validate_parts(information, optional, str_information, int_information, flt_information)
            
    def info_to_dictionary(self) -> dict:
        try:
            builder = AircraftBuilder()
            builder.set('creator', str(self.user))
            builder.set('image', './images/' + str(self.model.get()) + '-' + str(self.variation.get()) + '.png')
            builder.set('manufacturer', str(self.manufacturer.get()).strip())
            builder.set('birth_year', int(self.birth_year.get()))
            builder.set('model', str(self.model.get()).strip())
            builder.set('wingspan', round(float(self.wingspan.get()),1))
            builder.set('length', round(float(self.length.get()),1))
            builder.set('height', round(float(self.height.get()),1))
            builder.set('eu_analysis', str(self.eu_specific_analysis.get()).strip())
            builder.set('mtow', int(self.mtow.get()))
            builder.set('to_distance', int(self.to_distance.get()))
            builder.set('v2', int(self.v2.get()))
            builder.set('ic_ias', int(self.inc_ias.get()))
            builder.set('ic_roc', int(self.inc_roc.get()))
            builder.set('150_hd', bool(self.has_150_data.get()))
            builder.set('150_ias', int(self.c150_ias.get()) if self.c150_ias else None)
            builder.set('150_roc', int(self.c150_roc.get()) if self.c150_roc else None)
            builder.set('240_hd', bool(self.has_240_data.get()))
            builder.set('240_ias', int(self.c240_ias.get()) if self.c240_ias else None)
            builder.set('240_roc', int(self.c240_roc.get()) if self.c240_roc else None)
            builder.set('machc_hd', bool(self.has_cmach_data.get()))
            builder.set('machc_ias', round(float(self.cmach_ias.get()),1) if self.cmach_ias else None)
            builder.set('machc_roc', int(self.cmach_roc.get()) if self.cmach_roc else None)
            builder.set('tas', int(self.tas.get()))
            builder.set('mach_cruise', round(float(self.mach.get()),1))
            builder.set('ceiling', int(self.ceiling.get()))
            builder.set('range', int(self.range.get()))
            builder.set('machd_hd', bool(self.has_dmach_data.get()))
            builder.set('machd_ias', round(float(self.dmach_ias.get()),1) if self.dmach_ias else None)
            builder.set('machd_rod', int(self.dmach_rod.get()) if self.dmach_rod else None)
            builder.set('100_ias', int(self.d100_ias.get()))
            builder.set('100_rod', int(self.d100_rod.get()))
            builder.set('approach_ias', int(self.appr_ias.get()))
            builder.set('mcs', int(self.mcs.get()))
            builder.set('approach_rod', int(self.appr_rod.get()))
            builder.set('vat', int(self.vat.get()))
            builder.set('ld_distance', int(self.ld_distance.get()))
            builder.set('variation', str(self.variation.get()).strip())
            builder.set('wing_position', str(self.wingposition.get()).strip())
            builder.set('engine_position', str(self.engn_position.get()).strip())
            builder.set('tail_configuration', str(self.tail_config.get()).strip())
            builder.set('landing_gear', str(self.land_gear.get()).strip())
            return builder.build()
        except Exception as e:
            print(f'Error {e} when converting Aircraft object to dictionary.')


    def default_init(self, section: str):
        self.frm_creator = MenuFrame(self.frm_main).MainFrame(True)
        MenuLabel(self.frm_creator, section, 'darkblue', 'white').GenericLabel()

    def on_close(self):
        self.on_close_callback()
        self.root.destroy()
