from collections.abc import Sequence
from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, Field

from pydacharts.chartjs_types import (
    Color,
    Font,
    Function,
    Padding,
    PointStyle,
    RgbStr,
    number,
)
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

    padding: Padding | None = None


class Dataset(BaseModel):
    label: str | None = None
    data: list[Any] | None = None
    borderColor: list[RgbStr] | RgbStr | None = None
    backgroundColor: list[RgbStr] | RgbStr | None = None
    showLine: bool | None = None
    hoverOffset: int | None = None
    # Support stacked bar charts
    stack: str | None = None
    # Support rounded bars
    borderWidth: int | None = None
    borderRadius: int | None = None
    borderSkipped: bool | None = None
    borderDash: list[int] | None = None
    # Support "combo chart"
    type: ChartType | str | None = None
    order: int | None = None

    datalabels: DataLabelsPlugin | None = None


class LineDataSet(Dataset):
    showLine: bool | None = True
    fill: bool | None = False
    tension: float | None = 0.1
    stepped: bool | StepOption | None = None


class PieDataSet(Dataset):
    fill: bool | None = False


class Data(BaseModel):
    labels: list[str]
    datasets: Sequence[Dataset]


class LineData(Data):
    datasets: Sequence[LineDataSet]


class PieData(Data):
    datasets: Sequence[PieDataSet]


class Title(BaseModel):
    display: bool = True
    text: str | None = None
    color: RgbStr | None = None
    font: Font | None = None
    padding: Padding | None = None
    align: Literal["left", "right", "center"] | None = None


class LegendLabels(BaseModel):
    """
    Namespace: options.plugins.legend.labels
    """

    boxWidth: int | None = Field(40, description="Width of coloured box.")
    boxHeight: int | None = Field(40, description="Height of the coloured box.")
    color: Color | None = Field(
        "black", description="Color of label and the strikethrough."
    )
    font: Font | None = None
    padding: int | None = Field(5, description="Padding between rows of colored boxes.")
    generateLabels: Function | None = Field(
        None,
        description="Generates legend items for each thing in the legend. Default implementation returns the text + styling for the color box. See Legend Item for details.",
    )
    filter: Function | None = Field(
        None,
        description="Filters legend items out of the legend. Receives 2 parameters, a Legend Item and the chart data.",
    )
    sort: Function | None = Field(
        None,
        description="Sorts legend items. Type is : sort(a: LegendItem, b: LegendItem, data: ChartData): number;. Receives 3 parameters, two Legend Items and the chart data. The return value of the function is a number that indicates the order of the two legend item parameters. The ordering matches the return value of Array.prototype.sort()",
    )
    pointStyle: PointStyle | None = Field(
        default=PointStyle.circle,
        description="If specified, this style of point is used for the legend. Only used if usePointStyle is true.",
    )
    textAlign: Literal["left", "right", "center"] | None = Field(
        default="center",
        description="Horizontal alignment of the label text. Options are: 'left', 'right' or 'center'.",
    )
    usePointStyle: bool | None = Field(
        default=False,
        description="Label style will match corresponding point style (size is based on the minimum value between boxWidth and font.size).",
    )


class LegendTitle(BaseModel):
    color: Color | None = Field(None, description="Color of text.")
    display: bool | None = Field(None, description="Is the legend title displayed.")
    font: Font | None = Field(None, description="See Fonts")
    padding: Padding | None = Field(None, description="Padding around the title.")
    text: str | None = Field(None, description="The string title.")


class Legend(BaseModel):
    display: bool | None = Field(None, description="Is the legend shown?")
    position: str | None = Field(None, description="Position of the legend")
    align: str | None = Field(None, description="Alignment of the legend")
    maxHeight: int | None = Field(
        None, description="Maximum height of the legend, in pixels"
    )
    maxWidth: int | None = Field(
        None, description="Maximum width of the legend, in pixels"
    )
    fullSize: bool | None = Field(
        None,
        description="Marks that this box should take the full width/height of the canvas (moving other boxes). This is unlikely to need to be changed in day-to-day use.",
    )
    onClick: Function | None = Field(
        None,
        description="A callback that is called when a click event is registered on a label item. Arguments: [event, legendItem, legend].",
    )
    onHover: Function | None = Field(
        None,
        description="A callback that is called when a 'mousemove' event is registered on top of a label item. Arguments: [event, legendItem, legend].",
    )
    onLeave: Function | None = Field(
        None,
        description="A callback that is called when a 'mousemove' event is registered outside of a previously hovered label item. Arguments: [event, legendItem, legend].",
    )
    reverse: bool | None = Field(
        None, description="Legend will show datasets in reverse order."
    )
    labels: LegendLabels | None = Field(
        None, description="See the Legend Label Configuration section below."
    )
    rtl: bool | None = Field(
        None, description="true for rendering the legends from right to left."
    )
    textDirection: str | None = Field(
        None,
        description="This will force the text direction 'rtl' or 'ltr' on the canvas for rendering the legend, regardless of the css specified on the canvas",
    )
    title: LegendTitle | None = Field(
        None, description="See the Legend Title Configuration section below."
    )


class TooltipCallbacks(BaseModel):
    beforeTitle: Function | None = Field(
        None, description="Returns the text to render before the title."
    )
    title: Function | None = Field(
        None, description="Returns text to render as the title of the tooltip."
    )
    afterTitle: Function | None = Field(
        None, description="Returns text to render after the title."
    )
    beforeBody: Function | None = Field(
        None, description="Returns text to render before the body section."
    )
    beforeLabel: Function | None = Field(
        None,
        description="Returns text to render before an individual label. This will be called for each item in the tooltip.",
    )
    label: Function | None = Field(
        None,
        description="Returns text to render for an individual item in the tooltip. more...",
    )
    labelColor: Function | None = Field(
        None, description="Returns the colors to render for the tooltip item. more..."
    )
    labelTextColor: Function | None = Field(
        None,
        description="Returns the colors for the text of the label for the tooltip item.",
    )
    labelPointStyle: Function | None = Field(
        None,
        description="Returns the point style to use instead of color boxes if usePointStyle is true (object with values pointStyle and rotation). Default implementation uses the point style from the dataset points. more...",
    )
    afterLabel: Function | None = Field(
        None, description="Returns text to render after an individual label."
    )
    afterBody: Function | None = Field(
        None, description="Returns text to render after the body section."
    )
    beforeFooter: Function | None = Field(
        None, description="Returns text to render before the footer section."
    )
    footer: Function | None = Field(
        None, description="Returns text to render as the footer of the tooltip."
    )
    afterFooter: Function | None = Field(
        None, description="Text to render after the footer section."
    )


class Tooltip(BaseModel):
    """
    https://www.chartjs.org/docs/latest/configuration/tooltip.html#tooltip-callbacks
    """

    enabled: bool | None = Field(None, description="Are on-canvas tooltips enabled?")
    external: Function | None = Field(None, description="See external tooltip section.")
    mode: str | None = Field(
        None, description="Sets which elements appear in the tooltip."
    )
    intersect: bool | None = Field(
        None,
        description="If true, the tooltip mode applies only when the mouse position intersects with an element. If false, the mode will be applied at all times.",
    )
    position: str | None = Field(
        None, description="The mode for positioning the tooltip."
    )
    callbacks: TooltipCallbacks | None = Field(
        None, description="See the callbacks section."
    )
    itemSort: Function | None = Field(None, description="Sort tooltip items.")
    filter: Function | None = Field(None, description="Filter tooltip items.")
    backgroundColor: Color | None = Field(
        None, description="Background color of the tooltip."
    )
    titleColor: Color | None = Field(None, description="Color of title text.")
    titleFont: Font | None = Field(None, description="See Fonts.")
    titleAlign: str | None = Field(
        None, description="Horizontal alignment of the title text lines."
    )
    titleSpacing: number | None = Field(
        None, description="Spacing to add to top and bottom of each title line."
    )
    titleMarginBottom: number | None = Field(
        None, description="Margin to add on bottom of title section."
    )
    bodyColor: Color | None = Field(None, description="Color of body text.")
    bodyFont: Font | None = Field(None, description="See Fonts.")
    bodyAlign: str | None = Field(
        None, description="Horizontal alignment of the body text lines."
    )
    bodySpacing: int | None = Field(
        None, description="Spacing to add to top and bottom of each tooltip item."
    )
    footerColor: Color | None = Field(None, description="Color of footer text.")
    footerFont: Font | None = Field(None, description="See Fonts.")
    footerAlign: str | None = Field(
        None, description="Horizontal alignment of the footer text lines."
    )
    footerSpacing: int | None = Field(
        None, description="Spacing to add to top and bottom of each footer line."
    )
    footerMarginTop: int | None = Field(
        None, description="Margin to add before drawing the footer."
    )
    padding: Padding | None = Field(None, description="Padding inside the tooltip.")
    caretPadding: int | None = Field(
        None,
        description="Extra distance to move the end of the tooltip arrow away from the tooltip point.",
    )
    caretSize: int | None = Field(
        None, description="Size, in px, of the tooltip arrow."
    )
    cornerRadius: int | None = Field(
        None, description="Radius of tooltip corner curves."
    )
    multiKeyBackground: Color | None = Field(
        None,
        description="Color to draw behind the colored boxes when multiple items are in the tooltip.",
    )
    displayColors: bool | None = Field(
        None, description="If true, color boxes are shown in the tooltip."
    )
    boxWidth: int | None = Field(
        None, description="Width of the color box if displayColors is true."
    )
    boxHeight: int | None = Field(
        None, description="Height of the color box if displayColors is true."
    )
    boxPadding: int | None = Field(
        None, description="Padding between the color box and the text."
    )
    usePointStyle: int | None = Field(
        None,
        description="Use the corresponding point style (from dataset options) instead of color boxes, ex: star, triangle etc. (size is based on the minimum value between boxWidth and boxHeight).",
    )
    borderColor: Color | None = Field(None, description="Color of the border.")
    borderWidth: int | None = Field(None, description="Size of the border.")
    rtl: bool | None = Field(
        None, description="true for rendering the tooltip from right to left."
    )
    textDirection: Literal["rtl", "ltr"] | None = Field(
        None,
        description="This will force the text direction 'rtl' or 'ltr on the canvas for rendering the tooltips, regardless of the css specified on the canvas",
    )
    xAlign: str | None = Field(
        None, description="Position of the tooltip caret in the X direction."
    )
    yAlign: str | None = Field(
        None, description="Position of the tooltip caret in the Y direction."
    )


class Plugins(BaseModel):
    legend: Legend | None = None
    title: Title | None = None
    datalabels: DataLabelsPlugin | list[DataLabelsPlugin] | None = None
    tooltip: Tooltip | None = None


class Ticks(BaseModel):
    """
    Namespace: options.scales[scaleId].ticks
    """

    beginAtZero: bool | None = None
    backdropColor: Color | None = Field(
        default=None, description="Color of label backdrops."
    )
    backdropPadding: Padding | None = Field(
        default=None, description="Padding of label backdrop."
    )
    callback: Function | None = Field(
        default=None,
        description="Returns the string representation of the tick value as it should be displayed on the chart..",
    )
    display: bool | None = Field(default=None, description="If true, show tick labels.")
    color: Color | None = Field(default=None, description="Color of ticks.")
    font: Font | None = None
    major: dict | None = Field(default=None, description="Major ticks configuration.")
    padding: int | None = Field(
        default=None, description="Sets the offset of the tick labels from the axis"
    )
    showLabelBackdrop: bool | None = Field(
        default=None, description="If true, draw a background behind the tick labels."
    )
    stepSize: int | None = None
    textStrokeColor: Color | None = Field(
        default=None, description="The color of the stroke around the text."
    )
    textStrokeWidth: int | None = Field(
        default=None, description="Stroke width around the text."
    )
    z: int | None = Field(
        default=None,
        description="z-index of tick layer. Useful when ticks are drawn on chart area. Values <= 0 are drawn under datasets, > 0 on top.",
    )


class Grid(BaseModel):
    borderColor: Color | None = Field(
        default=None, description="The color of the border line."
    )
    borderWidth: float | None = Field(
        default=None, description="The width of the border line."
    )
    borderDash: list[float] | None = Field(
        default=None, description="Length and spacing of dashes on grid lines. See MDN."
    )
    borderDashOffset: float | None = Field(
        default=None, description="Offset for line dashes. See MDN."
    )
    circular: bool | None = Field(
        default=None,
        description="If true, gridlines are circular (on radar chart only).",
    )
    color: Color | None = Field(
        default=None,
        description="The color of the grid lines. If specified as an array, the first color applies to the first grid line, the second to the second grid line, and so on.",
    )
    display: bool | None = Field(
        default=None, description="If false, do not display grid lines for this axis."
    )
    drawBorder: bool | None = Field(
        default=None,
        description="If true, draw a border at the edge between the axis and the chart area.",
    )
    drawOnChartArea: bool | None = Field(
        default=None,
        description="If true, draw lines on the chart area inside the axis lines. This is useful when there are multiple axes and you need to control which grid lines are drawn.",
    )
    drawTicks: bool | None = Field(
        default=None,
        description="If true, draw lines beside the ticks in the axis area beside the chart.",
    )
    lineWidth: float | None = Field(
        default=None, description="Stroke width of grid lines."
    )
    offset: bool | None = Field(
        default=None,
        description="If true, grid lines will be shifted to be between labels. This is set to true for a bar chart by default.",
    )
    tickBorderDash: list[float] | None = Field(
        default=None,
        description="Length and spacing of the tick mark line. If not set, defaults to the grid line borderDash value.",
    )
    tickBorderDashOffset: float | None = Field(
        default=None,
        description="Offset for the line dash of the tick mark. If unset, defaults to the grid line borderDashOffset value",
    )
    tickColor: Color | None = Field(
        default=None,
        description="Color of the tick line. If unset, defaults to the grid line color.",
    )
    tickLength: int | None = Field(
        default=None,
        description="Length in pixels that the grid lines will draw into the axis area.",
    )
    tickWidth: int | None = Field(
        default=None,
        description="Width of the tick mark in pixels. If unset, defaults to the grid line width.",
    )
    z: int | None = Field(
        default=None,
        description="z-index of gridline layer. Values <= 0 are drawn under datasets, > 0 on top.",
    )


class CartesianTicks(Ticks):
    """
    Namespace: options.scales[scaleId].ticks
    """

    align: str | None = Field(
        default=None,
        description="The tick alignment along the axis. Can be 'start', 'center', or 'end'.",
    )
    crossAlign: str | None = Field(
        default=None,
        description="The tick alignment perpendicular to the axis. Can be 'near', 'center', or 'far'. See Tick Alignment",
    )
    sampleSize: int | None = Field(
        default=None,
        description="The number of ticks to examine when deciding how many labels will fit. Setting a smaller value will be faster, but may be less accurate when there is large variability in label length.",
    )
    autoSkip: bool | None = Field(
        default=None,
        description="If true, automatically calculates how many labels can be shown and hides labels accordingly. Labels will be rotated up to maxRotation before skipping any. Turn autoSkip off to show all labels no matter what.",
    )
    autoSkipPadding: int | None = Field(
        default=None,
        description="Padding between the ticks on the horizontal axis when autoSkip is enabled.",
    )
    includeBounds: bool | None = Field(
        default=None,
        description='Should the defined min and max values be presented as ticks even if they are not "nice".',
    )
    labelOffset: int | None = Field(
        default=None,
        description="Distance in pixels to offset the label from the centre point of the tick (in the x-direction for the horizontal axis, and the y-direction for the vertical axis).",
    )
    minRotation: int | None = Field(
        default=None, description="Minimum rotation for tick labels, in degrees."
    )
    maxRotation: int | None = Field(
        default=None, description="Maximum rotation for tick labels, in degrees."
    )
    mirror: bool | None = Field(
        default=None,
        description="Flips tick labels around axis, displaying the labels inside the chart instead of outside.",
    )
    padding: int | None = Field(
        default=None, description="Padding between the tick label and the axis."
    )
    showLabelBackdrop: bool | None = Field(
        default=None, description="If true, draw a background behind the tick labels."
    )
    textStrokeColor: Color | None = Field(
        default=None, description="The color of the stroke around the text."
    )
    textStrokeWidth: int | None = Field(
        default=None, description="Stroke width around the text."
    )
    z: int | None = Field(
        default=None,
        description="z-index of tick layer. Useful when ticks are drawn on chart area. Values <= 0 are drawn under datasets, > 0 on top.",
    )


class ScaleOptions(BaseModel):
    display: bool | None = True
    beginAtZero: bool | None = None
    title: Title | None = None
    min: int | None = None
    max: int | None = None
    stacked: bool | None = None
    position: str | None = None
    offset: bool = True
    ticks: Ticks | CartesianTicks | None = None
    barThickness: int | None = None
    labels: Any | None = None
    grid: Grid | None = None
    type: str | None = None


class Scales(BaseModel):
    y: ScaleOptions | None = None
    x: ScaleOptions | None = None
    # Added for datalabels plugin
    xAxes: list[ScaleOptions] | None = None
    yAxes: list[ScaleOptions] | None = None
    # x1, y1 represent additional
    y1: ScaleOptions | None = None
    x1: ScaleOptions | None = None
    grid: Grid | None = None


class Interaction(BaseModel):
    intersect: bool | None = None  # False for stacked charts
    mode: str | None = Field(
        None,
        description="Sets which elements appear in the interaction. See Interaction Modes for details.",
    )
    axis: str | None = "x"
    includeInvisible: bool | None = False


class Options(BaseModel):
    responsive: bool | None = Field(
        True,
        description="Resizes the chart canvas when its container does (important note...).",
    )
    maintainAspectRatio: bool | None = Field(
        True,
        description="Maintain the original canvas aspect ratio (width / height) when resizing.",
    )
    aspectRatio: number | Function | None = Field(
        2,
        description="Canvas aspect ratio (i.e. width / height, a value of 1 representing a square canvas). Note that this option is ignored if the height is explicitly defined either as attribute or via the style.",
    )
    onResize: Function | None = Field(
        None,
        description="Called when a resize occurs. Gets passed two arguments: the chart instance and the new size.",
    )
    resizeDelay: number | None = Field(
        0,
        description="Delay the resize update by give amount of milliseconds. This can ease the resize process by debouncing update of the elements.",
    )

    plugins: Plugins | None = None
    scales: Scales | None = None
    elements: Elements | None = None
    indexAxis: str | None = None
    interaction: Interaction | None = None

    # Bar chart option
    barPercentage: float | None = None
    layout: Layout | None = None
    stacked: bool | None = False

    # Doughnut chart
    cutout: str | None = None


class Config(BaseModel):
    type: ChartType | str = ChartType.line
    data: Data | None = None
    options: Options | None = None


if __name__ == "__main__":
    Layout().model_dump_json()
    Dataset().model_dump_json()
    Data(labels=["1", "2", "3"], datasets=[Dataset()]).model_dump_json()
    Font().model_dump_json()
    Title().model_dump_json()
    LegendLabels().model_dump_json()
    LegendTitle().model_dump_json()
    Legend().model_dump_json()
    DataLabelsPlugin().model_dump_json()
    TooltipCallbacks().model_dump_json()
    Tooltip().model_dump_json()
    Plugins().model_dump_json()
    Ticks().model_dump_json()
    Grid().model_dump_json()
    ScaleOptions().model_dump_json()
    Scales().model_dump_json()
    Interaction().model_dump_json()
    Options().model_dump_json()
    Config().model_dump_json()
