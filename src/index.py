import requests
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
async def root():
    return "Hello World!"


@app.get("/bing/daily")
async def bing():
    response = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1")
    image_url = "https://www.bing.com" + response.json()["images"][0]["url"]
    return RedirectResponse(url=image_url)