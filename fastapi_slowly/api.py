# fastapi_slowly/api.py

from .version import get_version
from .web import URL_ISS

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
import requests


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    html = f"""
    <h1>FastAPI - Slowly: HTML Response</h1>
    <p>version {get_version()}</p>
    """
    return html


@app.get("/hello")
async def hello_iss():
    response = requests.get(URL_ISS)
    context = {
        "API version": get_version(),
        "Hello from ISS": response.json(),
    }
    return context

@app.get("/timetravel/{branch}")
async def git_time_travel(branch: str, endpoint: str|None = None):
    print(branch, endpoint)
    import os
    os.system(f"git checkout {branch} && sleep 2")
    return RedirectResponse(f"/{endpoint or ''}")


