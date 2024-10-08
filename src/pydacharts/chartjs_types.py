from enum import Enum

from pydantic import BaseModel

RgbStr = str  # Like `rgb(255, 99, 132)`
Function = str | None  # Placeholder for what we'll define in JS
Color = str
Script = str  # This is intended to represent a "well known function" provided at a given namespace by a JS library
number = int | float
# TODO: Add specific well known scripts from what we've developed in DIRD?

"""
Color examples for reference:
color: 'green'                  // named color
color: '#dc143c'                // HEX color
color: 'rgb(51, 170, 51)'       // RGB color (opaque)
color: 'rgba(51, 170, 51, .5)'  // RGBa color (semi-transparent)
"""


class Font(BaseModel):
    family: str | None = None
    size: int | None = None
    style: str | None = None
    lineHeight: float | None = None
    weight: str | int | None = None


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
    left: int | None = None
    right: int | None = None
    top: int | None = None
    bottom: int | None = None


class PaddingXY(BaseModel):
    x: int | None = None
    y: int | None = None


Padding = int | PaddingObject | PaddingXY


if __name__ == "__main__":
    PaddingObject().model_dump_json()
    PaddingXY().model_dump_json()
