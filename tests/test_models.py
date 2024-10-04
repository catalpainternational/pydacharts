from pydacharts.models import (
    Layout,
    Interaction,
    Scales,
    ScaleOptions,
    Ticks,
    Tooltip,
    TooltipCallbacks,
    Legend,
    LegendTitle,
    LegendLabels,
    Title,
    Dataset,
    Data,
    Font,
    Plugins,
    Grid,
    Options,
    Config,
)
from pydacharts.plugins.datalabels import DataLabelsPlugin

import pytest


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
