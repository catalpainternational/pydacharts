from pydacharts.plugins import sankey as s


def test_sankey() -> s.Sankey:
    """
    Intended to work together with the "sankey" charts plugin
    """

    return s.Sankey(
        data=s.SankeyData(
            datasets=[
                s.SankeyDataSet(
                    data=[
                        s.SankeyDatasetData(from_="a", to="b", flow=10),
                        s.SankeyDatasetData(from_="a", to="c", flow=5),
                        s.SankeyDatasetData(from_="b", to="c", flow=2),
                        s.SankeyDatasetData(from_="b", to="d", flow=3),
                    ],
                    priority={"a": 1, "b": 2, "c": 3},
                    labels={"a": "Label 1", "b": "Label 2", "c": "Label 3"},
                )
            ]
        )
    )
