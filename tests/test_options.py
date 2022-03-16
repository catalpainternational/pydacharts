import calendar
from random import randint

from pydacharts.color import ChartColor, ChartColorTransparent
from pydacharts.models import ChartType, Config, Data, Dataset, Options, Plugins, ScaleOptions, Scales, Title


def test_center_positioning() -> Config:
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
        plugins=Plugins(title=Title(display=True, text="Axis Center Positioning")),
        scales=Scales(x=ScaleOptions(min=-100, max=100), y=ScaleOptions(min=-100, max=100)),
    )

    return Config(type=ChartType.scatter, data=data, options=options)
