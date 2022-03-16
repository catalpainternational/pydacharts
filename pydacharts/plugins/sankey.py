from typing import Dict, List, Optional

from pydantic import BaseModel

from pydacharts.models import Config


class SankeyDatasetData(BaseModel):
    from_: str
    to: str
    flow: int


class SankeyDataSet(BaseModel):
    data: List[SankeyDatasetData]
    colorMode: str = "gradient"
    labels: Optional[Dict[str, str]]
    priority: Optional[Dict[str, int]]


class SankeyData(BaseModel):
    datasets: List[SankeyDataSet]


class Sankey(Config):
    type: str = "sankey"
    data: SankeyData  # type: ignore

    def json(self, *args, **kwargs):
        """
        Hack to make python -> json keyword conversion
        """
        data = super().json(*args, **kwargs)
        data = data.replace('"from_":', '"from":')
        return data
