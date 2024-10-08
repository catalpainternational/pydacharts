from pydacharts.models import (
    CartesianTicks,
    ChartType,
    Config,
    Data,
    Dataset,
    Font,
    Options,
    Plugins,
    ScaleOptions,
    Scales,
)
from pydacharts.plugins.datalabels import DataLabelsPlugin, Label


class CenteredDataLabel(DataLabelsPlugin):
    offset: int = 25
    font: Font = Font(size=16, weight="bold")


class OffsetTicks(CartesianTicks):
    mirror: bool = True
    z: int = 100
    padding: int = 10


class RightAlignedScale(ScaleOptions):
    position: str = "right"
    ticks: OffsetTicks = OffsetTicks(mirror=True, display=True, z=100, padding=-10)


class PluginsDataLabels(Plugins):
    datalabels: DataLabelsPlugin = DataLabelsPlugin()


def test_datalabels():
    _data = [
        ("World Bank", 3703888321),
        ("European Union", 1596973970),
        ("UK - Foreign, Commonwealth and Development Office", 1373918906),
        ("Asian Development Bank", 1356078649),
        ("U.S. Agency for International Development", 1101991438),
        ("Government of Germany", 981575439),
        ("World Food Programme", 769002439),
        ("Government of France", 613321247),
        ("Korea EximBank", 598375000),
    ]

    options = Options(
        indexAxis="y",
        scales=Scales(
            y=RightAlignedScale(
                labels=[f"${n[1] / 1e6:.0f} M" for n in _data],
            ),
        ),
        plugins=PluginsDataLabels(
            datalabels=CenteredDataLabel(
                labels=dict(
                    name=Label(
                        anchor=Label.Anchor.start, align=Label.Align.end, clamp=True
                    ),
                )
            )
        ),
    )

    ds = Dataset(
        label="Total Commitment",
        data=[n[1] / 1e6 for n in _data],
    )

    data = Data(labels=[n[0] for n in _data], datasets=[ds])

    config = Config(type=ChartType.bar, options=options, data=data)

    # Assertions
    assert config.type == ChartType.bar
    assert config.data.labels == [n[0] for n in _data]
    assert config.data.datasets[0].label == "Total Commitment"
    assert config.data.datasets[0].data == [n[1] / 1e6 for n in _data]
    assert config.options.indexAxis == "y"
    assert config.options.scales.y.position == "right"
    assert config.options.scales.y.ticks.mirror is True
    assert config.options.scales.y.ticks.z == 100
    assert config.options.scales.y.ticks.padding == -10
    assert config.options.plugins.datalabels.offset == 25
    assert config.options.plugins.datalabels.font.size == 16
    assert config.options.plugins.datalabels.font.weight == "bold"
    assert config.options.plugins.datalabels.labels["name"].anchor == Label.Anchor.start
    assert config.options.plugins.datalabels.labels["name"].align == Label.Align.end
    assert config.options.plugins.datalabels.labels["name"].clamp is True
