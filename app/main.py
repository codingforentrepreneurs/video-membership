import json
import pathlib
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from cassandra.cqlengine.management import sync_table
from pydantic.error_wrappers import ValidationError
from . import config, db, utils
from .shortcuts import render
from .users.models import User
from .users.schemas import (
    UserLoginSchema,
    UserSignupSchema
)

BASE_DIR = pathlib.Path(__file__).resolve().parent # app/
TEMPLATE_DIR = BASE_DIR / "templates"

app = FastAPI()
templates = Jinja2Templates(directory=str(TEMPLATE_DIR))

DB_SESSION = None
# settings = config.get_settings()



@app.on_event("startup")
def on_startup():
    # triggered when fastapi starts
    print("hello world")
    global DB_SESSION
    DB_SESSION = db.get_session()
    sync_table(User)


@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    context = {
        "abc": "abc"
    }
    return render(request, "home.html", context)


@app.get("/login", response_class=HTMLResponse)
def login_get_view(request: Request):
    return render(request, "auth/login.html")


@app.post("/login", response_class=HTMLResponse)
def login_post_view(request: Request, 
    email: str=Form(...), 
    password: str = Form(...)):
    raw_data  = {
        "email": email,
        "password": password,
    }
    data, errors = utils.valid_schema_data_or_error(raw_data, UserLoginSchema)
    context = {
                "data": data,
                "errors": errors,
            }
    if len(errors) > 0:
        return render(request, "auth/login.html", context, status_code=400)

    print(data['password'].get_secret_value())
    return render(request, "auth/login.html", context)


@app.get("/signup", response_class=HTMLResponse)
def signup_get_view(request: Request):
    return render(request, "auth/signup.html")


@app.post("/signup", response_class=HTMLResponse)
def signup_post_view(request: Request, 
    email: str=Form(...), 
    password: str = Form(...),
    password_confirm: str = Form(...)
    ):
    raw_data  = {
        "email": email,
        "password": password,
        "password_confirm": password_confirm
    }
    data, errors = utils.valid_schema_data_or_error(raw_data, UserSignupSchema)
    if len(errors) > 0:
        return render(request, "auth/signup.html", context, status_code=400)
    return render(request, "auth/signup.html", {
        "data": data,
        "errors": errors,
    })




@app.get("/users")
def users_list_view():
    q = User.objects.all().limit(10)
    return list(q)