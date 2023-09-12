# fastapi_slowly/api.py

from .version import get_version

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import requests

app = FastAPI()


@app.get("/timetravel/{branch}")
async def git_time_travel(branch: str, endpoint: str|None = None):
    print(branch, endpoint)
    import os
    os.system(f"git checkout {branch}")
    return RedirectResponse(f"/{endpoint or ''}")


@app.get("/")
async def root():
    iss_url = "https://api.wheretheiss.at/v1/satellites/25544"
    response = requests.get(iss_url)
    return {
        "API version": get_version(),
        "Hello from ISS": response.json(),
    }