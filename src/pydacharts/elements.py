from typing import Literal

from pydantic import BaseModel, Field

from pydacharts.chartjs_types import Color, PointStyle, number


class PointsElements(BaseModel):
    radius: number | None = Field(None, description="Point radius.")
    pointStyle: PointStyle | None = Field(None, description="Point style.")
    rotation: number | None = Field(None, description="Point rotation (in degrees).")
    backgroundColor: Color | None = Field(None, description="Point fill color.")
    borderWidth: number | None = Field(None, description="Point stroke width.")
    borderColor: Color | None = Field(None, description="Point stroke color.")
    hitRadius: number | None = Field(
        None, description="Extra radius added to point radius for hit detection."
    )
    hoverRadius: number | None = Field(None, description="Point radius when hovered.")
    hoverBorderWidth: number | None = Field(
        None, description="Stroke width when hovered."
    )


class LinesElements(BaseModel):
    tension: number | None = Field(
        None, description="Bézier curve tension (0 for no Bézier curves)."
    )
    backgroundColor: Color | None = Field(None, description="Line fill color.")
    borderWidth: number | None = Field(None, description="Line stroke width.")
    borderColor: Color | None = Field(None, description="Line stroke color.")
    borderCapStyle: str | None = Field(None, description="Line cap style. See MDN")
    borderDash: list[number] | None = Field(None, description="Line dash. See MDN")
    borderDashOffset: number | None = Field(
        None, description="Line dash offset. See MDN"
    )
    borderJoinStyle: Literal["round", "bevel", "miter"] | None = Field(
        None, description="Line join style. See MDN"
    )
    capBezierPoints: bool | None = Field(
        None,
        description="true to keep Bézier control inside the chart, false for no restriction.",
    )
    cubicInterpolationMode: str | None = Field(
        None, description="Interpolation mode to apply. See more..."
    )
    fill: bool | str | None = Field(
        None, description="How to fill the area under the line. See area charts."
    )
    stepped: bool | None = Field(
        None,
        description="true to show the line as a stepped line (tension will be ignored).",
    )


class BarsElements(BaseModel):
    """
    Bar Configuration
    Bar elements are used to represent the bars in a bar chart.
    Namespace: options.elements.bar, global bar options: Chart.defaults.elements.bar.
    """

    backgroundColor: Color | None = Field(None, description="Bar fill color.")
    borderWidth: number | None = Field(None, description="Bar stroke width.")
    borderColor: Color | None = Field(None, description="Bar stroke color.")
    borderSkipped: (
        Literal["start", "end", "middle", "bottom", "left", "top", "right", False]
        | None
    ) = Field(
        None,
        description="Skipped (excluded) border: 'start', 'end', 'middle', 'bottom', 'left', 'top', 'right' or false.",
    )
    borderRadius: number | dict | None = Field(
        None, description="The bar border radius (in pixels)."
    )
    inflateAmount: number | Literal["auto"] | None = Field(
        None,
        description="The amount of pixels to inflate the bar rectangle(s) when drawing.",
    )
    pointStyle: PointStyle | None = Field(
        None, description="Style of the point for legend."
    )


class ArcElements(BaseModel):
    """
    Arc Configuration
    Arcs are used in the polar area, doughnut and pie charts.
    Namespace: options.elements.arc, global arc options: Chart.defaults.elements.arc.
    """

    angle: number | None = Field(None, description="Arc angle to cover.")
    backgroundColor: Color | None = Field(None, description="Arc fill color.")
    borderAlign: Literal["center", "inner"] | None = Field(
        None, description="Arc stroke alignment."
    )
    borderColor: Color | None = Field(None, description="Arc stroke color.")
    borderJoinStyle: Literal["round", "bevel", "miter", "bevel", "round"] | None = (
        Field(None, description="Line join style")
    )
    borderWidth: number | None = Field(None, description="Arc stroke width.")


class Elements(BaseModel):
    """
    arc, lines, points, and bars.
    """

    arc: ArcElements | None = None
    lines: LinesElements | None = None
    points: PointsElements | None = None
    bars: BarsElements | None = None


if __name__ == "__main__":
    arc = ArcElements()
    lines = LinesElements()
    points = PointsElements()
    bars = BarsElements()

    print(Elements(arc=arc, lines=lines, points=points, bars=bars).json())
