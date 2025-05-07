# FACE_RECOGNITION_USING_PYTHON
## TEAM MEMBERS
### TARUN SHARMA(TEAM LEADER) 2401730104
### SWASTIK SHARMA 2401730032
### GOURAV 2401730019
## PROJECT DESCRIPTION
This project explains a face recognition system developed using Python. It highlights objectives, methodology, real-time implementation, and applications in security, attendance, and smart devices. The project uses libraries like OpenCV and dlib to ensure accurate facial detection. Challenges like lighting and angles are also addressed, enhancing overall system reliability.

## Video Explaination
[video](https://example.com)

## Technologies used
### Python – Core language used for all scripts.
### face_recognition

### For detecting and recognizing faces in images and real-time video.

### OpenCV (opencv-python)

### Used for video capture from the webcam, image processing, and GUI display (like bounding boxes).

### tkinter

### For building the graphical user interface (GUI) of the main application (main_app.py).

### pickle

### To save and load serialized data (face encodings and names).

### urllib.request

### To download images from the internet (in create_dataset.py).

### os and datetime (Standard Python Libraries)

### File and folder operations, getting current date/time.

### subprocess

### To call Python scripts from within the GUI app.

## HOW TO RUN THE CODE?
## step1-
## IN CMD
##  pip install -r requirements.txt
## python main_app.py
## step2-
## Load the dataset
## Click on “Load Dataset”.

## This will:

## Download sample celebrity images (Elon Musk, Emma Watson, Tom Holland) into the dataset/ folder.
## step3-
## encod faces
## Click on “Encode Faces”.

## This will:

## Extract face encodings from the images.

## Save them into encodings.pkl for later use in recognition.
## step4-
## Start attendance
## Click on “Start Attendance”.

## This will:

## Open your webcam.

## Detect and recognize faces in real-time.

## Mark attendance in attendance.csv (only once per person).

## Press ‘q’ on the keyboard to exit.
## step5-
## for exiting 
## Click “Exit” to close the application.





