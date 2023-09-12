# fastapi_slowly/api.py

from .version import get_version

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
import requests

app = FastAPI()


@app.get("/timetravel/{branch}")
async def git_time_travel(branch: str, endpoint: str|None = None):
    print(branch, endpoint)
    import os
    os.system(f"git checkout {branch} && sleep 2")
    return RedirectResponse(f"/{endpoint or ''}")


@app.get("/hello")
async def hello_iss():
    iss_url = "https://api.wheretheiss.at/v1/satellites/25544"
    response = requests.get(iss_url)
    return {
        "API version": get_version(),
        "Hello from ISS": response.json(),
    }


@app.get("/")
async def root():
    html = f"""
    <h1>FastAPI - Slowly: HTML Response</h1>
    <p>version {get_version()}</p>
    """
    return HTMLResponse(content=html)
