from flask import Flask, render_template
from .serve_data import config

app = Flask(__name__)


@app.route("/")
def hello_world():
    config_json = config().model_dump_json(exclude_none=True, indent=2)
    return render_template(
        "chart_datalabels.html",
        config=config_json,
    )
