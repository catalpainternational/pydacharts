from pydacharts.plugins import sankey as s


def test_sankey():
    """
    Intended to work together with the "sankey" charts plugin
    """
    sankey = s.Sankey(
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

    # Assertions
    assert len(sankey.data.datasets) == 1
    dataset = sankey.data.datasets[0]

    assert len(dataset.data) == 4
    assert dataset.data[0].from_ == "a"
    assert dataset.data[0].to == "b"
    assert dataset.data[0].flow == 10
    assert dataset.data[1].from_ == "a"
    assert dataset.data[1].to == "c"
    assert dataset.data[1].flow == 5
    assert dataset.data[2].from_ == "b"
    assert dataset.data[2].to == "c"
    assert dataset.data[2].flow == 2
    assert dataset.data[3].from_ == "b"
    assert dataset.data[3].to == "d"
    assert dataset.data[3].flow == 3

    assert dataset.priority == {"a": 1, "b": 2, "c": 3}
    assert dataset.labels == {"a": "Label 1", "b": "Label 2", "c": "Label 3"}
