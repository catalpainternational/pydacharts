from typing import Callable
from flask import Flask, render_template

import examples

app = Flask(__name__)
from pydacharts.models import Config


@app.route("/")
def hello_world():
    config = examples.datalabels  # type: Callable[[], Config]
    config_json = config().json(exclude_none=True, indent=2)
    return render_template(
        "chart_datalabels.html",
        config=config_json,
    )



@app.route("/example/datalabels")
def get_datalabels_chart():
    config = examples.datalabels  # type: Callable[[], Config]
    config_json = config().json(exclude_none=True, indent=2)
    return render_template(
        "chart_datalabels.html",
        config=config_json,
    )


@app.route("/example/<name>")
def get_chart(name):
    config = getattr(examples, name)()  # type: Config
    config_json = config.json(exclude_none=True, indent=2)
    return render_template(
        "chart.html",
        config=config_json,
    )
