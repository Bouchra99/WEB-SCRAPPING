from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory = "templates")


@app.get("/")
async def root(request : Request):
    return templates.TemplateResponse("home.html",{"request" : request , "name" : "Bouchra MHAMDI"})

@app.get("/main")
async def main():
    return 12