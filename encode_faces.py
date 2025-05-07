import face_recognition
import os
import pickle

dataset_path = "dataset"
known_encodings = []
known_names = []

for filename in os.listdir(dataset_path):
    if filename.endswith(".jpg"):
        image_path = os.path.join(dataset_path, filename)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_encodings.append(encodings[0])
            name = filename.split("_")[0]
            known_names.append(name)

data = {"encodings": known_encodings, "names": known_names}
with open("encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print("Encodings saved.")
