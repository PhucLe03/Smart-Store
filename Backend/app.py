from fastapi import FastAPI

from SmartCom.face_validator import Face_Validator

app  = FastAPI()

@app.get("/")
async def start():
    return "hello"

@app.get("/testparam/{param}")
async def test_param(param):
    return param

@app.get("/face")
async def face_recog():
    fv = Face_Validator(wait=20)
    url = "https://dxwd4tssreb4w.cloudfront.net/image/5d57c4480c84b88ccfa086c42241e7c1" # Obama's image
    match = fv.capture_and_validate(url)
    return match

