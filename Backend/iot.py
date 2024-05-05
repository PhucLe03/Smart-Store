from SmartCom.face_validator import Face_Validator, Face_Reader
import face_recognition
import mysql.connector as sqlcon
import SmartCom.util as util
import numpy
import pickle
import json
from fastapi.encoders import jsonable_encoder

database = sqlcon.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="test"
)

db_cursor = database.cursor()

# sql = "SELECT * from user"
# db_cursor.execute(sql)

# results = db_cursor.fetchall()

# result = util.fetchall_then_label(results, db_cursor.description)
# for r in result:
#     print(r)
def read_user_face(email):
    query_sql = "SELECT face_encode from user WHERE email = %s"
    query_var = [str(email)]
    db_cursor.execute(query_sql, query_var)
    result = db_cursor.fetchone()
    # user = util.fetchone_then_label(result, db_cursor.description)
    # print('faceencode:', result[0])
    return result[0]

face_read = Face_Reader()
# TODO: 
image = "./.venv/imgs/Phuc.JPG"
face = face_read.get_face_from_image(image)
if not face is None:
    print('one face')
else:
    print('More than one face')



exit()

email = "phuc.le1103@hcmut.edu.vn"
email = "phuc.le@gmail.com"
face = (read_user_face(email))
if face == "":
    print('faceid not register')
    exit()
array_list = json.loads(face)

person_face = numpy.array(array_list)


face_read = Face_Reader()
first_face = (face_read.get_face_from_video())
if not first_face is None:
    match = face_recognition.compare_faces([person_face], first_face)
    if True in match:
        print('found')
    else:
        print('not found')
else:
    print('More than one face found')





