from typing import Callable
from flask import Flask, render_template
from pydacharts.models import Config

from tests import test_datalabels

app = Flask(__name__)


@app.route("/")
def hello_world():
    config = test_datalabels.test_datalabels  # type: Callable[[], Config]
    config_json = config().json(exclude_none=True, indent=2)
    return render_template(
        "chart_datalabels.html",
        config=config_json,
    )


@app.route("/example/datalabels")
def get_datalabels_chart():
    config = test_datalabels.test_datalabels  # type: Callable[[], Config]
    config_json = config().json(exclude_none=True, indent=2)
    return render_template(
        "chart_datalabels.html",
        config=config_json,
    )
