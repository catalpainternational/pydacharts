import pytest

from pydacharts.elements import ArcElements, BarsElements, LinesElements, PointsElements


@pytest.mark.parametrize(
    "element", [ArcElements, LinesElements, PointsElements, BarsElements]
)
def test_instances(element):
    element().model_dump_json()
