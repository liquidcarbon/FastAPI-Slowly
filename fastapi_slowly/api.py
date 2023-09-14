# fastapi_slowly/api.py

from .version import get_version

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from markupsafe import Markup

import os
import requests


app = FastAPI()
app.mount(
    path="/static",
    app=StaticFiles(directory="static"),
    name="static",
)

templates = Jinja2Templates(directory="static/templates")


@app.get("/timetravel/{branch}")
async def git_time_travel(branch: str, endpoint: str | None = None):
    """Time travel using git branches."""

    os.system(f"git checkout {branch} && sleep 2")
    return RedirectResponse(f"/{endpoint or ''}")


@app.get("/hello")
async def hello_iss():
    """Request to ISS API."""

    iss_url = "https://api.wheretheiss.at/v1/satellites/25544"
    response = requests.get(iss_url)
    return {
        "API version": get_version(),
        "Hello from ISS": response.json(),
    }


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Home page."""

    context = {
        "request": request,
        "content": Markup(f"<p>Version: {get_version()}</p>"),
    }
    return templates.TemplateResponse(name="base.html.jinja", context=context)
