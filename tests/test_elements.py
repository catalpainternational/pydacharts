import pytest

from pydacharts.elements import ArcElements, LinesElements, PointsElements, BarsElements


@pytest.mark.parametrize("element", [ArcElements, LinesElements, PointsElements, BarsElements])
def test_instances(element):
    element().model_dump_json()
