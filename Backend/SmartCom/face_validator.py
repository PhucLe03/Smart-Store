import face_recognition
import cv2
import numpy as np
import time
import urllib.request

import mysql.connector as sqlcon
import json
import numpy

# import sys


# class Face_Reader():
#     def __init__(self):
#         self.video_capture = cv2.VideoCapture(0)

class Database():
    def __init__(self):
        self.database = sqlcon.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="test"
        )
        self.db_cursor = self.database.cursor()
        
    def select(self, query_sql: str, query_var: list[str] = None):
        if query_var:
            self.db_cursor.execute(query_sql, query_var)
        else:
            self.db_cursor.execute(query_sql)
        return
    
    def insert(self, query_sql: str, query_var: list[str] = None):
        if query_var:
            self.db_cursor.execute(query_sql, query_var)
            self.database.commit()
        else:
            self.db_cursor.execute(query_sql)
            self.database.commit()
        return
    
    def fetchone(self):
        return self.db_cursor.fetchone(), self.db_cursor.description
    
    def fetchall(self):
        return self.db_cursor.fetchall(), self.db_cursor.description
        
    def read_user_face(self, email):
        query_sql = "SELECT face_encode from user WHERE email = %s"
        query_var = [str(email)]
        self.db_cursor.execute(query_sql, query_var)
        result = self.db_cursor.fetchone()
        # user = util.fetchone_then_label(result, db_cursor.description)
        # print('faceencode:', result[0])
        user_face_code = result[0]
        array_list = json.loads(user_face_code)
        return numpy.array(array_list)
    
    def read_user_face_raw(self, email):
        query_sql = "SELECT face_encode from user WHERE email = %s"
        query_var = [str(email)]
        self.db_cursor.execute(query_sql, query_var)
        result = self.db_cursor.fetchone()
        return result[0]
    


class Face_Validator():
    def __init__(self, vidcap: cv2.VideoCapture = None, wait=10):
        self.video_capture = None
        if vidcap is None:
            self.video_capture = cv2.VideoCapture(0)
        else:
            self.video_capture = vidcap #cv2.VideoCapture(0)
        self.max_wait = wait

    def get_face_from_image(self, imgfile):
        image = face_recognition.load_image_file(imgfile)
        face_locations = face_recognition.face_locations(image)
        if len(face_locations) == 1:
            face_encode = face_recognition.face_encodings(image)[0]
            return face_encode
        else:
            return None

    def get_face_from_video(self):
        # process_this_frame = True
        while True:
            _, frame = self.video_capture.read()
            frame = cv2.flip(frame, 1)

            # Only process every other frame of video to save time
            # if process_this_frame:
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            # rgb_small_frame = small_frame[:, :, ::-1]
            rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(
                rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)
            # print(face_encodings)
            # face_encodings = face_locations
            if len(face_encodings) > 0:
                self.video_capture.release()
                cv2.destroyAllWindows()
                # return result
                return face_encodings
                # else:
                #     self.video_capture.release()
                #     cv2.destroyAllWindows()
                #     return None

            # process_this_frame = not process_this_frame
        self.video_capture.release()
        cv2.destroyAllWindows()
        return None

    # Read image from file, imgfile is the path to file
    def read_face(self, imgfile: str):
        filename = imgfile.split('/')[-1]
        name, _ = filename.split('.')
        image = face_recognition.load_image_file(imgfile)
        face_encoding = face_recognition.face_encodings(image)[0]
        return face_encoding, name

    def read_face_from_url(self, url):
        response = urllib.request.urlopen(url)
        image = face_recognition.load_image_file(response)
        face_encoding = face_recognition.face_encodings(image)[0]
        return face_encoding, "User"

    # Compare face from video capture and from imgfile
    def capture_and_validate(self, url):
        mat, person_name = self.read_face_from_url(url)
        known_face_encodings = [mat]
        known_face_names = [person_name]
        result = "None"

        # face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        now = time.time()
        while True:
            _, frame = self.video_capture.read()
            frame = cv2.flip(frame, 1)

            # Only process every other frame of video to save time
            if process_this_frame:
                # Resize frame of video to 1/4 size for faster face recognition processing
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                # rgb_small_frame = small_frame[:, :, ::-1]
                rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(
                    rgb_small_frame)
                face_encodings = face_recognition.face_encodings(
                    rgb_small_frame, face_locations)
                # print(face_encodings)
                # face_encodings = face_locations
                face_names = []
                # if len(face_locations) == 1:
                #     face_names.append("User")
                for face in face_encodings:
                    name = "Unknown"
                    # face_encode = face_recognition.face_encodings()
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(
                        known_face_encodings, face)

                    # # If a match was found in known_face_encodings, just use the first one.
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]

                    # # Or instead, use the known face with the smallest distance to the new face
                    # face_distances = face_recognition.face_distance(
                    #     known_face_encodings, face)
                    # best_match_index = np.argmin(face_distances)
                    # if matches[best_match_index]:
                    #     name = known_face_names[best_match_index]

                    face_names.append(name)

            process_this_frame = not process_this_frame

            # Display the resulting image``
            # cv2.imshow('Video', frame)
            # time.sleep(0.1)

            if person_name in face_names:
                # Show that face is match
                result = "Validated " + person_name
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                result = "Interupt"
                break
            if time.time() - now > self.max_wait:
                result = "Face not match"
                break

        # Release handle to the webcam
        self.video_capture.release()
        # cv2.destroyAllWindows()
        return result
