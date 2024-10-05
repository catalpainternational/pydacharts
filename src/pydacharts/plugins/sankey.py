from pydantic import BaseModel

from pydacharts.models import Config


class SankeyDatasetData(BaseModel):
    from_: str
    to: str
    flow: int


class SankeyDataSet(BaseModel):
    data: list[SankeyDatasetData]
    colorMode: str = "gradient"
    labels: dict[str, str] | None
    priority: dict[str, int] | None


class SankeyData(BaseModel):
    datasets: list[SankeyDataSet]


class Sankey(Config):
    type: str = "sankey"
    data: SankeyData  # type: ignore

    def model_dump_json(self, *args, **kwargs):
        """
        Hack to make python -> json keyword conversion
        """
        data = super().model_dump_json(*args, **kwargs)
        data = data.replace('"from_":', '"from":')
        return data
