class Cruise:
    '''Cruise object containing TAS, MACH speed, Ceiling and Range data.'''
    def __init__(self, tas: int, mach: float, ceiling: int, range: int):
        '''Initializes Cruise object.'''
        try:
            self.tas: int = tas
            self.mach: float = None if mach == -1 else round(float(mach), 2)
            self.ceiling: int = ceiling
            self.range: int = range
        except Exception as e:
            print(f'Error {e} when booting Cruise class.')