# Face Recognition Attendance System 🎥🧑‍💼

A Python-based face recognition attendance system using webcam, face encodings, and a graphical interface.

## 📌 Features
- Load celebrity images as dataset
- Encode faces and store for future recognition
- Real-time face recognition using webcam
- Automatically mark attendance with timestamp
- GUI-based control using Tkinter

---

## 🛠️ Technologies Used

- **Python**
- **face_recognition** – Face detection and recognition
- **OpenCV (cv2)** – Webcam and image processing
- **Tkinter** – GUI development
- **pickle** – Save/load face encodings
- **urllib.request** – Download images from URLs
- **CSV** – Log attendance
- **subprocess, os, datetime** – Python standard libraries

---

## 🧑‍💻 Setup Instructions

### ✅ 1. Clone the Repository
```bash
git clone https://github.com/tarun-1-8/Tarun_Sharma_CSE_AI_ML_A_FACE_RECOGNITION_USING_PYTHON/tree/main
```

### 📦 2. Install Dependencies
Ensure Python is installed, then run:
```bash
pip install -r requirements.txt
```

If you face issues with `tkinter`, install it using your OS package manager (e.g., `sudo apt install python3-tk` for Ubuntu).

---

## 🚀 How to Run

### ▶️ Step 1: Start the GUI
```bash
python main_app.py
```

### 🖼️ Step 2: Load Dataset
- Click **“Load Dataset”**
- Downloads celebrity images into `dataset/` folder.

### 🧠 Step 3: Encode Faces
- Click **“Encode Faces”**
- Extracts and stores facial features into `encodings.pkl`.

### 🎥 Step 4: Start Attendance
- Click **“Start Attendance”**
- Opens webcam, identifies known faces, and logs attendance in `attendance.csv`.
- Press **‘q’** to quit webcam window.

### ❌ Step 5: Exit
- Click **“Exit”** to close the GUI.

---

## 📁 Output Files

| File / Folder        | Description                             |
|----------------------|-----------------------------------------|
| `dataset/`           | Stores downloaded face images           |
| `encodings.pkl`      | Pickled face encodings and names        |
| `attendance.csv`     | CSV log of attendance with date & time  |

---

## 📸 Dataset
This app uses images of:
- Elon Musk
- Emma Watson
- Tom Holland

You can add more images manually in the `dataset/` folder using the format: `name_0.jpg`, `name_1.jpg`, etc.

---

## 📝 License
This project is for educational purposes.

---

## 🙌 Authors
- Tarun Sharma (2401730104)  
- Swastik Sharma (2401730032)  
- Gaurav (2401730019)
