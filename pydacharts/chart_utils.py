from typing import Optional, Union

from pydacharts.chartjs_types import Font, Function, PaddingObject, number
from pydacharts.elements import BarsElements
from pydacharts.models import (
    DataLabelsPlugin,
    Elements,
    Grid,
    Layout,
    Legend,
    Options,
    Plugins,
    ScaleOptions,
    Scales,
    Ticks,
    Title,
    Tooltip,
    TooltipCallbacks,
)


def chart_options() -> Options:
    return Options(
        responsive=True,
        scales=Scales(
            y=ScaleOptions(grid=Grid(display=True), ticks=Ticks(font=Font(size=14))),
            x=ScaleOptions(grid=Grid(display=False)),
        ),
        plugins=Plugins(
            legend=Legend(display=False),
            tooltip=Tooltip(position="cursor", enabled=False, external="externalTooltipHandler"),
        ),
    )


class BarChartOptions(Options):
    barPercentage: Optional[float] = 0.6
    aspectRatio: Optional[Union[number, Function]] = "aspectRatioFunction"
    elements: Elements = Elements(bars=BarsElements(borderRadius=10))


class HorizontalBarChartOptions(BarChartOptions):
    indexAxis: Optional[str] = "y"
    plugins: Plugins = Plugins(datalabels=DataLabelsPlugin(align="end", anchor="end"))


class HorizontalBarChartStackedOptions(HorizontalBarChartOptions):
    layout: Layout = Layout(padding=PaddingObject(right=40))
    aspectRatio: Function = "(context) => { return Math.max(2, 10 / context.chart.data.labels.length);"
    scales: Scales = Scales(
        y=ScaleOptions(stacked=True, grid=Grid(display=False)),
        x=ScaleOptions(stacked=True, grid=Grid(display=False)),
    )
    plugins: Plugins = Plugins(
        datalabels=DataLabelsPlugin(
            align="end",
            anchor="end",
            padding=PaddingObject(left=12),
            formatter="(value, ctx) => ctx.chart.$totalizer.totals[ctx.dataIndex]",
            display="(ctx) => ctx.datasetIndex === ctx.chart.$totalizer.utmost",
        )
    )


class PyramidChartOptions(HorizontalBarChartStackedOptions):
    scales: Scales = Scales(
        x=ScaleOptions(
            display=True,
            grid=Grid(display=True),
            ticks=Ticks(beginAtZero=True, callback="(value) => `${Math.abs(value) / 1000}k`;", stepSize=2000),
        ),
    )
    plugins: Plugins = Plugins(
        datalabels=DataLabelsPlugin(display=False),
        tooltip=Tooltip(
            callbacks=TooltipCallbacks(
                label="""
                 (context) => {
                    let label = context.dataset.label || "";
                    let value = context.formattedValue;
                    return `${label ? label + ": " : ""}${value.split("-").join("")}`;
                    """
            )
        ),
    )


class DoughnutChartOptions(Options):
    cutout: str = "80%"
    scales = Scales(
        y=ScaleOptions(display=False, grid=Grid(display=False)),
        x=ScaleOptions(display=False, grid=Grid(display=False)),
    )
    plugins: Plugins = Plugins(title=Title(padding=20, color="#70798C", font=Font(size=20, weight="normal")))


if __name__ == "__main__":
    print(HorizontalBarChartStackedOptions().json(exclude_none=True, indent=1))
    print(DoughnutChartOptions().json(exclude_none=True, indent=1))
    print(BarChartOptions().json(exclude_none=True, indent=1))
    print(PyramidChartOptions().json(exclude_none=True, indent=1))
