from enum import Enum
from typing import Any, Dict, List, Optional, Union, Sequence

from pydantic import BaseModel, Field

RgbStr = str  # Like `rgb(255, 99, 132)`
Function = Optional[str]  # Placeholder for what we'll define in JS
Color = str


class ChartType(str, Enum):
    line = "line"
    bar = "bar"
    horizontalbar = "horizontalBar"
    radar = "radar"
    doughnut = "doughnut"
    pie = "pie"
    polararea = "polarArea"
    bubble = "bubble"
    scatter = "scatter"
    # This is a chart type provided by a plugin
    sankey = "sankey"


class StepOption(str, Enum):
    before = "before"
    after = "after"
    middle = "middle"


class TitleAlign(str, Enum):
    start = "start"
    center_ = "center"
    end = "end"


class LegendAlign(str, Enum):
    top = "top"
    left = "left"
    bottom = "bottom"
    right = "right"
    chartArea = "chartArea"


class LegendPosition(str, Enum):
    top = "top"
    left = "left"
    bottom = "bottom"
    right = "right"
    chartArea = "chartArea"


class PaddingObject(BaseModel):
    left: Optional[int]
    right: Optional[int]
    top: Optional[int]
    bottom: Optional[int]


class PaddingXY(BaseModel):
    x: Optional[int]
    y: Optional[int]


Padding = Union[int, PaddingObject, PaddingXY]


class Layout(BaseModel):
    """
    the global options for the chart layout is defined in Chart.defaults.layout
    """

    padding: Padding


class Dataset(BaseModel):
    label: str
    data: List[Any]
    borderColor: Optional[Union[List[RgbStr], RgbStr]]
    backgroundColor: Optional[Union[List[RgbStr], RgbStr]]
    showLine: Optional[bool]
    hoverOffset: Optional[int]
    # Support stacked bar charts
    stack: Optional[str]
    # Support rounded bars
    borderWidth: Optional[int]
    borderRadius: Optional[int]
    borderSkipped: Optional[bool]
    borderDash: Optional[List[int]]
    # Support "combo chart"
    type: Optional[Union[ChartType, str]]


class LineDataSet(Dataset):
    showLine: Optional[bool] = True
    fill: Optional[bool] = False
    tension: Optional[float] = 0.1
    stepped: Optional[Union[bool, StepOption]]


class PieDataSet(Dataset):
    ...


class Data(BaseModel):
    labels: List[str]
    datasets: Sequence[Dataset]


class LineData(Data):
    datasets: Sequence[LineDataSet]


class PieData(Data):
    datasets: Sequence[PieDataSet]


class Font(BaseModel):
    family: Optional[str]
    size: Optional[int]
    style: Optional[str]
    lineHeight: Optional[float]
    weight: Optional[Union[str, int]]


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


class Title(BaseModel):
    display: bool = True
    text: str
    color: Optional[RgbStr]
    font: Optional[Font]
    padding: Optional[Padding]
    align: Optional[TitleAlign]


class LegendLabels(BaseModel):
    """
    Namespace: options.plugins.legend.labels
    """

    boxWidth: int = Field(40, description="Width of coloured box.")
    boxHeight: int = Field(description="Height of the coloured box.")
    color: Color = Field(description="Color of label and the strikethrough.")
    font: Optional[Font]
    padding: Optional[int] = Field(description="Padding between rows of colored boxes.")
    generateLabels: Optional[Function] = Field(
        description="Generates legend items for each thing in the legend. Default implementation returns the text + styling for the color box. See Legend Item for details."
    )
    filter: Optional[Function] = Field(
        description="Filters legend items out of the legend. Receives 2 parameters, a Legend Item and the chart data."
    )
    sort: Optional[Function] = Field(
        description="Sorts legend items. Type is : sort(a: LegendItem, b: LegendItem, data: ChartData): number;. Receives 3 parameters, two Legend Items and the chart data. The return value of the function is a number that indicates the order of the two legend item parameters. The ordering matches the return value of Array.prototype.sort()"
    )
    pointStyle: PointStyle = Field(
        default=PointStyle.circle,
        description="If specified, this style of point is used for the legend. Only used if usePointStyle is true.",
    )
    textAlign: str = Field(
        default=TitleAlign.center,
        description="Horizontal alignment of the label text. Options are: 'left', 'right' or 'center'.",
    )
    usePointStyle: Optional[bool] = Field(
        default=False,
        description="Label style will match corresponding point style (size is based on the minimum value between boxWidth and font.size).",
    )


class LegendTitle(BaseModel):

    color: Optional[Color] = Field(description="Color of text.")
    display: Optional[bool] = Field(description="Is the legend title displayed.")
    font: Optional[Font] = Field(description="See Fonts")
    padding: Optional[Padding] = Field(description="Padding around the title.")
    text: Optional[str] = Field(description="The string title.")


class Legend(BaseModel):

    display: Optional[bool] = Field(description="Is the legend shown?")
    position: Optional[str] = Field(description="Position of the legend")
    align: Optional[str] = Field(description="Alignment of the legend")
    maxHeight: Optional[int] = Field(description="Maximum height of the legend, in pixels")
    maxWidth: Optional[int] = Field(description="Maximum width of the legend, in pixels")
    fullSize: Optional[bool] = Field(
        description="Marks that this box should take the full width/height of the canvas (moving other boxes). This is unlikely to need to be changed in day-to-day use."
    )
    onClick: Optional[Function] = Field(
        description="A callback that is called when a click event is registered on a label item. Arguments: [event, legendItem, legend]."
    )
    onHover: Optional[Function] = Field(
        description="A callback that is called when a 'mousemove' event is registered on top of a label item. Arguments: [event, legendItem, legend]."
    )
    onLeave: Optional[Function] = Field(
        description="A callback that is called when a 'mousemove' event is registered outside of a previously hovered label item. Arguments: [event, legendItem, legend]."
    )
    reverse: Optional[bool] = Field(description="Legend will show datasets in reverse order.")
    labels: Optional[LegendLabels] = Field(description="See the Legend Label Configuration section below.")
    rtl: Optional[bool] = Field(description="true for rendering the legends from right to left.")
    textDirection: Optional[str] = Field(
        description="This will force the text direction 'rtl' or 'ltr' on the canvas for rendering the legend, regardless of the css specified on the canvas"
    )
    title: Optional[LegendTitle] = Field(description="See the Legend Title Configuration section below.")


class Plugins(BaseModel):
    legend: Optional[Legend]
    title: Optional[Title]
    # datalabels: Optional[Union[DataLabelsPlugin, List[DataLabelsPlugin]]]


class Ticks(BaseModel):
    """
    Namespace: options.scales[scaleId].ticks
    """

    backdropColor: Optional[Color] = Field(description="Color of label backdrops.")
    backdropPadding: Optional[Padding] = Field(description="Padding of label backdrop.")
    callback: Optional[Function] = Field(
        description="Returns the string representation of the tick value as it should be displayed on the chart.."
    )
    display: Optional[bool] = Field(description="If true, show tick labels.")
    color: Optional[Color] = Field(description="Color of ticks.")
    font: Optional[Font]
    major: Optional[Dict] = Field(description="Major ticks configuration.")
    padding: Optional[int] = Field(description="Sets the offset of the tick labels from the axis")
    showLabelBackdrop: Optional[bool] = Field(description="If true, draw a background behind the tick labels.")
    textStrokeColor: Optional[Color] = Field(description="The color of the stroke around the text.")
    textStrokeWidth: Optional[int] = Field(description="Stroke width around the text.")
    z: Optional[int] = Field(
        description="z-index of tick layer. Useful when ticks are drawn on chart area. Values <= 0 are drawn under datasets, > 0 on top."
    )


class CartesianTicks(Ticks):
    """
    Namespace: options.scales[scaleId].ticks
    """

    align: Optional[str] = Field(description="The tick alignment along the axis. Can be 'start', 'center', or 'end'.")
    crossAlign: Optional[str] = Field(
        description="The tick alignment perpendicular to the axis. Can be 'near', 'center', or 'far'. See Tick Alignment"
    )
    sampleSize: Optional[int] = Field(
        description="The number of ticks to examine when deciding how many labels will fit. Setting a smaller value will be faster, but may be less accurate when there is large variability in label length."
    )
    autoSkip: Optional[bool] = Field(
        description="If true, automatically calculates how many labels can be shown and hides labels accordingly. Labels will be rotated up to maxRotation before skipping any. Turn autoSkip off to show all labels no matter what."
    )
    autoSkipPadding: Optional[int] = Field(
        description="Padding between the ticks on the horizontal axis when autoSkip is enabled."
    )
    includeBounds: Optional[bool] = Field(
        description='Should the defined min and max values be presented as ticks even if they are not "nice".'
    )
    labelOffset: Optional[int] = Field(
        description="Distance in pixels to offset the label from the centre point of the tick (in the x-direction for the x-axis, and the y-direction for the y-axis). Note: this can cause labels at the edges to be cropped by the edge of the canvas"
    )
    maxRotation: Optional[int] = Field(
        description="Maximum rotation for tick labels when rotating to condense labels. Note: Rotation doesn't occur until necessary. Note: Only applicable to horizontal scales."
    )
    minRotation: Optional[int] = Field(
        description="Minimum rotation for tick labels. Note: Only applicable to horizontal scales."
    )
    mirror: Optional[bool] = Field(
        description="Flips tick labels around axis, displaying the labels inside the chart instead of outside. Note: Only applicable to vertical scales."
    )
    padding: Optional[int] = Field(
        description="Padding between the tick label and the axis. When set on a vertical axis, this applies in the horizontal (X) direction. When set on a horizontal axis, this applies in the vertical (Y) direction."
    )


class ScaleOptions(BaseModel):
    display: Optional[bool] = True
    beginAtZero: Optional[bool]
    title: Optional[Title]
    min: Optional[int]
    max: Optional[int]
    stacked: Optional[bool]
    position: Optional[str]
    offset: bool = True
    ticks: Optional[Union[Ticks, CartesianTicks]]
    barThickness: Optional[int]
    labels: Optional[Any]


class Scales(BaseModel):
    y: Optional[ScaleOptions]
    x: Optional[ScaleOptions]
    # Added for datalabels plugin
    xAxes: Optional[List[ScaleOptions]]
    yAxes: Optional[List[ScaleOptions]]
    # x1, y1 represent additional
    y1: Optional[ScaleOptions]
    x1: Optional[ScaleOptions]


class Interaction(BaseModel):
    intersect: Optional[bool]  # False for stacked charts


class Options(BaseModel):
    responsive: bool = True
    plugins: Optional[Plugins]
    scales: Optional[Scales]
    elements: Optional[Dict]
    indexAxis: Optional[str]
    interaction: Optional[Interaction]

    # Bar chart option
    barPercentage: Optional[float]


class Config(BaseModel):
    type: Union[ChartType, str] = ChartType.line
    data: Data
    options: Optional[Options]


class Grid(BaseModel):
    drawOnChartArea: Optional[bool] = True
