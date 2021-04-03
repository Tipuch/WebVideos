import os

import uvicorn
from b2sdk.v1 import *
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()

app.mount("/css", StaticFiles(directory="./static/dist/css"), name="css")
app.mount("/img", StaticFiles(directory="./static/dist/img"), name="img")
app.mount("/js", StaticFiles(directory="./static/dist/js"), name="js")

templates = Jinja2Templates(directory="./static/dist")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/video", response_class=JSONResponse)
async def get_video():
    info = InMemoryAccountInfo()
    b2_session = B2Session(info)
    application_key_id = os.environ["BACKBLAZE_API_KEY_ID"]
    application_key = os.environ["BACKBLAZE_API_KEY"]
    b2_session.authorize_account("production", application_key_id, application_key)
    download_token = b2_session.get_download_authorization(os.environ["BACKBLAZE_BUCKET_ID"], "video", 3600)

    file_url = b2_session.get_download_url_by_name(os.environ["BACKBLAZE_BUCKET"], "video.mp4")
    download_url = f"{file_url}?Authorization={download_token['authorizationToken']}"

    return {"download_url": download_url}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
