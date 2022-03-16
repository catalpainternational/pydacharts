from pydacharts.models import (
    CartesianTicks,
    Font,
    Options,
    ScaleOptions,
    Scales,
    Plugins,
    Data,
    Dataset,
    Config,
    ChartType,
)

from pydacharts.plugins.datalabels import DataLabelsPlugin, Label


class CenteredDataLabel(DataLabelsPlugin):
    offset: int = 25
    font: Font = Font(size=16, weight="bold")


class OffsetTicks(CartesianTicks):
    mirror = True
    z = 100
    padding = 10


class RightAlignedScale(ScaleOptions):
    position: str = "right"
    ticks: OffsetTicks = OffsetTicks(mirror=True, display=True, z=100, padding=-10)


class Plugins_(Plugins):
    datalabels: DataLabelsPlugin


def test_datalabels() -> Config:

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
                labels=["${0:.0f} M".format(n[1] / 1e6) for n in _data],
            ),
        ),
        plugins=Plugins_(
            datalabels=CenteredDataLabel(
                labels=dict(
                    name=Label(anchor=Label.Anchor.start, align=Label.Align.end, clamp=True),
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


"""

function App() {
  const data = {
    labels: ["ACCESSIBILITY", "FOR ALL AGES", "VARIETY"],
    datasets: [
      {

        borderColor: [
          "rgba(255,99,132,1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)"
        ],
        borderWidth: 1
      }
    ]
  };
  return (
    <div className="App" style={{ width: 500 }}>
      <HorizontalBar data={data} width={50} height={35} options={options} />
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
"""
