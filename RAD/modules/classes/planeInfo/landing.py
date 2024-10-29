class Landing:
    def __init__(self, vat: int, distance: int):
        self.vat: int = vat
        self.apc: str = self.find_apc(vat)
        self.distance: int = distance

    def find_apc(self, vat: int) -> str:
        if vat < 91:
            return 'A'
        elif vat < 120:
            return 'B'
        elif vat < 140:
            return 'C'
        elif vat < 165:
            return 'D'
        elif vat >= 166:
            return 'E'