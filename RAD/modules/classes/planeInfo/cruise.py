from dataclasses import dataclass
from typing import Optional


@dataclass
class Cruise:
    """Cruise performance data."""

    tas: int = 0
    mach: Optional[float] = None
    ceiling: int = 0
    range: int = 0

    def __post_init__(self) -> None:
        if self.mach is not None:
            self.mach = round(float(self.mach), 2)
