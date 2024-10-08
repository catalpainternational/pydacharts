from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydacharts.models import Config

from .serve_data import config

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    config_json = config().model_dump_json(exclude_none=True, indent=2)
    return templates.TemplateResponse(
        request=request, name="chart_datalabels.html", context={"config": config_json}
    )


@app.get("/chart", response_model=Config, response_model_exclude_none=True)
async def read_chart(request: Request):
    return config()
