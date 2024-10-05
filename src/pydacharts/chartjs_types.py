from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel

RgbStr = str  # Like `rgb(255, 99, 132)`
Function = Optional[str]  # Placeholder for what we'll define in JS
Color = str
Script = str  # This is intended to represent a "well known function" provided at a given namespace by a JS library
number = Union[int, float]
# TODO: Add specific well known scripts from what we've developed in DIRD?

"""
Color examples for reference:
color: 'green'                  // named color
color: '#dc143c'                // HEX color
color: 'rgb(51, 170, 51)'       // RGB color (opaque)
color: 'rgba(51, 170, 51, .5)'  // RGBa color (semi-transparent)
"""


class Font(BaseModel):
    family: Optional[str] = None
    size: Optional[int] = None
    style: Optional[str] = None
    lineHeight: Optional[float] = None
    weight: Optional[Union[str, int]] = None


class PointStyle(str, Enum):
    circle = "circle"
    cross = "cross"
    crossRot = "crossRot"
    dash = "dash"
    line = "line"
    rect = "rect"
    rectRounded = "rectRounded"
    rectRot = "rectRot"
    star = "star"
    triangle = "triangle"


class PaddingObject(BaseModel):
    left: Optional[int] = None
    right: Optional[int] = None
    top: Optional[int] = None
    bottom: Optional[int] = None


class PaddingXY(BaseModel):
    x: Optional[int] = None
    y: Optional[int] = None


Padding = Union[int, PaddingObject, PaddingXY]


if __name__ == "__main__":

    PaddingObject().model_dump_json()
    PaddingXY().model_dump_json()
