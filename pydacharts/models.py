from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Sequence, Union

from pydantic import BaseModel, Field

from pydacharts.chartjs_types import Color, Font, Function, Padding, PointStyle, RgbStr, number
from pydacharts.elements import Elements
from pydacharts.plugins.datalabels import DataLabelsPlugin


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


class Layout(BaseModel):
    """
    the global options for the chart layout is defined in Chart.defaults.layout
    """

    padding: Optional[Padding]


class Dataset(BaseModel):
    label: Optional[str]
    data: Optional[List[Any]]
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
    order: Optional[int]

    datalabels: Optional[DataLabelsPlugin]


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


class Title(BaseModel):
    display: bool = True
    text: Optional[str]
    color: Optional[RgbStr]
    font: Optional[Font]
    padding: Optional[Padding]
    align: Optional[Literal["left", "right", "center"]]


class LegendLabels(BaseModel):
    """
    Namespace: options.plugins.legend.labels
    """

    boxWidth: Optional[int] = Field(40, description="Width of coloured box.")
    boxHeight: Optional[int] = Field(description="Height of the coloured box.")
    color: Optional[Color] = Field(description="Color of label and the strikethrough.")
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
    pointStyle: Optional[PointStyle] = Field(
        default=PointStyle.circle,
        description="If specified, this style of point is used for the legend. Only used if usePointStyle is true.",
    )
    textAlign: Optional[Literal["left", "right", "center"]] = Field(
        default="center",
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


class TooltipCallbacks(BaseModel):
    beforeTitle: Optional[Function] = Field(description="Returns the text to render before the title.")
    title: Optional[Function] = Field(description="Returns text to render as the title of the tooltip.")
    afterTitle: Optional[Function] = Field(description="Returns text to render after the title.")
    beforeBody: Optional[Function] = Field(description="Returns text to render before the body section.")
    beforeLabel: Optional[Function] = Field(
        description="Returns text to render before an individual label. This will be called for each item in the tooltip."
    )
    label: Optional[Function] = Field(
        description="Returns text to render for an individual item in the tooltip. more..."
    )
    labelColor: Optional[Function] = Field(description="Returns the colors to render for the tooltip item. more...")
    labelTextColor: Optional[Function] = Field(
        description="Returns the colors for the text of the label for the tooltip item."
    )
    labelPointStyle: Optional[Function] = Field(
        description="Returns the point style to use instead of color boxes if usePointStyle is true (object with values pointStyle and rotation). Default implementation uses the point style from the dataset points. more..."
    )
    afterLabel: Optional[Function] = Field(description="Returns text to render after an individual label.")
    afterBody: Optional[Function] = Field(description="Returns text to render after the body section.")
    beforeFooter: Optional[Function] = Field(description="Returns text to render before the footer section.")
    footer: Optional[Function] = Field(description="Returns text to render as the footer of the tooltip.")
    afterFooter: Optional[Function] = Field(description="Text to render after the footer section.")


class Tooltip(BaseModel):
    """
    https://www.chartjs.org/docs/latest/configuration/tooltip.html#tooltip-callbacks
    """

    enabled: Optional[bool] = Field(description="Are on-canvas tooltips enabled?")
    external: Optional[Function] = Field(description="See external tooltip section.")
    mode: Optional[str] = Field(description="Sets which elements appear in the tooltip.")
    intersect: Optional[bool] = Field(
        description="If true, the tooltip mode applies only when the mouse position intersects with an element. If false, the mode will be applied at all times."
    )
    position: Optional[str] = Field(description="The mode for positioning the tooltip.")
    callbacks: Optional[TooltipCallbacks] = Field(description="See the callbacks section.")
    itemSort: Optional[Function] = Field(description="Sort tooltip items.")
    filter: Optional[Function] = Field(description="Filter tooltip items.")
    backgroundColor: Optional[Color] = Field(description="Background color of the tooltip.")
    titleColor: Optional[Color] = Field(description="Color of title text.")
    titleFont: Optional[Font] = Field(description="See Fonts.")
    titleAlign: Optional[str] = Field(description="Horizontal alignment of the title text lines.")
    titleSpacing: Optional[number] = Field(description="Spacing to add to top and bottom of each title line.")
    titleMarginBottom: Optional[number] = Field(description="Margin to add on bottom of title section.")
    bodyColor: Optional[Color] = Field(description="Color of body text.")
    bodyFont: Optional[Font] = Field(description="See Fonts.")
    bodyAlign: Optional[str] = Field(description="Horizontal alignment of the body text lines.")
    bodySpacing: Optional[int] = Field(description="Spacing to add to top and bottom of each tooltip item.")
    footerColor: Optional[Color] = Field(description="Color of footer text.")
    footerFont: Optional[Font] = Field(description="See Fonts.")
    footerAlign: Optional[str] = Field(description="Horizontal alignment of the footer text lines.")
    footerSpacing: Optional[int] = Field(description="Spacing to add to top and bottom of each footer line.")
    footerMarginTop: Optional[int] = Field(description="Margin to add before drawing the footer.")
    padding: Optional[Padding] = Field(description="Padding inside the tooltip.")
    caretPadding: Optional[int] = Field(
        description="Extra distance to move the end of the tooltip arrow away from the tooltip point."
    )
    caretSize: Optional[int] = Field(description="Size, in px, of the tooltip arrow.")
    cornerRadius: Optional[int] = Field(description="Radius of tooltip corner curves.")
    multiKeyBackground: Optional[Color] = Field(
        description="Color to draw behind the colored boxes when multiple items are in the tooltip."
    )
    displayColors: Optional[bool] = Field(description="If true, color boxes are shown in the tooltip.")
    boxWidth: Optional[int] = Field(description="Width of the color box if displayColors is true.")
    boxHeight: Optional[int] = Field(description="Height of the color box if displayColors is true.")
    boxPadding: Optional[int] = Field(description="Padding between the color box and the text.")
    usePointStyle: Optional[int] = Field(
        description="Use the corresponding point style (from dataset options) instead of color boxes, ex: star, triangle etc. (size is based on the minimum value between boxWidth and boxHeight)."
    )
    borderColor: Optional[Color] = Field(description="Color of the border.")
    borderWidth: Optional[int] = Field(description="Size of the border.")
    rtl: Optional[bool] = Field(description="true for rendering the tooltip from right to left.")
    textDirection: Optional[Literal["rtl", "ltr"]] = Field(
        description="This will force the text direction 'rtl' or 'ltr on the canvas for rendering the tooltips, regardless of the css specified on the canvas"
    )
    xAlign: Optional[str] = Field(description="Position of the tooltip caret in the X direction.")
    yAlign: Optional[str] = Field(description="Position of the tooltip caret in the Y direction.")


class Plugins(BaseModel):
    legend: Optional[Legend]
    title: Optional[Title]
    datalabels: Optional[Union[DataLabelsPlugin, List[DataLabelsPlugin]]]
    tooltip: Optional[Tooltip]


class Ticks(BaseModel):
    """
    Namespace: options.scales[scaleId].ticks
    """

    beginAtZero: Optional[bool]
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
    stepSize: Optional[int]
    textStrokeColor: Optional[Color] = Field(description="The color of the stroke around the text.")
    textStrokeWidth: Optional[int] = Field(description="Stroke width around the text.")
    z: Optional[int] = Field(
        description="z-index of tick layer. Useful when ticks are drawn on chart area. Values <= 0 are drawn under datasets, > 0 on top."
    )


class Grid(BaseModel):
    borderColor: Optional[Color] = Field(description="The color of the border line.")
    borderWidth: Optional[float] = Field(description="The width of the border line.")
    borderDash: Optional[List[float]] = Field(description="Length and spacing of dashes on grid lines. See MDN.")
    borderDashOffset: Optional[float] = Field(description="Offset for line dashes. See MDN.")
    circular: Optional[bool] = Field(description="If true, gridlines are circular (on radar chart only).")
    color: Optional[Color] = Field(
        description="The color of the grid lines. If specified as an array, the first color applies to the first grid line, the second to the second grid line, and so on."
    )
    display: Optional[bool] = Field(description="If false, do not display grid lines for this axis.")
    drawBorder: Optional[bool] = Field(
        description="If true, draw a border at the edge between the axis and the chart area."
    )
    drawOnChartArea: Optional[bool] = Field(
        description="If true, draw lines on the chart area inside the axis lines. This is useful when there are multiple axes and you need to control which grid lines are drawn."
    )
    drawTicks: Optional[bool] = Field(
        description="If true, draw lines beside the ticks in the axis area beside the chart."
    )
    lineWidth: Optional[float] = Field(description="Stroke width of grid lines.")
    offset: Optional[bool] = Field(
        description="If true, grid lines will be shifted to be between labels. This is set to true for a bar chart by default."
    )
    tickBorderDash: Optional[List[float]] = Field(
        description="Length and spacing of the tick mark line. If not set, defaults to the grid line borderDash value."
    )
    tickBorderDashOffset: Optional[float] = Field(
        description="Offset for the line dash of the tick mark. If unset, defaults to the grid line borderDashOffset value"
    )
    tickColor: Optional[Color] = Field(
        description="Color of the tick line. If unset, defaults to the grid line color."
    )
    tickLength: Optional[int] = Field(description="Length in pixels that the grid lines will draw into the axis area.")
    tickWidth: Optional[int] = Field(
        description="Width of the tick mark in pixels. If unset, defaults to the grid line width."
    )
    z: Optional[int] = Field(
        description="z-index of gridline layer. Values <= 0 are drawn under datasets, > 0 on top."
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
    grid: Optional[Grid]


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

    responsive: Optional[bool] = Field(
        True, description="Resizes the chart canvas when its container does (important note...)."
    )
    maintainAspectRatio: Optional[bool] = Field(
        True, description="Maintain the original canvas aspect ratio (width / height) when resizing."
    )
    aspectRatio: Optional[Union[number, Function]] = Field(
        2,
        description="Canvas aspect ratio (i.e. width / height, a value of 1 representing a square canvas). Note that this option is ignored if the height is explicitly defined either as attribute or via the style.",
    )
    onResize: Optional[Function] = Field(
        description="Called when a resize occurs. Gets passed two arguments: the chart instance and the new size."
    )
    resizeDelay: Optional[number] = Field(
        0,
        description="Delay the resize update by give amount of milliseconds. This can ease the resize process by debouncing update of the elements.",
    )

    plugins: Optional[Plugins]
    scales: Optional[Scales]
    elements: Optional[Elements]
    indexAxis: Optional[str]
    interaction: Optional[Interaction]

    # Bar chart option
    barPercentage: Optional[float]
    layout: Optional[Layout]

    # Doughnut chart
    cutout: Optional[str]


class Config(BaseModel):
    type: Union[ChartType, str] = ChartType.line
    data: Optional[Data]
    options: Optional[Options]


if __name__ == "__main__":

    Layout().json()
    Dataset().json()
    Data(labels=["1", "2", "3"], datasets=[Dataset()]).json()
    Font().json()
    Title().json()
    LegendLabels().json()
    LegendTitle().json()
    Legend().json()
    DataLabelsPlugin().json()
    TooltipCallbacks().json()
    Tooltip().json()
    Plugins().json()
    Ticks().json()
    Grid().json()
    ScaleOptions().json()
    Scales().json()
    Interaction().json()
    Options().json()
    Config().json()
