from pydacharts.models import ChartType, Config, Data, Dataset, PieData, PieDataSet


def test_example() -> Config:
    """
    Return a chartjs "config" object for sip dataset
    charting
    """
    return Config(
        type="bar",
        data=Data(
            labels=["Green is nice", "Red is angry", "Blue is calming"],
            datasets=[Dataset(backgroundColor=["green", "red", "blue"], data=[1, 2, 3], label="We love colors")],
        ),
    )


def test_pie_chart() -> Config:
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
