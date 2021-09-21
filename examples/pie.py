import calendar
from pydacharts.charts import Line

from pydacharts.color import ChartColor, ChartColorTransparent
from pydacharts.models import (
    ChartType,
    Config,
    PieData,
    PieDataSet,
)
from random import randint


def pie():

    return Config(
        type=ChartType.pie,
        data=PieData(
            labels=["Red", "Orange", "Yellow", "Green", "Blue"],
            datasets=[
                PieDataSet(
                    label="My First Dataset",
                    data=[65, 59, 80, 81, 56],
                    fill=False,
                    backgroundColor=["Red", "Orange", "Yellow", "Green", "Blue"],
                )
            ],
        ),
    )
