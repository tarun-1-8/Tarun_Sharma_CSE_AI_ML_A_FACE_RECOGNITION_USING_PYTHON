import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def load_dataset():
    subprocess.run(["python", "create_dataset.py"])
    messagebox.showinfo("Done", "Celebrity images downloaded.")

def encode_faces():
    subprocess.run(["python", "encode_faces.py"])
    messagebox.showinfo("Done", "Face encodings generated.")

def start_attendance():
    subprocess.run(["python", "recognize_faces.py"])

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Face Recognition Attendance")
root.geometry("400x300")

tk.Label(root, text="Face Recognition Attendance", font=("Arial", 16)).pack(pady=20)

tk.Button(root, text="Load Dataset", width=30, command=load_dataset).pack(pady=5)
tk.Button(root, text="Encode Faces", width=30, command=encode_faces).pack(pady=5)
tk.Button(root, text="Start Attendance", width=30, command=start_attendance).pack(pady=5)
tk.Button(root, text="Exit", width=30, command=exit_app).pack(pady=20)

root.mainloop()
