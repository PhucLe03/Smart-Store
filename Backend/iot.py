from SmartCom.face_validator import Face_Validator
import face_recognition
import mysql.connector as sqlcon
import SmartCom.util as util
import numpy
import pickle
import json
from fastapi.encoders import jsonable_encoder
import sys


database = sqlcon.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="test"
)

db_cursor = database.cursor()


def read_user_face(email):
    query_sql = "SELECT face_encode from user WHERE email = %s"
    query_var = [str(email)]
    db_cursor.execute(query_sql, query_var)
    result = db_cursor.fetchone()
    # user = util.fetchone_then_label(result, db_cursor.description)
    # print('faceencode:', result[0])
    return result[0]


def validate_user_face(face_read: Face_Validator, email: str):
    user_face_code = read_user_face(email)
    array_list = json.loads(user_face_code)
    user_face = numpy.array(array_list)

    faces = face_read.get_face_from_video()
    if faces is None:
        return False
    else:
        for face in faces:
            if face is None:
                continue
            match = face_recognition.compare_faces([user_face], face)
            if True in match:
                # print(user_face)
                # print(face)
                return True
            else:
                continue
        return False


# face = (read_user_face(email))
# if face == "":
#     print('faceid not register')
#     exit()
# array_list = json.loads(face)

# person_face = numpy.array(array_list)
# print(person_face)


# first_face = (face_read.get_face_from_video())
# if not first_face is None:
#     match = face_recognition.compare_faces([person_face], first_face)
#     if True in match:
#         print('found')
#     else:
#         print('not found')
# else:
#     print('More than one face found')

# email = "phuc.le1103@hcmut.edu.vn"
# email = "phuc.le@gmail.com"
# email = "phuong@gmail.com"

def main():
    email = ""
    if len(sys.argv) == 2:
        email = str(sys.argv[1])
    else:
        print('Usage: python3 iot.py <email>')
        return

    face_read = Face_Validator()
    if validate_user_face(face_read, email):
        print('validate success')
    else:
        print('validate fail')


if __name__ == "__main__":
    main()
