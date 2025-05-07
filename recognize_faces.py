import face_recognition
import cv2
import pickle
import os
from datetime import datetime

with open("encodings.pkl", "rb") as f:
    data = pickle.load(f)

if not os.path.exists("attendance.csv"):
    with open("attendance.csv", "w") as f:
        f.write("Name,Date,Time\n")

def mark_attendance(name):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    with open("attendance.csv", "r+") as f:
        lines = f.readlines()
        entries = [line.split(",")[0] for line in lines]
        if name not in entries:
            f.write(f"{name},{date},{time}\n")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    for encoding, location in zip(encodings, faces):
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"

        if True in matches:
            index = matches.index(True)
            name = data["names"][index]
            mark_attendance(name)

        top, right, bottom, left = location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    cv2.imshow("Face Recognition Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
