from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from httpx import request
from backend.database import tao_tk, dang_nhap

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def trangchu(request: Request):
    return templates.TemplateResponse(name="index.html", context={'request': request})

@app.post("/login")
async def login(user_name: str = Form(...), user_mk: str = Form(...)):
    dnhap = await dang_nhap(user_name, user_mk)
    if  isinstance(dnhap, str):
        return templates.TemplateResponse(name="page-login/login.html", context={'request': request, "error_message": dnhap})
    else:
        return templates.TemplateResponse(name="index.html", context= {'request': request, "login": True, "user_infor": dnhap})
        
    

@app.get("/pages-login")
async def pages_login(request: Request):
    return templates.TemplateResponse(name= "page-login/login.html", context={'request': request})

@app.get("/pages-register")
async def pages_register(request: Request):
    return templates.TemplateResponse(name= "page-login/register.html", context={'request': request})

@app.post("/register")
async def register(user_name: str = Form(...), user_mk: str = Form(...), user_code: str = Form(...)):
    dky = await tao_tk(user_name, user_mk, user_code)
    print(dky)
    return dky
