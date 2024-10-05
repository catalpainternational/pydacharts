from typing import List, Optional
from pydantic import BaseModel

from pydacharts.models import Font, RgbStr


class Label(BaseModel):
    text: str
    font: Optional[Font]
    color: Optional[RgbStr]


class DoughnutLabel(BaseModel):
    labels: List[Label]
