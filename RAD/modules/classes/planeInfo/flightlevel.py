class Flight_level:
    def __init__(self, has_data: bool, ias, roc: int, climb):
        try:
            self.has_data: bool = has_data
            if self.has_data == True:
                self.ias = round(float(ias),2) if climb == 'MACH' else ias
                self.roc: int = roc
                self.climb: int = climb
            else:
                self.ias: bool = False
                self.roc: bool = False
                self.climb: bool = False
        except Exception as e:
            print(f'Error {e} when booting Flight Level class.')