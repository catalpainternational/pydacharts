import calendar
from pydacharts.charts import Line

from pydacharts.color import ChartColor, ChartColorTransparent
from pydacharts.models import (
    ChartType,
    Config,
    Grid,
    Interaction,
    Legend,
    LineData,
    LineDataSet,
    Options,
    Plugins,
    ScaleOptions,
    Scales,
    StepOption,
    Title,
)
from random import randint


def line():

    return Config(
        type=ChartType.line,
        data=LineData(
            labels=[calendar.month_name[i] for i in range(1, 8)],
            datasets=[
                LineDataSet(
                    label="My First Dataset",
                    data=[65, 59, 80, 81, 56, 55, 40],
                    fill=False,
                    borderColor=ChartColor.GREEN,
                )
            ],
        ),
    )


def multi_axis():

    data = LineData(
        labels=[calendar.month_name[i] for i in range(1, 8)],
        datasets=[
            LineDataSet(
                label="Dataset 1",
                data=[randint(-100, 100) for i in range(1, 8)],
                borderColor=ChartColor.RED,
                backgroundColor=ChartColorTransparent.RED,
                yAxisID="y",
            ),
            LineDataSet(
                label="Dataset 2",
                data=[randint(-100, 100) for i in range(1, 8)],
                borderColor=ChartColor.BLUE,
                backgroundColor=ChartColorTransparent.BLUE,
                yAxisID="y",
            ),
        ],
    )
    options = Options(
        plugins=Plugins(
            legend=Legend(position="top"),
            title=Title(display=True, text="Chart.js Line Chart - Multi Axis"),
        ),
        interaction=Interaction(mode="index", intersect=False),
        stacked=False,
        scales=Scales(
            y=ScaleOptions(type="linear", display="true", position="left"),
            x=ScaleOptions(type="linear", display="true", position="right"),
            grid=Grid(drawOnChartArea=False),
        ),
    )

    return Config(type="line", data=data, options=options)


def stepped_line():

    data = LineData(
        labels=[calendar.month_name[i] for i in range(1, 8)],
        datasets=[
            LineDataSet(
                label="Dataset 1",
                data=[randint(-100, 100) for i in range(1, 8)],
                borderColor=ChartColor.RED,
                backgroundColor=ChartColorTransparent.RED,
                fill=False,
                stepped=StepOption.middle,
            )
        ],
    )

    options = Options(
        interaction=Interaction(intersect=False, axis="x"),
        plugins=Plugins(title=Title(display=True, text="Step chart")),
    )

    return Config(type=ChartType.line, data=data, options=options)


def styled_line():

    data = LineData(
        labels=[calendar.month_name[i] for i in range(1, 8)],
        datasets=[
            LineDataSet(
                label="Unfilled",
                data=[randint(-100, 100) for i in range(1, 8)],
                borderColor=ChartColor.RED,
                backgroundColor=ChartColorTransparent.RED,
                fill=False,
                stepped=StepOption.middle,
            ),
            LineDataSet(
                label="Dashed",
                data=[randint(-100, 100) for i in range(1, 8)],
                borderColor=ChartColor.BLACK,
                backgroundColor=ChartColorTransparent.BLUE,
                fill=False,
                borderDash=[5, 5],
            ),
            LineDataSet(
                label="Filled",
                data=[randint(-100, 100) for i in range(1, 8)],
                borderColor=ChartColor.GREEN,
                backgroundColor=ChartColorTransparent.GREEN,
                fill=True,
                stepped=True,
            ),
        ],
    )

    options = Options(
        interaction=Interaction(intersect=False, mode="index"),
        plugins=Plugins(title=Title(display=True, text="Chart.js Line Chart")),
        scales=Scales(
            y=ScaleOptions(display="true", title=Title(text="Value")),
            x=ScaleOptions(display="true", title=Title(text="Month")),
        ),
    )

    return Line(options=options, data=data)
