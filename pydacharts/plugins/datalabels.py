from pydantic import BaseModel
from pydacharts.models import Font, Color
from typing import Optional, Dict
from enum import Enum

Function = str


class DataLabelsPlugin(BaseModel):
    align: str = "center"
    anchor: str = "center"
    offset: Optional[int]
    padding: Optional[int]
    clip: Optional[bool]
    font: Optional[Font]
    labels: Optional[Dict]

    # Found these at https://chartjs-plugin-datalabels.netlify.app/samples/charts/line.html
    color: Optional[Color]
    borderRadius: Optional[int]


class Label(BaseModel):
    """
    Represents a DataLabels Label instance
    """

    class Anchor(str, Enum):
        center_ = "center"
        start = "start"
        end = "end"

    class Align(str, Enum):
        center_ = "center"
        start = "start"
        end = "end"
        right = "right"
        bottom = "bottom"
        left = "left"
        top = "top"

    align: Optional[Align]
    anchor: Optional[Anchor]
    color: Optional[Color]
    font: Optional[Font]
    formatter: Optional[str]
    offset: Optional[int]
    opacity: Optional[float]

    padding: Optional[int]
    borderRadius: Optional[int]
    backgroundColor: Optional[Color]
