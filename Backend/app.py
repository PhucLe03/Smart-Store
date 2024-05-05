from fastapi import FastAPI, Form, File, UploadFile, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response, JSONResponse
from pydantic import BaseModel
# from typing import Annotated
import mysql.connector as sqlcon
import json
import pickle
import uuid

from SmartCom.face_validator import Face_Validator
import SmartCom.util as util

be_app = FastAPI()

database = sqlcon.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="test"
)

db_cursor = database.cursor()

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
    url = "https://dxwd4tssreb4w.cloudfront.net/image/5d57c4480c84b88ccfa086c42241e7c1"  # Obama's image
    match = fv.capture_and_validate(url)
    return match


class UserLogin(BaseModel):
    email: str = Form()
    password: str = Form()


class User(BaseModel):
    name: str
    login_info: UserLogin


class UserData(BaseModel):
    username: str = Form()
    name: str = Form()
    email: str = Form()
    password: str = Form()


class UserRegister(BaseModel):
    user_register: UserData = Form()
    file: UploadFile = File(...)

class Temp(BaseModel):
    user_register: UserData = Form()
# class UserLoginForm(BaseModel):
#     message: str
#     loginUser: UserLogin


# @be_app.options("/api/auth/signin")
# async def signin(item: UserLogin):
#     return item
@be_app.post("/api/auth/temp", response_model=Temp)
async def temp(user_register: str = Form()):
# async def temp(username: str = Form(), name: str = Form(), email: str = Form(), password: str = Form()):
    # name = n
    formatted = json.loads(user_register)
    res = {}
    res['name'] = formatted['name']
    return JSONResponse(jsonable_encoder(res))


@be_app.post("/api/auth/signin", response_model=UserLogin)
async def signin(email: str = Form(), password: str = Form()):
    # item = UserLogin(email=email, password=password)
    try:
        query_sql = "SELECT * FROM user WHERE email = %s AND password= %s"
        query_var = (str(email), str(password))
        db_cursor.execute(query_sql, query_var)
        db_res = db_cursor.fetchone()
        final_res = util.fetchone_then_label(db_res, db_cursor.description)
        final_res['accessToken'] = True
        final_res['role'] = "ROLE_STUDENT"
        # NOTE: return json object of the user
        return JSONResponse(jsonable_encoder(final_res))

    except Exception as e:
        print('!!!Server Error:', e)
        error = {}
        error['message'] = "Email or password is incorrect"
        return JSONResponse(content=error, status_code=status.HTTP_404_NOT_FOUND)


@be_app.post("/api/auth/signup", response_model=UserRegister)
async def signup(user_register: str = Form(), file: UploadFile = File(...)):
    # user_register = form.user_register
    # file = form.file
    user = json.loads(user_register)
    imgdir = "./temp/imgs/"
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!

    # example of how you can save the file
    with open(f"{imgdir}{file.filename}", "wb") as f:
        f.write(contents)
    res = {"user": user['name'] , "filename": file.filename}
    return JSONResponse(jsonable_encoder(res))


@ be_app.post("/api/sendimage")
async def sendimage(image: UploadFile = File(...)):
    imgdir="./temp/imgs/"
    image.filename=f"{uuid.uuid4()}.jpg"
    contents=await image.read()  # <-- Important!

    # example of how you can save the file
    with open(f"{imgdir}{image.filename}", "wb") as f:
        f.write(contents)

    return {"filename": image.filename}
