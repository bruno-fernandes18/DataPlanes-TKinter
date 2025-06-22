from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class Flight_level:
    """Information about a particular flight level."""

    has_data: bool
    ias: Optional[float] = None
    roc: Optional[int] = None
    climb: Optional[Union[int, str]] = None

    def __post_init__(self) -> None:
        if not self.has_data:
            self.ias = None
            self.roc = None
            self.climb = None
        elif self.climb == "MACH" and self.ias is not None:
            self.ias = round(float(self.ias), 2)
