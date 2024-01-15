import cv2 as cv
from PIL import Image, ImageTk
import tkinter as tk
def capture():
    ret, frame = cam.read()
    if not ret:
        cat.after(10, capture)
        return
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    update_label(frame)
    cat.after(10, capture)
def update_label(frame):
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    img = Image.fromarray(frame_rgb)
    imgtk = ImageTk.PhotoImage(image=img)

    video_label.imgtk = imgtk
    video_label.config(image=imgtk)
cat = tk.Tk()
cam = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
video_label = tk.Label(cat)
video_label.pack()
capture()
cat.mainloop()
cam.release()
