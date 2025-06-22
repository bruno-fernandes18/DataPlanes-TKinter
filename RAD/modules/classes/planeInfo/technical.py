from dataclasses import dataclass
from typing import Optional


@dataclass(init=False)
class Technical:
    """Technical information for an aircraft."""

    manufacturer: str
    birth_year: int
    model: str
    variation: str
    wingspan: float
    wing_position: str
    engn_position: str
    tail_config: str
    land_gear: str
    length: float
    height: float
    eu_specific_analysis: Optional[str] = None

    def __init__(self,
                 manufacturer: str,
                 birth_year: int,
                 model: str,
                 variation: str,
                 wingspan: float,
                 wing_position: str,
                 engn_position: str,
                 tail_config: str,
                 land_gear: str,
                 length: float,
                 height: float,
                 eu_specific_analysis: Optional[str] = None) -> None:
        self.manufacturer = manufacturer
        self.birth_year = birth_year
        self.model = model
        self.variation = variation
        self.wingspan = wingspan
        self.wing_position = wing_position
        self.engn_position = engn_position
        self.tail_config = tail_config
        self.land_gear = land_gear
        self.length = length
        self.height = height
        self.eu_specific_analysis = eu_specific_analysis
        self.__post_init__()

    def __post_init__(self) -> None:
        """Round numeric values and normalise optional fields."""
        self.wingspan = round(self.wingspan, 2)
        self.length = round(self.length, 2)
        self.height = round(self.height, 2)
        if isinstance(self.eu_specific_analysis, str) and self.eu_specific_analysis == "None":
            self.eu_specific_analysis = None
