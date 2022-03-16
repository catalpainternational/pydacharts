from pydacharts.models import (
    ChartType,
    Config,
    PieData,
    PieDataSet,
)


def test_pie() -> Config:

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
