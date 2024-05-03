from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
# from typing import Annotated

from SmartCom.face_validator import Face_Validator

be_app  = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

be_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@be_app.get("/")
async def start():
    return "hello"

@be_app.get("/testparam/{param}")
async def test_param(param):
    return param

@be_app.get("/face")
async def face_recog():
    fv = Face_Validator(wait=20)
    url = "https://dxwd4tssreb4w.cloudfront.net/image/5d57c4480c84b88ccfa086c42241e7c1" # Obama's image
    match = fv.capture_and_validate(url)
    return match

class UserLogin(BaseModel):
    email: str
    password: str = Form()
    
# class UserLoginForm(BaseModel):
#     message: str
#     loginUser: UserLogin
    

# @be_app.options("/api/auth/signin")
# async def signin(item: UserLogin):
#     return item

@be_app.post("/api/auth/signin", response_model=UserLogin)
async def signin(email: str = Form(), password: str = Form()):
    item = UserLogin(email=email, password=password)
    return item
    return JSONResponse(jsonable_encoder(item))