from dataclasses import dataclass, field


@dataclass
class Landing:
    """Landing performance information."""

    vat: int
    distance: int
    apc: str = field(init=False)

    def __post_init__(self) -> None:
        self.apc = self.find_apc(self.vat)

    def find_apc(self, vat: int) -> str:
        '''Returns APC from VAT in knots.'''
        if vat < 91:
            return 'A'
        elif vat < 121:
            return 'B'
        elif vat < 141:
            return 'C'
        elif vat < 166:
            return 'D'
        elif vat >= 167:
            return 'E'