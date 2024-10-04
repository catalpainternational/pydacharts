from pydacharts.models import ChartType, Config, Data, Dataset, PieData, PieDataSet


def test_example():
    """
    Return a chartjs "config" object for sip dataset
    charting
    """
    config = Config(
        type="bar",
        data=Data(
            labels=["Green is nice", "Red is angry", "Blue is calming"],
            datasets=[
                Dataset(
                    backgroundColor=["green", "red", "blue"],
                    data=[1, 2, 3],
                    label="We love colors",
                )
            ],
        ),
    )

    assert config.type == "bar"
    assert config.data.labels == ["Green is nice", "Red is angry", "Blue is calming"]
    assert config.data.datasets[0].backgroundColor == ["green", "red", "blue"]
    assert config.data.datasets[0].data == [1, 2, 3]
    assert config.data.datasets[0].label == "We love colors"


def test_pie_chart():
    config = Config(
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

    assert config.type == ChartType.pie
    assert config.data.labels == ["Red", "Orange", "Yellow", "Green", "Blue"]
    assert config.data.datasets[0].label == "My First Dataset"
    assert config.data.datasets[0].data == [65, 59, 80, 81, 56]
    assert config.data.datasets[0].fill is False
    assert config.data.datasets[0].backgroundColor == [
        "Red",
        "Orange",
        "Yellow",
        "Green",
        "Blue",
    ]
