import pytest

from pydacharts.chart_utils import (
    BarChartOptions,
    DoughnutChartOptions,
    HorizontalBarChartStackedOptions,
    PyramidChartOptions,
)


@pytest.mark.parametrize(
    "element",
    [
        HorizontalBarChartStackedOptions,
        DoughnutChartOptions,
        BarChartOptions,
        PyramidChartOptions,
    ],
)
def test_chart_utils(element):
    element().model_dump_json(exclude_none=True, indent=1)
