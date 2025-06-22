import tkinter as tk
from .widgets import MenuLabel, MenuEntry, MenuFrame, MenuButton, MenuCheck

class BaseForm:
    def __init__(self, parent, widgets, next_callback=None):
        self.parent = parent
        self.widgets = widgets
        self.widgets["next_callback"] = next_callback

    def build(self):
        raise NotImplementedError

class TechnicalForm(BaseForm):
    def build(self):
        MenuLabel = self.widgets['MenuLabel']
        MenuEntry = self.widgets['MenuEntry']
        MenuFrame = self.widgets['MenuFrame']
        MenuButton = self.widgets['MenuButton']

        MenuLabel(self.parent,'320x320 PNG IMAGE PATH:', '#f0f0f0').GenericLabel()
        img_path = MenuEntry(self.parent).TechnicalEntry()
        frm_grid = MenuFrame(self.parent).MainFrame(True)
        frm_a = MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'MANUFACTURER:', '#f0f0f0').GenericLabel()
        manufacturer = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'CREATION YEAR:', '#f0f0f0').GenericLabel()
        birth_year = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'MODEL:', '#f0f0f0').GenericLabel()
        model = MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'VARIATION:', '#f0f0f0').GenericLabel()
        variation = MenuEntry(frm_a).TechnicalEntry()
        frm_b = MenuFrame(frm_grid).GridFrame(0,1)
        MenuLabel(frm_b,'WINGSPAN IN METERS:', '#f0f0f0').GenericLabel()
        wingspan = MenuEntry(frm_b).TechnicalEntry()
        MenuLabel(frm_b,'WING POSITION:', '#f0f0f0').GenericLabel()
        wingposition = MenuEntry(frm_b).TechnicalEntry()
        MenuLabel(frm_b,'ENGINE POSITION:', '#f0f0f0').GenericLabel()
        engn_position = MenuEntry(frm_b).TechnicalEntry()
        MenuLabel(frm_b,'TAIL CONFIGURATION:', '#f0f0f0').GenericLabel()
        tail_config = MenuEntry(frm_b).TechnicalEntry()
        frm_c = MenuFrame(frm_grid).GridFrame(1,0)
        MenuLabel(frm_c,'LENGTH IN METERS:', '#f0f0f0').GenericLabel()
        length = MenuEntry(frm_c).TechnicalEntry()
        MenuLabel(frm_c,'HEIGHT IN METERS:', '#f0f0f0').GenericLabel()
        height = MenuEntry(frm_c).TechnicalEntry()
        frm_d = MenuFrame(frm_grid).GridFrame(1,1)
        MenuLabel(frm_d,'LANDING GEAR:', '#f0f0f0').GenericLabel()
        land_gear = MenuEntry(frm_d).TechnicalEntry()
        MenuLabel(frm_d,'SPECIFIC EU ANALYSIS:', '#f0f0f0').GenericLabel()
        eu_specific_analysis = MenuEntry(frm_d).TechnicalEntry()
        MenuButton(self.parent, 'NEXT', self.widgets['next_callback']).MainButton()
        return {
            'img_path': img_path,
            'manufacturer': manufacturer,
            'birth_year': birth_year,
            'model': model,
            'variation': variation,
            'wingspan': wingspan,
            'wingposition': wingposition,
            'engn_position': engn_position,
            'tail_config': tail_config,
            'length': length,
            'height': height,
            'land_gear': land_gear,
            'eu_specific_analysis': eu_specific_analysis
        }

class TakeoffForm(BaseForm):
    def build(self):
        MenuLabel=self.widgets['MenuLabel']
        MenuEntry=self.widgets['MenuEntry']
        MenuFrame=self.widgets['MenuFrame']
        MenuButton=self.widgets['MenuButton']
        frm_grid=MenuFrame(self.parent).MainFrame(True)
        frm_a=MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'MTOW IN KILOGRAMS:', '#f0f0f0').GenericLabel()
        mtow=MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'MINIMUM DISTANCE IN METERS:', '#f0f0f0').GenericLabel()
        to_distance=MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'V2 IN KNOTS:', '#f0f0f0').GenericLabel()
        v2=MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.parent,'NEXT',self.widgets['next_callback']).MainButton()
        return {'mtow':mtow,'to_distance':to_distance,'v2':v2}

class InitClimbForm(BaseForm):
    def build(self):
        MenuLabel=self.widgets['MenuLabel']
        MenuEntry=self.widgets['MenuEntry']
        MenuFrame=self.widgets['MenuFrame']
        MenuButton=self.widgets['MenuButton']
        frm_grid=MenuFrame(self.parent).MainFrame(True)
        frm_a=MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'IAS IN KNOTS:', '#f0f0f0').GenericLabel()
        inc_ias=MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'ROC IN FT/MIN:', '#f0f0f0').GenericLabel()
        inc_roc=MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.parent,'NEXT',self.widgets['next_callback']).MainButton()
        return {'inc_ias':inc_ias,'inc_roc':inc_roc}

class Climb150Form(BaseForm):
    def build(self):
        MenuLabel=self.widgets['MenuLabel']
        MenuEntry=self.widgets['MenuEntry']
        MenuFrame=self.widgets['MenuFrame']
        MenuCheck=self.widgets['MenuCheck']
        MenuButton=self.widgets['MenuButton']
        var=tk.BooleanVar(value=True)
        MenuCheck(self.parent,'HAS DATA?',var,self.widgets['next_callback']).MainButton()
        frm_grid=MenuFrame(self.parent).MainFrame(True)
        frm_a=MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'IAS IN KNOTS:', '#f0f0f0').GenericLabel()
        c150_ias=MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'ROC IN FT/MIN:', '#f0f0f0').GenericLabel()
        c150_roc=MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.parent,'NEXT',self.widgets['next_callback']).MainButton()
        return {'has_data':var,'c150_ias':c150_ias,'c150_roc':c150_roc}

class Climb240Form(BaseForm):
    def build(self):
        MenuLabel=self.widgets['MenuLabel']
        MenuEntry=self.widgets['MenuEntry']
        MenuFrame=self.widgets['MenuFrame']
        MenuCheck=self.widgets['MenuCheck']
        MenuButton=self.widgets['MenuButton']
        var=tk.BooleanVar(value=True)
        MenuCheck(self.parent,'HAS DATA?',var,self.widgets['next_callback']).MainButton()
        frm_grid=MenuFrame(self.parent).MainFrame(True)
        frm_a=MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'IAS IN KNOTS:', '#f0f0f0').GenericLabel()
        c240_ias=MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'ROC IN FT/MIN:', '#f0f0f0').GenericLabel()
        c240_roc=MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.parent,'NEXT',self.widgets['next_callback']).MainButton()
        return {'has_data':var,'c240_ias':c240_ias,'c240_roc':c240_roc}

class ClimbMachForm(BaseForm):
    def build(self):
        MenuLabel=self.widgets['MenuLabel']
        MenuEntry=self.widgets['MenuEntry']
        MenuFrame=self.widgets['MenuFrame']
        MenuCheck=self.widgets['MenuCheck']
        MenuButton=self.widgets['MenuButton']
        var=tk.BooleanVar(value=True)
        MenuCheck(self.parent,'HAS DATA?',var,self.widgets['next_callback']).MainButton()
        frm_grid=MenuFrame(self.parent).MainFrame(True)
        frm_a=MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'MACH SPEED:', '#f0f0f0').GenericLabel()
        cmach_ias=MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'ROC IN FT/MIN:', '#f0f0f0').GenericLabel()
        cmach_roc=MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.parent,'NEXT',self.widgets['next_callback']).MainButton()
        return {'has_data':var,'cmach_ias':cmach_ias,'cmach_roc':cmach_roc}

class CruiseForm(BaseForm):
    def build(self):
        MenuLabel=self.widgets['MenuLabel']
        MenuEntry=self.widgets['MenuEntry']
        MenuFrame=self.widgets['MenuFrame']
        MenuButton=self.widgets['MenuButton']
        frm_grid=MenuFrame(self.parent).MainFrame(True)
        frm_a=MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'TAS IN KNOTS:', '#f0f0f0').GenericLabel()
        tas=MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'MACH SPEED:', '#f0f0f0').GenericLabel()
        mach=MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'FLIGHT LEVEL CEILING:', '#f0f0f0').GenericLabel()
        ceiling=MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'RANGE IN NAUTICAL MILES:', '#f0f0f0').GenericLabel()
        range_entry=MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.parent,'NEXT',self.widgets['next_callback']).MainButton()
        return {'tas':tas,'mach':mach,'ceiling':ceiling,'range':range_entry}

class InitDescentForm(BaseForm):
    def build(self):
        MenuLabel=self.widgets['MenuLabel']
        MenuEntry=self.widgets['MenuEntry']
        MenuFrame=self.widgets['MenuFrame']
        MenuCheck=self.widgets['MenuCheck']
        MenuButton=self.widgets['MenuButton']
        var=tk.BooleanVar(value=True)
        MenuCheck(self.parent,'HAS DATA?',var,self.widgets['next_callback']).MainButton()
        frm_grid=MenuFrame(self.parent).MainFrame(True)
        frm_a=MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'MACH SPEED:', '#f0f0f0').GenericLabel()
        dmach_ias=MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'ROD IN FT/MIN:', '#f0f0f0').GenericLabel()
        dmach_rod=MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.parent,'NEXT',self.widgets['next_callback']).MainButton()
        return {'has_data':var,'dmach_ias':dmach_ias,'dmach_rod':dmach_rod}

class Descent100Form(BaseForm):
    def build(self):
        MenuLabel=self.widgets['MenuLabel']
        MenuEntry=self.widgets['MenuEntry']
        MenuFrame=self.widgets['MenuFrame']
        MenuButton=self.widgets['MenuButton']
        frm_grid=MenuFrame(self.parent).MainFrame(True)
        frm_a=MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'IAS IN KNOTS:', '#f0f0f0').GenericLabel()
        d100_ias=MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'ROD IN FT/MIN:', '#f0f0f0').GenericLabel()
        d100_rod=MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.parent,'NEXT',self.widgets['next_callback']).MainButton()
        return {'d100_ias':d100_ias,'d100_rod':d100_rod}

class ApproachForm(BaseForm):
    def build(self):
        MenuLabel=self.widgets['MenuLabel']
        MenuEntry=self.widgets['MenuEntry']
        MenuFrame=self.widgets['MenuFrame']
        MenuButton=self.widgets['MenuButton']
        frm_grid=MenuFrame(self.parent).MainFrame(True)
        frm_a=MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'IAS IN KNOTS:', '#f0f0f0').GenericLabel()
        appr_ias=MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'MCS IN KNOTS:', '#f0f0f0').GenericLabel()
        mcs=MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'ROD IN FT/MIN:', '#f0f0f0').GenericLabel()
        appr_rod=MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.parent,'NEXT',self.widgets['next_callback']).MainButton()
        return {'appr_ias':appr_ias,'mcs':mcs,'appr_rod':appr_rod}

class LandingForm(BaseForm):
    def build(self):
        MenuLabel=self.widgets['MenuLabel']
        MenuEntry=self.widgets['MenuEntry']
        MenuFrame=self.widgets['MenuFrame']
        MenuButton=self.widgets['MenuButton']
        frm_grid=MenuFrame(self.parent).MainFrame(True)
        frm_a=MenuFrame(frm_grid).GridFrame(0,0)
        MenuLabel(frm_a,'VAT IN KNOTS:', '#f0f0f0').GenericLabel()
        vat=MenuEntry(frm_a).TechnicalEntry()
        MenuLabel(frm_a,'MINIMUM DISTANCE IN METERS:', '#f0f0f0').GenericLabel()
        ld_distance=MenuEntry(frm_a).TechnicalEntry()
        MenuButton(self.parent,'NEXT',self.widgets['next_callback']).MainButton()
        return {'vat':vat,'ld_distance':ld_distance}
