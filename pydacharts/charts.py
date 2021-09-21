from pydacharts.models import ChartType, Config


class Doughnut(Config):
    type: str = ChartType.doughnut


class Bar(Config):
    type: str = ChartType.bar


class Line(Config):
    type: str = ChartType.line
