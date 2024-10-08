from enum import Enum
from typing import Literal

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

    align: Align | None = None
    anchor: Anchor | None = None
    clamp: bool | None = None
    color: Color | None = None
    font: Font | None = None
    formatter: str | None = None
    offset: int | None = None
    opacity: float | None = None

    padding: int | None = None
    borderRadius: int | None = None
    backgroundColor: Color | None = None


"""
https://chartjs-plugin-datalabels.netlify.app/guide/options.html#style-options
Style options are usually inputs for fillStyle or strokeStyle

The following values are supported:
string parsed as CSS color
CanvasGradient
CanvasPattern
"""
DataLabelsPluginStyle = str

align_values = Literal[
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
    align: align_values | degrees | None = None
    anchor: str | None = "center"
    backgroundColor: DataLabelsPluginStyle | None = None
    borderColor: DataLabelsPluginStyle | None = None
    borderRadius: number | None = None
    borderWidth: number | None = None
    clamp: bool | None = None
    clip: bool | None = None
    color: DataLabelsPluginStyle | None = None
    display: Function | Literal[True, False, "auto"] | None = Field(
        True, description="controls the visibility of labels"
    )
    font: Font | None = None
    formatter: Function | None = None
    labels: object | None = None
    listeners: object | None = None
    offset: number | None = Field(
        4,
        description="The offset represents the distance (in pixels) to pull the label away from the anchor point. This option is not applicable when align is 'center'. Also note that if align is 'start', the label is moved in the opposite direction. The default value is 4.",
    )
    opacity: number | None = None
    padding: Padding | None = None
    rotation: degrees | None = None
    textAlign: str | None = None
    textStrokeColor: DataLabelsPluginStyle | None = None
    textStrokeWidth: number | None = None
    textShadowBlur: number | None = None
    textShadowColor: Color | None = None


if __name__ == "__main__":
    print(DataLabelsPlugin().model_dump_json(exclude_none=True))
