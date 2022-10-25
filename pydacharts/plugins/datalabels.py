from enum import Enum
from typing import Literal, Optional, Union

from pydantic import BaseModel, Field

from pydacharts.chartjs_types import Color, Font, Function, Padding, number

"""
https://chartjs-plugin-datalabels.netlify.app/guide/options.html

The plugin options can be changed at 3 different levels and are evaluated with the following priority:

per dataset: dataset.datalabels.*
per chart: options.plugins.datalabels.*
or globally: Chart.defaults.plugins.datalabels.*
"""


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


"""
https://chartjs-plugin-datalabels.netlify.app/guide/options.html#style-options
Style options are usually inputs for fillStyle or strokeStyle

The following values are supported:
string parsed as CSS color
CanvasGradient
CanvasPattern
"""
DataLabelsPluginStyle = str

align = Literal[
    "center",  # (default): the label is centered on the anchor point
    "start",  #: the label is positioned before the anchor point, following the same direction
    "end",  #: the label is positioned after the anchor point, following the same direction
    "right",  #: the label is positioned to the right of the anchor point (0°)
    "bottom",  #: the label is positioned to the bottom of the anchor point (90°)
    "left",  #: the label is positioned to the left of the anchor point (180°)
    "top",  #: the label is positioned to the top of the anchor point (270°)
]

degrees = int


class DataLabelsPlugin(BaseModel):
    align: Optional[Union[align, degrees]]
    anchor: Optional[str] = "center"
    backgroundColor: Optional[DataLabelsPluginStyle]
    borderColor: Optional[DataLabelsPluginStyle]
    borderRadius: Optional[number]
    borderWidth: Optional[number]
    clamp: Optional[bool]
    clip: Optional[bool]
    color: Optional[DataLabelsPluginStyle]
    display: Optional[Union[Function, Literal[True, False, "auto"]]] = Field(
        True, description="controls the visibility of labels"
    )
    font: Optional[Font]
    formatter: Optional[Function]
    labels: Optional[object]
    listeners: Optional[object]
    offset: Optional[number] = Field(
        4,
        description="The offset represents the distance (in pixels) to pull the label away from the anchor point. This option is not applicable when align is 'center'. Also note that if align is 'start', the label is moved in the opposite direction. The default value is 4.",
    )
    opacity: Optional[number]
    padding: Optional[Padding]
    rotation: Optional[degrees]
    textAlign: Optional[str]
    textStrokeColor: Optional[DataLabelsPluginStyle]
    textStrokeWidth: Optional[number]
    textShadowBlur: Optional[number]
    textShadowColor: Optional[Color]


if __name__ == "__main__":
    print(DataLabelsPlugin().json(exclude_none=True))
