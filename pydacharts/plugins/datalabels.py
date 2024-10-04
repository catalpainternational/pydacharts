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

    align: Optional[Align] = None
    anchor: Optional[Anchor] = None
    clamp: Optional[bool] = None
    color: Optional[Color] = None
    font: Optional[Font] = None
    formatter: Optional[str] = None
    offset: Optional[int] = None
    opacity: Optional[float] = None

    padding: Optional[int] = None
    borderRadius: Optional[int] = None
    backgroundColor: Optional[Color] = None


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
    align: Optional[Union[align, degrees]] = None
    anchor: Optional[str] = "center"
    backgroundColor: Optional[DataLabelsPluginStyle] = None
    borderColor: Optional[DataLabelsPluginStyle] = None
    borderRadius: Optional[number] = None
    borderWidth: Optional[number] = None
    clamp: Optional[bool] = None
    clip: Optional[bool] = None
    color: Optional[DataLabelsPluginStyle] = None
    display: Optional[Union[Function, Literal[True, False, "auto"]]] = Field(
        True, description="controls the visibility of labels"
    )
    font: Optional[Font] = None
    formatter: Optional[Function] = None
    labels: Optional[object] = None
    listeners: Optional[object] = None
    offset: Optional[number] = Field(
        4,
        description="The offset represents the distance (in pixels) to pull the label away from the anchor point. This option is not applicable when align is 'center'. Also note that if align is 'start', the label is moved in the opposite direction. The default value is 4.",
    )
    opacity: Optional[number] = None
    padding: Optional[Padding] = None
    rotation: Optional[degrees] = None
    textAlign: Optional[str] = None
    textStrokeColor: Optional[DataLabelsPluginStyle] = None
    textStrokeWidth: Optional[number] = None
    textShadowBlur: Optional[number] = None
    textShadowColor: Optional[Color] = None


if __name__ == "__main__":
    print(DataLabelsPlugin().json(exclude_none=True))
