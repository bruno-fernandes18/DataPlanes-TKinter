class Technical:
    def __init__(self, manufacturer: str, birth_year: int, model: str, variation: str, wingspan: float, wingposition: str, engineposition: str, tailconfig: str, landinggear: str, length: float, height: float, eu_specific_analysis: str = None):
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
            self.eu_specific_analysis: str = eu_specific_analysis if eu_specific_analysis else None
        except Exception as e:
            print(f'Error {e} when booting Technical class.')