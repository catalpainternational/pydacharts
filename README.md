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
uv .venv/bin/activate
cd serve
fastapi run
```

go to localhost:8000

## Dev

Linting is done with ruff & mypy, testing with pytest. Expected output is like this:

```sh
(pydacharts) josh@carbonmint:~/github/catalpainternational/pydacharts$ uv run mypy .
Success: no issues found in 25 source files

(pydacharts) josh@carbonmint:~/github/catalpainternational/pydacharts$ uv run ruff check --fix .
All checks passed!

(pydacharts) josh@carbonmint:~/github/catalpainternational/pydacharts$ uv run pytest
===================================================================================================================== test session starts =====================================================================================================================
platform linux -- Python 3.11.10, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/josh/github/catalpainternational/pydacharts
configfile: pyproject.toml
plugins: cov-5.0.0, anyio-4.6.0
collected 41 items                                                                                                                                                                                                                                            

tests/test_bar.py .....                                                                                                                                                                                                                                 [ 12%]
tests/test_chart_examples.py ..                                                                                                                                                                                                                         [ 17%]
tests/test_chart_utils.py ....                                                                                                                                                                                                                          [ 26%]
tests/test_datalabels.py .                                                                                                                                                                                                                              [ 29%]
tests/test_elements.py ....                                                                                                                                                                                                                             [ 39%]
tests/test_line.py ....                                                                                                                                                                                                                                 [ 48%]
tests/test_models.py ..................                                                                                                                                                                                                                 [ 92%]
tests/test_options.py .                                                                                                                                                                                                                                 [ 95%]
tests/test_other.py .                                                                                                                                                                                                                                   [ 97%]
tests/test_pie.py .                                                                                                                                                                                                                                     [100%]

===================================================================================================================== 41 passed in 0.37s ======================================================================================================================
```

### Building

Update the `version` field in `pyproject.toml`
Create a git tag same as the version


```bash
uv build
uv publish --token pypi-YOURTOKENHERE
```
