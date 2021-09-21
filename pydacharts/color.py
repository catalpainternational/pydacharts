from enum import Enum


class ChartColor(str, Enum):
    RED = "rgb(255, 99, 132)"
    ORANGE = "rgb(255, 159, 64)"
    YELLOW = "rgb(255, 205, 86)"
    GREEN = "rgb(75, 192, 192)"
    BLUE = "rgb(54, 162, 235)"
    PURPLE = "rgb(153, 102, 255)"
    GREY = "rgb(201, 203, 207)"
    WHITE = "rgb(255,255,255)"
    BLACK = "rgb(0,0,0)"


class ChartColorTransparent(str, Enum):
    RED = "rgba(255, 99, 132, 0.5)"
    ORANGE = "rgba(255, 159, 64, 0.5)"
    YELLOW = "rgba(255, 205, 86, 0.5)"
    GREEN = "rgba(75, 192, 192, 0.5)"
    BLUE = "rgba(54, 162, 235, 0.5)"
    PURPLE = "rgba(153, 102, 255, 0.5)"
    GREY = "rgba(201, 203, 207, 0.5)"
