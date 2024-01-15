import cv2
import face_recognition as frcn
import os
import numpy as np
import pickle
import customtkinter as tk
from PIL import Image, ImageTk
import attendence as ac
# from notification import show_notification as notify
import os
import sys
base_path = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
person =str()
attendease_path = 'Data/Attandease'
images = []
attendease_name = []
images_list = os.listdir(attendease_path)
for photos in images_list:
    current_image = cv2.imread(f'{attendease_path}/{photos}')
    images.append(current_image)
    attendease_name.append(os.path.splitext(photos)[0])
known_face_encodings = []
try:
    with open('Data/processing/known_face_encodings.pkl', 'rb') as file:
        known_face_encodings = pickle.load(file)
except FileNotFoundError:
    print('Pickle file not found. Please run Program encoder to create known face encodings.')
def recognition():
    def capture():
        success, cam = cap.read()
        if success:
            imgS = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)
            cam_img_loc = frcn.face_locations(imgS)
            cam_image_encodings = frcn.face_encodings(imgS, cam_img_loc)
            cam_image_encodings = [np.array(enc) for enc in cam_image_encodings]
            for encode_face, face_loc in zip(cam_image_encodings, cam_img_loc):
                check_match = frcn.compare_faces(known_face_encodings, cam_image_encodings[0])
                face_dis = frcn.face_distance(known_face_encodings, encode_face)
                print(face_dis)
                match_index = np.argmin(face_dis)
                if check_match[match_index]:
                    global person
                    name = attendease_name[match_index].upper()
                    person =name
                    y1, x2, y2, x1 = face_loc
                    cv2.rectangle(cam, (x1, y1), (x2, y2), (52, 32, 79), 3)
                    cv2.putText(cam, name, (x1-6, y2+6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    # if keyboard.is_pressed('p'):
                    #     ac.present(name)
                    #     print(f'{name} attended')
                    # if 'name' in locals():
                    #     if cv2.waitKey(1) & 0xFF == ord('p'):
                    #         ac.present(name)
                    #         print(f'{name} attended')
            frame_rgb = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk=tk.CTkImage(img,size=(500,400))
            # imgtk = ImageTk.PhotoImage(image=img)
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)
            video_label.image = imgtk
            if not recognition.stopped:
                tpl.after(10, capture)
    def stop_capture(count=2):
        start_button.configure(state='normal')
        attadance_button.configure(state='disabled')
        if count > 0:
            # Load your image
            display.configure(state='normal')
            display.insert(1.0,"Attandance Taker")
            display.configure(state='disabled')
            u = Image.open('Data/processing/user.png')
            u = ImageTk.PhotoImage(u, size=(500, 400))
            video_label.configure(image=u)
            tpl.update_idletasks()
            recognition.stopped = True
            display.configure(state='normal')
            display.delete(1.0,tk.END)
            display.configure(state='disabled')
            tpl.after(10, stop_capture, count - 1)
    def start_capture():
        attadance_button.configure(state='normal')
        display.configure(state='normal')
        display.delete(1.0, tk.END)
        display.insert(1.0,"Attandance Taker")
        display.configure(state='disabled')
        recognition.stopped = False
        start_button.configure(state='disabled')
        capture()
    def present_taker():
        try:
            if person !='':
                gett=f'attandance taken {person}'
                ac.present(person)
                print(f'present taken')
                # notify(tpl,f'attendance taken {person}',5)
                # person=""
            else:
                gett = "No person specified"
        except Exception as e:
            print(e)
            gett = "Face not detected properly!"
        display.configure(state='normal')
        display.delete(1.0, tk.END)
        display.insert(1.0, gett)
        display.configure(state='disabled')    
    recognition.stopped = False
    def restore_main_window():
        cap.release()
        tpl.destroy()
        # subprocess.Popen(["python", "app.pyw"])
    cap = cv2.VideoCapture(0)
    tpl = tk.CTk()
    tpl.lift()
    tpl.title("Face Recognition")
    tpl.geometry('1000x700')
    tpl.resizable(False,False)
    # tpl.configure(fg_color='white')
    video_frame = tk.CTkFrame(tpl, width=500, height=400, bg_color='gray')
    video_frame.place(relx=0.5,rely=0.5,anchor='center')
    u = Image.open('Data/processing/user.png')
    u = tk.CTkImage(u,size=(430,400))
    video_label = tk.CTkLabel(video_frame,text='',image=u)
    video_label.pack(fill='both',anchor='center')
    start_button = tk.CTkButton(tpl, text="Start Capture", command=start_capture)
    start_button.pack()
    stop_button = tk.CTkButton(tpl, text="Stop Capture", command=stop_capture)
    stop_button.pack()
    attadance_button = tk.CTkButton(tpl, text="Register Attandance", command=present_taker)
    attadance_button.pack()
    display=tk.CTkTextbox(tpl,height=30,width=280,font=tk.CTkFont(family='cursive',size=14,weight='bold'))
    display.place(relx=0.5,rely=0.9,anchor='center')
    display.insert(1.0,"Attandance Taker")
    tpl.protocol("WM_DELETE_WINDOW",restore_main_window)
    tpl.mainloop()
if __name__=='__main__':
    recognition()