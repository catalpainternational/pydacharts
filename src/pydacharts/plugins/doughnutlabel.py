from pydantic import BaseModel

from pydacharts.models import Font, RgbStr


class Label(BaseModel):
    text: str
    font: Font | None
    color: RgbStr | None


class DoughnutLabel(BaseModel):
    labels: list[Label]
