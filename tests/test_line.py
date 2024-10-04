import calendar
from random import randint

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


def test_line():
    config = Config(
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

    assert config.type == ChartType.line
    assert config.data.labels == [calendar.month_name[i] for i in range(1, 8)]
    assert len(config.data.datasets) == 1
    assert config.data.datasets[0].label == "My First Dataset"
    assert config.data.datasets[0].data == [65, 59, 80, 81, 56, 55, 40]
    assert config.data.datasets[0].fill is False
    assert config.data.datasets[0].borderColor == ChartColor.GREEN


def test_multi_axis():
    labels = [calendar.month_name[i] for i in range(1, 8)]
    data1 = [randint(-100, 100) for _ in range(1, 8)]
    data2 = [randint(-100, 100) for _ in range(1, 8)]

    data = LineData(
        labels=labels,
        datasets=[
            LineDataSet(
                label="Dataset 1",
                data=data1,
                borderColor=ChartColor.RED,
                backgroundColor=ChartColorTransparent.RED,
                yAxisID="y",
            ),
            LineDataSet(
                label="Dataset 2",
                data=data2,
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

    config = Config(type="line", data=data, options=options)

    assert config.type == "line"
    assert config.data.labels == labels
    assert len(config.data.datasets) == 2
    assert config.data.datasets[0].data == data1
    assert config.data.datasets[1].data == data2
    assert config.options.plugins.legend.position == "top"
    assert config.options.plugins.title.display is True
    assert config.options.plugins.title.text == "Chart.js Line Chart - Multi Axis"
    assert config.options.interaction.mode == "index"
    assert config.options.interaction.intersect is False
    assert config.options.stacked is False
    assert config.options.scales.y.type == "linear"
    assert config.options.scales.y.display is True
    assert config.options.scales.y.position == "left"
    assert config.options.scales.x.type == "linear"
    assert config.options.scales.x.display is True
    assert config.options.scales.x.position == "right"
    assert config.options.scales.grid.drawOnChartArea is False


def test_stepped_line():
    labels = [calendar.month_name[i] for i in range(1, 8)]
    data_values = [randint(-100, 100) for _ in range(1, 8)]

    data = LineData(
        labels=labels,
        datasets=[
            LineDataSet(
                label="Dataset 1",
                data=data_values,
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

    config = Config(type=ChartType.line, data=data, options=options)

    assert config.type == ChartType.line
    assert config.data.labels == labels
    assert len(config.data.datasets) == 1
    assert config.data.datasets[0].data == data_values
    assert config.data.datasets[0].borderColor == ChartColor.RED
    assert config.data.datasets[0].backgroundColor == ChartColorTransparent.RED
    assert config.data.datasets[0].fill is False
    assert config.data.datasets[0].stepped == StepOption.middle
    assert config.options.interaction.intersect is False
    assert config.options.interaction.axis == "x"
    assert config.options.plugins.title.display is True
    assert config.options.plugins.title.text == "Step chart"


def test_styled_line():
    labels = [calendar.month_name[i] for i in range(1, 8)]
    data1 = [randint(-100, 100) for _ in range(1, 8)]
    data2 = [randint(-100, 100) for _ in range(1, 8)]
    data3 = [randint(-100, 100) for _ in range(1, 8)]

    data = LineData(
        labels=labels,
        datasets=[
            LineDataSet(
                label="Unfilled",
                data=data1,
                borderColor=ChartColor.RED,
                backgroundColor=ChartColorTransparent.RED,
                fill=False,
                stepped=StepOption.middle,
            ),
            LineDataSet(
                label="Dashed",
                data=data2,
                borderColor=ChartColor.BLACK,
                backgroundColor=ChartColorTransparent.BLUE,
                fill=False,
                borderDash=[5, 5],
            ),
            LineDataSet(
                label="Filled",
                data=data3,
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

    config = Config(type=ChartType.line, data=data, options=options)

    assert config.type == ChartType.line
    assert config.data.labels == labels
    assert len(config.data.datasets) == 3
    assert config.data.datasets[0].data == data1
    assert config.data.datasets[0].borderColor == ChartColor.RED
    assert config.data.datasets[0].backgroundColor == ChartColorTransparent.RED
    assert config.data.datasets[0].fill is False
    assert config.data.datasets[0].stepped == StepOption.middle
    assert config.data.datasets[1].data == data2
    assert config.data.datasets[1].borderColor == ChartColor.BLACK
    assert config.data.datasets[1].backgroundColor == ChartColorTransparent.BLUE
    assert config.data.datasets[1].fill is False
    assert config.data.datasets[1].borderDash == [5, 5]
    assert config.data.datasets[2].data == data3
    assert config.data.datasets[2].borderColor == ChartColor.GREEN
    assert config.data.datasets[2].backgroundColor == ChartColorTransparent.GREEN
    assert config.data.datasets[2].fill is True
    assert config.data.datasets[2].stepped is True
    assert config.options.interaction.intersect is False
    assert config.options.interaction.mode == "index"
    assert config.options.plugins.title.display is True
    assert config.options.plugins.title.text == "Chart.js Line Chart"
    assert config.options.scales.y.display is True
    assert config.options.scales.y.title.text == "Value"
    assert config.options.scales.x.display is True
    assert config.options.scales.x.title.text == "Month"
