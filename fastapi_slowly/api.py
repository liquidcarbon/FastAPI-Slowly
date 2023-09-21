# fastapi_slowly/api.py

from .version import get_version
from .web import Templates, URLS

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse

import csv
import os
import requests


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    return Templates().render()


@app.get("/hello")
async def hello_iss():
    response = requests.get(URLS.ISS)
    context = {
        "API version": get_version(),
        "Hello from ISS": response.json(),
    }
    return context


@app.get("/timetravel/{branch}")
async def git_time_travel(branch: str, endpoint: str | None = None):
    os.system(f"git checkout {branch} && sleep 2")
    return RedirectResponse(f"/{endpoint or ''}")


@app.get("/element/{Z}", response_class=HTMLResponse)
async def get_element(Z: int):
    response = requests.get(URLS.PERIODIC_TABLE_CSV)
    elements = csv.reader(response.text.splitlines(), delimiter=",")

    for z, line in enumerate(elements):
        if z == 0:
            header = line
        if z == Z:
            element_info = [(key, value) for key, value in zip(header, line)]
            break

    content = Templates("table.html").render(
        header=["keys", "values"],
        data=element_info,
        # table_caption="What a great element!",
        # dt_order="[[0, 'asc']]",  # default: unsorted
        div_classes="col-5",
    )

    return Templates().render(content=content)
