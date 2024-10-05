from pydacharts.models import ChartType, Config, PieData, PieDataSet


def test_pie():
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
