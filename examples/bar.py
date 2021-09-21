import calendar
from random import randint

from pydacharts.color import ChartColor, ChartColorTransparent
from pydacharts.models import (
    ChartType,
    Config,
    Data,
    Dataset,
    Interaction,
    Legend,
    Options,
    Plugins,
    ScaleOptions,
    Scales,
    Title,
)


def vertical_bar():

    bar_data = Data(
        labels=[calendar.month_name[i] for i in range(1, 8)],
        datasets=[
            Dataset(
                label="Dataset 1",
                data=[randint(-100, 100) for i in range(1, 8)],
                borderColor=ChartColor.RED,
                backgroundColor=ChartColorTransparent.RED,
            ),
            Dataset(
                label="Dataset 2",
                data=[randint(-100, 100) for i in range(1, 8)],
                borderColor=ChartColor.BLUE,
                backgroundColor=ChartColorTransparent.BLUE,
            ),
        ],
    )
    options = Options(
        plugins=Plugins(title=Title(text="Chart.js Bar Chart"), legend=Legend(position="top")),
        scales=Scales(y=ScaleOptions(beginAtZero=True)),
    )

    return Config(type=ChartType.bar, data=bar_data, options=options)


def horizontal_bar():

    data = Data(
        labels=[calendar.month_name[i] for i in range(1, 8)],
        datasets=[
            Dataset(
                label="Dataset 1",
                data=[randint(-100, 100) for i in range(1, 8)],
                borderColor=ChartColor.RED,
                backgroundColor=ChartColorTransparent.RED,
            ),
            Dataset(
                label="Dataset 2",
                data=[randint(-100, 100) for i in range(1, 8)],
                borderColor=ChartColor.BLUE,
                backgroundColor=ChartColorTransparent.BLUE,
            ),
        ],
    )
    options = Options(
        indexAxis="y",
        elements=dict(bar=dict(borderWidth=2)),
        plugins=Plugins(
            legend=Legend(position="right"),
            title=Title(text="Chart.js Horizontal Bar Chart"),
        ),
        scales=Scales(x=ScaleOptions(stacked=True), y=ScaleOptions(stacked=True)),
    )

    return Config(type=ChartType.bar, data=data, options=options)


def stacked_bar():

    data = Data(
        labels=[calendar.month_name[i] for i in range(1, 8)],
        datasets=[
            Dataset(
                label="Dataset 1",
                data=[randint(-100, 100) for i in range(1, 8)],
                borderColor=ChartColor.RED,
                backgroundColor=ChartColor.RED,
                stack="Stack 0",
            ),
            Dataset(
                label="Dataset 2",
                data=[randint(-100, 100) for i in range(1, 8)],
                borderColor=ChartColor.BLUE,
                backgroundColor=ChartColor.BLUE,
                stack="Stack 0",
            ),
            Dataset(
                label="Dataset 3",
                data=[randint(-100, 100) for i in range(1, 8)],
                borderColor=ChartColor.GREEN,
                backgroundColor=ChartColor.GREEN,
                stack="Stack 1",
            ),
        ],
    )

    options = Options(
        plugins=Plugins(title=Title(display=True, text="Charts.js Bar Chart - Grouped")),
        interaction=Interaction(intersect=False),
        scales=Scales(x=ScaleOptions(stacked=True), y=ScaleOptions(stacked=True)),
    )

    return Config(type=ChartType.bar, options=options, data=data)


def floating_bar():

    data = Data(
        labels=[calendar.month_name[i] for i in range(1, 8)],
        datasets=[
            Dataset(
                label="Dataset 1",
                data=[[randint(-100, 100), randint(-100, 100)] for i in range(1, 8)],
                backgroundColor=ChartColor.RED,
            ),
            Dataset(
                label="Dataset 2",
                data=[[randint(-100, 100), randint(-100, 100)] for i in range(1, 8)],
                backgroundColor=ChartColor.BLUE,
            ),
        ],
    )

    options = Options(
        plugins=Plugins(
            legend=Legend(position="top"),
            title=Title(display=True, text="Chart.js Floating Bar Chart"),
        ),
    )

    return Config(type=ChartType.bar, options=options, data=data)


def rounded_bar():

    data = Data(
        labels=[calendar.month_name[i] for i in range(1, 8)],
        datasets=[
            Dataset(
                label="Fully Rounded",
                data=[randint(-100, 100) for i in range(1, 8)],
                borderColor=ChartColor.BLUE,
                backgroundColor=ChartColorTransparent.BLUE,
                borderWidth=2,
                borderRadius=100,
                borderSkipped=False,
            ),
            Dataset(
                label="Small Radius",
                data=[randint(-100, 100) for i in range(1, 8)],
                borderColor=ChartColor.RED,
                backgroundColor=ChartColorTransparent.RED,
                borderWidth=2,
                borderRadius=5,
                borderSkipped=False,
            ),
        ],
    )

    options = Options(
        plugins=Plugins(
            legend=Legend(position="top"),
            title=Title(display=True, text="Chart.js Bar Chart"),
        ),
    )

    return Config(type=ChartType.bar, options=options, data=data)
