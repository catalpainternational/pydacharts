from pydacharts.models import (
    ChartType,
    Config,
    Data,
    Dataset,
    Options,
    ScaleOptions,
    Scales,
)
from pydacharts.plugins.datalabels import Label
from tests.test_datalabels import CenteredDataLabel, OffsetTicks, PluginsDataLabels


class RightAlignedScale(ScaleOptions):
    position: str = "right"
    ticks: OffsetTicks = OffsetTicks(mirror=True, display=True, z=100, padding=-10)


def config():
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

    return Config(type=ChartType.bar, options=options, data=data)
