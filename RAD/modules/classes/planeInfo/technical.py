from dataclasses import dataclass
from typing import Optional


@dataclass
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

    def __post_init__(self) -> None:
        """Round numeric values and normalise optional fields."""
        self.wingspan = round(self.wingspan, 2)
        self.length = round(self.length, 2)
        self.height = round(self.height, 2)
        if isinstance(self.eu_specific_analysis, str) and self.eu_specific_analysis == "None":
            self.eu_specific_analysis = None
