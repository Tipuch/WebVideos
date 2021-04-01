from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse
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
