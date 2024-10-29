class Cruise:
    def __init__(self, tas: int, mach: float, ceiling: int, range: int):
        try:
            self.tas: int = tas
            self.mach: float = None if mach == -1 else round(float(mach), 2)
            self.ceiling: int = ceiling
            self.range: int = range
        except Exception as e:
            print(f'Error {e} when booting Cruise class.')