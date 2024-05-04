from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
# from typing import Annotated
import mysql.connector as sqlcon
import json
import pickle

from SmartCom.face_validator import Face_Validator
import SmartCom.util as util

be_app  = FastAPI()

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
    url = "https://dxwd4tssreb4w.cloudfront.net/image/5d57c4480c84b88ccfa086c42241e7c1" # Obama's image
    match = fv.capture_and_validate(url)
    return match

class UserLogin(BaseModel):
    email: str
    password: str = Form()
    
class User(BaseModel):
    name: str
    login_info: UserLogin
    
# class UserLoginForm(BaseModel):
#     message: str
#     loginUser: UserLogin
    

# @be_app.options("/api/auth/signin")
# async def signin(item: UserLogin):
#     return item

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
        return JSONResponse(jsonable_encoder(final_res))
        # final_res = {}
        # for i, col in enumerate(db_cursor.description):
        #     # print('col', col[0])
        #     final_res[col[0]] = db_res[i]
        # print('res', final_res)
        encode = final_res['face_encode']
        res = {}
        res['encode'] = encode
        return JSONResponse(jsonable_encoder(res))
        final_res['face_encode'] = pickle.loads(bytes(encode))
        # print(pickle.loads(encode))
        # NOTE: return json object of the user
    except Exception as e:
        print('!!!Server Error:', e)
        raise HTTPException(status_code=404, detail="Email or password is incorrect")



