# fastapi_slowly/api.py

from .version import get_version
from .web import URL_ISS, URL_PERIODIC_TABLE_CSV

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from markupsafe import Markup

import csv
import os
import requests


app = FastAPI()
app.mount(
    path="/static",
    app=StaticFiles(directory="static"),
    name="static",
)

templates = Jinja2Templates(directory="static/templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Home page."""

    context = {
        "request": request,
        "version": Markup(f"<p>Version: {get_version()}</p>"),
    }
    return templates.TemplateResponse(name="base.html.jinja", context=context)


@app.get("/hello")
async def hello_iss():
    """Request to ISS API."""

    response = requests.get(URL_ISS)
    return {
        "API version": get_version(),
        "Hello from ISS": response.json(),
    }


@app.get("/timetravel/{branch}")
async def git_time_travel(branch: str, endpoint: str | None = None):
    """Time travel using git branches."""

    os.system(f"git checkout {branch} && sleep 2")
    return RedirectResponse(f"/{endpoint or ''}")


@app.get("/element/{Z}", response_class=HTMLResponse)
async def get_element(request: Request, Z: int):
    """Get information about a chemical element by atomic number (Z)."""

    response = requests.get(URL_PERIODIC_TABLE_CSV)
    elements = csv.reader(response.text.splitlines(), delimiter=",")

    for z, line in enumerate(elements):
        if z == 0:
            header = line
        if z == Z:
            element_info = line
            break

    element_html = "<br>".join(
        [key + ": " + value for key, value in zip(header, element_info)]
    )

    context = {
        "request": request,
        "content": Markup(element_html),
        "version": Markup(f"<p>Version: {get_version()}</p>"),
    }
    return templates.TemplateResponse(name="base.html.jinja", context=context)
