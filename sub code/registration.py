import customtkinter as tk
from customtkinter import filedialog
from PIL import Image ,ImageTk
import shutil
import os
from notification import show_notification as notify

def registration():

    file_path = ''

    tpl = tk.CTk()

    def file_find():
        global file_path
        file_path = filedialog.askopenfilename()
        if file_path:
            update_photo_label()
            enable_entry()

    def enable_entry():
        entry_box.configure(state='normal')

    def update_photo_label():
        if file_path:
            notify(tpl,'Enter the name for the person',5)
            temp_Photo = Image.open(file_path)
            temp_Photo=tk.CTkImage(temp_Photo,size=(250,250))
            photo_label.configure(image=temp_Photo)
            photo_label.update()
            open_button.configure(state='disabled')
            entry_box.configure(state='normal')

    def change_and_copy():
        new_file_name = entry_box.get()
        if file_path and new_file_name:
            file_dir, file_ext = os.path.splitext(file_path)
            new_path = f'Data/Attandease/{new_file_name}{file_ext}'

            # Check if the destination folder exists, and create it if not
            destination_folder = os.path.dirname(new_path)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            shutil.copy(file_path, new_path)
            notify(tpl,f'Image Saved !! as {new_file_name}',3)
            tpl.destroy()
        elif file_path:
            notify(tpl,'please Select Image',5)
        elif new_file_name:
            notify(tpl,'Enter the name first !! then save!',7)
    default_image = Image.open('Data/processing/user.png')
    default_image = tk.CTkImage(default_image,size=(250, 255))  # Resize the default image
    #
    photo_label = tk.CTkLabel(tpl, text='', image=default_image)
    photo_label.pack()

    entry_box = tk.CTkEntry(tpl, state='disabled', width=80)
    entry_box.pack()
    # entry_box.configure(state='normal')

    open_button = tk.CTkButton(tpl, text='Select File', command=file_find)
    open_button.pack()

    copy_button = tk.CTkButton(tpl, text='Change and Copy', command=change_and_copy)
    copy_button.pack()
    notify(tpl,'Select image than add name in the box',7)
    tpl.mainloop()


    import cv2 
    import face_recognition as frcn
    import os 
    import numpy as np
    import pickle

    attendease_path='Data/Attandease'
    known_face_encodings=[]
    images=[]
    attendease_name=[]
    images_list=os.listdir(attendease_path)

    for photos in images_list:
        current_image=cv2.imread(f'{attendease_path}\{photos}')

        images.append(current_image)
        attendease_name.append(os.path.splitext(photos)[0])
    def create_encodings(images):
        encodinglist=[]
        for image in images:
            image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            current_image_encoding=frcn.face_encodings(image)[0]
            encodinglist.append(current_image_encoding)
        return encodinglist

    known_face_encodings=create_encodings(images)
    known_face_encodings=[np.array(enc) for enc in known_face_encodings]
    print('encoding complete ')
    pickle_file = "Data/processing/known_face_encodings.pkl"
    # Open the file in binary write mode and save the list to it
    with open(pickle_file, 'wb') as file:
        pickle.dump(known_face_encodings, file)
    print(f"Known face encodings saved to {pickle_file}")

if __name__=='__main__':
    registration()