import pytest

from pydacharts.models import (
    Config,
    Data,
    Dataset,
    Font,
    Grid,
    Interaction,
    Layout,
    Legend,
    LegendLabels,
    LegendTitle,
    Options,
    Plugins,
    ScaleOptions,
    Scales,
    Ticks,
    Title,
    Tooltip,
    TooltipCallbacks,
)
from pydacharts.plugins.datalabels import DataLabelsPlugin


@pytest.mark.parametrize(
    "testcase",
    [
        Layout,
        Font,
        Title,
        LegendLabels,
        LegendTitle,
        Legend,
        DataLabelsPlugin,
        TooltipCallbacks,
        Tooltip,
        Plugins,
        Ticks,
        Grid,
        ScaleOptions,
        Scales,
        Interaction,
        Options,
        Config,
    ],
)
def test_all_models(testcase):
    testcase().model_dump_json()


def test_data_labels():
    Data(labels=["1", "2", "3"], datasets=[Dataset()]).model_dump_json()
