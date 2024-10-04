from typing import Union, Optional, List, Literal, Dict
from pydantic import BaseModel, Field
from pydacharts.chartjs_types import PointStyle, number, Color


class PointsElements(BaseModel):
    radius: Optional[number] = Field(None, description="Point radius.")
    pointStyle: Optional[PointStyle] = Field(None, description="Point style.")
    rotation: Optional[number] = Field(None, description="Point rotation (in degrees).")
    backgroundColor: Optional[Color] = Field(None, description="Point fill color.")
    borderWidth: Optional[number] = Field(None, description="Point stroke width.")
    borderColor: Optional[Color] = Field(None, description="Point stroke color.")
    hitRadius: Optional[number] = Field(
        None, description="Extra radius added to point radius for hit detection."
    )
    hoverRadius: Optional[number] = Field(
        None, description="Point radius when hovered."
    )
    hoverBorderWidth: Optional[number] = Field(
        None, description="Stroke width when hovered."
    )


class LinesElements(BaseModel):
    tension: Optional[number] = Field(
        None, description="Bézier curve tension (0 for no Bézier curves)."
    )
    backgroundColor: Optional[Color] = Field(None, description="Line fill color.")
    borderWidth: Optional[number] = Field(None, description="Line stroke width.")
    borderColor: Optional[Color] = Field(None, description="Line stroke color.")
    borderCapStyle: Optional[str] = Field(None, description="Line cap style. See MDN")
    borderDash: Optional[List[number]] = Field(None, description="Line dash. See MDN")
    borderDashOffset: Optional[number] = Field(
        None, description="Line dash offset. See MDN"
    )
    borderJoinStyle: Optional[Literal["round", "bevel", "miter"]] = Field(
        None, description="Line join style. See MDN"
    )
    capBezierPoints: Optional[bool] = Field(
        None,
        description="true to keep Bézier control inside the chart, false for no restriction.",
    )
    cubicInterpolationMode: Optional[str] = Field(
        None, description="Interpolation mode to apply. See more..."
    )
    fill: Optional[Union[bool, str]] = Field(
        None, description="How to fill the area under the line. See area charts."
    )
    stepped: Optional[bool] = Field(
        None,
        description="true to show the line as a stepped line (tension will be ignored).",
    )


class BarsElements(BaseModel):
    """
    Bar Configuration
    Bar elements are used to represent the bars in a bar chart.
    Namespace: options.elements.bar, global bar options: Chart.defaults.elements.bar.
    """

    backgroundColor: Optional[Color] = Field(None, description="Bar fill color.")
    borderWidth: Optional[number] = Field(None, description="Bar stroke width.")
    borderColor: Optional[Color] = Field(None, description="Bar stroke color.")
    borderSkipped: Optional[
        Literal["start", "end", "middle", "bottom", "left", "top", "right", False]
    ] = Field(
        None,
        description="Skipped (excluded) border: 'start', 'end', 'middle', 'bottom', 'left', 'top', 'right' or false.",
    )
    borderRadius: Optional[Union[number, Dict]] = Field(
        None, description="The bar border radius (in pixels)."
    )
    inflateAmount: Optional[Union[number, Literal["auto"]]] = Field(
        None,
        description="The amount of pixels to inflate the bar rectangle(s) when drawing.",
    )
    pointStyle: Optional[PointStyle] = Field(
        None, description="Style of the point for legend."
    )


class ArcElements(BaseModel):
    """
    Arc Configuration
    Arcs are used in the polar area, doughnut and pie charts.
    Namespace: options.elements.arc, global arc options: Chart.defaults.elements.arc.
    """

    angle: Optional[number] = Field(None, description="Arc angle to cover.")
    backgroundColor: Optional[Color] = Field(None, description="Arc fill color.")
    borderAlign: Optional[Literal["center", "inner"]] = Field(
        None, description="Arc stroke alignment."
    )
    borderColor: Optional[Color] = Field(None, description="Arc stroke color.")
    borderJoinStyle: Optional[Literal["round", "bevel", "miter", "bevel", "round"]] = (
        Field(None, description="Line join style")
    )
    borderWidth: Optional[number] = Field(None, description="Arc stroke width.")


class Elements(BaseModel):
    """
    arc, lines, points, and bars.
    """

    arc: Optional[ArcElements] = None
    lines: Optional[LinesElements] = None
    points: Optional[PointsElements] = None
    bars: Optional[BarsElements] = None


if __name__ == "__main__":
    arc = ArcElements()
    lines = LinesElements()
    points = PointsElements()
    bars = BarsElements()

    print(Elements(arc=arc, lines=lines, points=points, bars=bars).json())
