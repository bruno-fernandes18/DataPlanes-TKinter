class Technical:
    '''Technical object containing Manufacturer, Creation Year, Model, Variation, Wingspan, Wing Position, Engine Position, Tail Configuration, Landing Gear, Lenght, Height and EU Specif Analysis data.'''
    def __init__(self, manufacturer: str, birth_year: int, model: str, variation: str, wingspan: float, wingposition: str, engineposition: str, tailconfig: str, landinggear: str, length: float, height: float, eu_specific_analysis: str = None):
        '''Initializes Technical object.'''
        try:
            self.manufacturer: str = manufacturer
            self.birth_year: int = birth_year
            self.model: str = model
            self.variation: str = variation
            self.wingspan: float = round(wingspan, 2)
            self.wing_position: str = wingposition
            self.engn_position: str = engineposition
            self.tail_config: str = tailconfig
            self.land_gear: str = landinggear
            self.length: float = round(length, 2)
            self.height: float = round(height, 2)
            self.eu_specific_analysis: str = None if eu_specific_analysis == 'None' else eu_specific_analysis
        except Exception as e:
            print(f'Error {e} when booting Technical class.')