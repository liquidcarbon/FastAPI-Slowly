# fastapi_slowly/api.py

from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def root():
    iss_url = "https://api.wheretheiss.at/v1/satellites/25544"
    response = requests.get(iss_url)
    return {
        "Hello from ISS": response.json(),
    }