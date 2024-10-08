import calendar
from random import randint

from pydacharts.color import ChartColor, ChartColorTransparent
from pydacharts.models import (
    ChartType,
    Config,
    Data,
    Dataset,
    Options,
    Plugins,
    ScaleOptions,
    Scales,
    Title,
)


def test_center_positioning():
    labels = [calendar.month_name[i] for i in range(1, 8)]
    dataset1_data = [randint(-100, 100) for i in range(1, 8)]
    dataset2_data = [randint(-100, 100) for i in range(1, 8)]

    data = Data(
        labels=labels,
        datasets=[
            Dataset(
                label="Dataset 1",
                data=dataset1_data,
                borderColor=ChartColor.RED,
                backgroundColor=ChartColorTransparent.RED,
            ),
            Dataset(
                label="Dataset 2",
                data=dataset2_data,
                borderColor=ChartColor.BLUE,
                backgroundColor=ChartColorTransparent.BLUE,
            ),
        ],
    )

    options = Options(
        plugins=Plugins(title=Title(display=True, text="Axis Center Positioning")),
        scales=Scales(
            x=ScaleOptions(min=-100, max=100), y=ScaleOptions(min=-100, max=100)
        ),
    )

    config = Config(type=ChartType.scatter, data=data, options=options)

    # Assertions
    assert config.type == ChartType.scatter
    assert config.data.labels == labels
    assert config.data.datasets[0].label == "Dataset 1"
    assert config.data.datasets[0].data == dataset1_data
    assert config.data.datasets[0].borderColor == ChartColor.RED
    assert config.data.datasets[0].backgroundColor == ChartColorTransparent.RED
    assert config.data.datasets[1].label == "Dataset 2"
    assert config.data.datasets[1].data == dataset2_data
    assert config.data.datasets[1].borderColor == ChartColor.BLUE
    assert config.data.datasets[1].backgroundColor == ChartColorTransparent.BLUE
    assert config.options.plugins.title.display is True
    assert config.options.plugins.title.text == "Axis Center Positioning"
    assert config.options.scales.x.min == -100
    assert config.options.scales.x.max == 100
    assert config.options.scales.y.min == -100
    assert config.options.scales.y.max == 100
