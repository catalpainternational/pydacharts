# pydacharts

Pydantic :heart: chartjs
This is a code generator for [ChartJS](https://www.chartjs.org) configuration JSON.

## Set Up

1. Pip install the package with `pip install pydacharts`, `uv add pydacharts`, or clone the repo
2. Use the class generator to write a "config" file. One simple example

```py
from pydacharts.models import Config, Data, Dataset

def spending_by_year_chartjs() -> Config:
    """
    Return a chartjs "config" object for sip dataset
    charting
    """
    return Config(
        type="bar",
        data=Data(
            labels=["Green is nice", "Red is angry", "Blue is calming"],
            datasets=[Dataset(
                backgroundColor = ["green", "red", "blue"],
                data = [1,2,3],
                label = "We love colors"
            )]
        )
    )
```

(This example should work standalone)

For running examples

### Run Examples

```bash
uv sync --extra serve
cd serve
flask run
```

go to localhost:5000

### Building

Update the `version` field in `pyproject.toml`
Create a git tag same as the version


```bash
uv build
uv publish --token pypi-YOURTOKENHERE
```
