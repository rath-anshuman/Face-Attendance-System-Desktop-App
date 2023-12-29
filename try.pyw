# def create_encodings(images):
#     encodinglist=[]
#     for image in images:
#         image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#         current_image_encoding=frcn.face_encodings(image)[0]
#         encodinglist.append(current_image_encoding)
#     return encodinglist
# known_face_encodings=create_encodings(images)
# known_face_encodings = [np.array(enc) for enc in known_face_encodings]
# print('encoding complete ')
# import cv2
# import face_recognition as frcn
# import os
# import numpy as np

# # Directory containing images of known individuals
# attendease_path = 'Data/Attandease'

# # Lists to store known face encodings and names
# known_face_encodings = []
# attendease_names = []

# # Get a list of image files in the directory
# images_list = os.listdir(attendease_path)

# # Load and encode known face images
# for photo in images_list:
#     current_image = cv2.imread(os.path.join(attendease_path, photo))
#     current_image = cv2.cvtColor(current_image, cv2.COLOR_BGR2RGB)
#     face_encoding = frcn.face_encodings(current_image)
    
#     if len(face_encoding) > 0:
#         # Use the first face encoding if multiple faces are detected
#         known_face_encodings.append(np.array(face_encoding[0]))
#         attendease_names.append(os.path.splitext(photo)[0])

# print('Encoding complete')

# # Initialize the camera
# cap = cv2.VideoCapture(0)

# while True:
#     success, cam = cap.read()
    
#     # Resize, convert, and encode the camera image
#     imgS = cv2.resize(cam, (0, 0), None, 0.25, 0.25)
#     imgS = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)
#     cam_img_loc = frcn.face_locations(imgS)
#     cam_image_encodings = frcn.face_encodings(imgS, cam_img_loc)
    
#     cam_image_encodings = [np.array(enc) for enc in cam_image_encodings]

#     for encode_face, face_loc in zip(cam_image_encodings, cam_img_loc):
#         # Compare the camera image encoding with known face encodings
#         check_match = frcn.compare_faces(known_face_encodings, encode_face)
#         face_dis = frcn.face_distance(known_face_encodings, encode_face)
#         print(face_dis)

#     cv2.imshow('camera', cam)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAlltpls()


# import cv2 as cv2
# # import numpy as np
# import face_recognition as fcrn


# fst=fcrn.load_image_file('Data/narendra.jpeg')
# fst=cv2.cvtColor(fst,cv2.COLOR_BGRA2RGB)

# sec=fcrn.load_image_file('Data/test1 (2).jpeg')
# sec=cv2.cvtColor(sec,cv2.COLOR_BGRA2RGB)

# face_locationnamo=fcrn.face_locations(fst)[0]
# encodefstmodi=fcrn.face_encodings(fst)[0]
# cv2.rectangle(fst,(face_locationnamo[3],face_locationnamo[0]),(face_locationnamo[1],face_locationnamo[2]),(64, 86, 173),4)

# face_locationmodi=fcrn.face_locations(sec)[0]
# encodesecmodi=fcrn.face_encodings(sec)[0]
# cv2.rectangle(sec,(face_locationmodi[3],face_locationmodi[0]),(face_locationmodi[1],face_locationmodi[2]),(64, 86, 173),4)



# check=fcrn.compare_faces([encodefstmodi],encodesecmodi)
# print(check)

# cv2.imshow('namo',fst)
# cv2.imshow('modi',sec) 

# cv2.waitKey(0)

# import pandas as pd

# # Replace 'input.csv' with the path to your CSV file
# csv_file = 'abcd.csv'

# # Replace 'output.xlsx' with the desired name of the Excel file
# excel_file = 'output.xlsx'

# # Read the CSV file into a DataFrame
# df = pd.read_csv(csv_file)

# # Write the DataFrame to an Excel file
# df.to_excel(excel_file, index=False)

# import getpass

# # Get the currently logged-in tpls user's username
# current_user = getpass.getuser()

# print(f"The currently logged-in user is: {current_user}")


# import pandas as pd

# # try:
   
# # except:
# #     print('tpl')


# data1=pd.read_csv('tpl.csv')
# data2=pd.read_csv('tpl2.csv')
# combd=data1.merge(data2,left_index=False)
# # combd=data1.app
# combd.to_excel('output.xlsx')


# import pandas as pd
# headings=pd.DataFrame({'SlNo.':[]  ,'Name':[],'Time':[],'Subject':[]})
# headings.to_csv('tpl.csv',index=False)
# # Read the existing CSV files
# data1 = pd.read_csv('tpl.csv')
# data2 = pd.read_csv('tpl2.csv')

# # Concatenate data2 to data1
# combined_data = pd.concat([data1, data2], ignore_index=True)

# # Save the combined data to the original data1 CSV file
# combined_data.to_csv('tpl.csv', index=False)
# combined_data.to_excel('tpl.xlsx', index=False)
# import pandas as pd
# df = pd.DataFrame( columns=["SlNo.", "Name", "Time", "Subject"])

# # Append a new row to the DataFrame
# df = df.append(
#     {"SlNo.": 2, "Name": "John Doe", "Time": 19.0, "Subject": "math"}, ignore_index=True
# )

# # Print the DataFrame
# print(df.to_string())


# import pandas as pd

# df = pd.DataFrame(columns=["SlNo.",

# # Create a new row as a DataFrame
# new_data = pd.DataFrame({ "Name": ["John Doe"], "Time": [19.0], "Subject": ["math"]})
# new_data = pd.DataFrame({ "Name": ["tpl"], "Time": [139.0], "Subject": ["4math"]})

# # Concatenate the new data with the original DataFrame
# df = pd.concat([df, new_data], ignore_index=False)
# df.to_csv('output.csv')

# # Print the DataFrame
# print(df.to_string(index=False))


# import pandas as pd
# d1=pd.read_csv('tpl.csv')
# d1.columns(["Name", "Time", "Subject"])
# d3.to_csv('a.csv')
# print(d3)


# import openpyxl as ox
# import pandas as pd
# data=pd.DataFrame()
# data.to_excel('b.xlsx')
# dataxl=ox.load_workbook('b.xlsx')
# datas=dataxl.active
# datas['A1']='Name'
# datas['B1']='Time'
# datas['C1']='Subject'

# # datas.append([,'55.55','python'])
# dataxl.save('b.xlsx')
# nxl=pd.read_excel('main.xlsx')
# nxl.to_csv('main.csv')

# import openpyxl
# from openpyxl.styles import Font

# # Create a new workbook and select a sheet
# workbook = openpyxl.Workbook()
# sheet = workbook.active

# # Access cell A2 and set its font to bold
# cell = sheet['A2']
# bold_font = Font(bold=True)
# cell.font = bold_font

# # Add some text to the cell
# cell.value = "Bold Text in A2"

# # Save the workbook
# workbook.save("bold_text.xlsx")

# import os

# import cv2
# import os

# # Set the path to the Attandease folder
# attendease_path = 'Data/Attandease'

# # List all image files in the folder
# images_list = os.listdir(attendease_path)

# # Define the new resolution (width and height)
# new_width = 800  # Change this to your desired width
# new_height = 600  # Change this to your desired height

# for image_filename in images_list:
#     # Read the image
#     image_path = os.path.join(attendease_path, image_filename)
#     image = cv2.imread(image_path)

#     # Resize the image to the new resolution
#     resized_image = cv2.resize(image, (new_width, new_height))

#     # Save the resized image with the same name, overwriting the original
#     cv2.imwrite(image_path, resized_image)

# print("Images have been resized and overwritten.")




# import tkinter as tk
# from tkinter import filedialog

# def open_file_dialog():
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         print("Selected file:", file_path)

# def save_file_dialog():
#     file_path = filedialog.asksaveasfilename(defaultextension=".txt")
#     if file_path:
#         print("Saved file as:", file_path)

# # Create a main tpl
# cat = tk.Tk()

# # Create buttons for open and save dialogs
# open_button = tk.Button(cat, text="Open File", command=open_file_dialog)
# save_button = tk.Button(cat, text="Save File", command=save_file_dialog)

# open_button.pack()
# save_button.pack()

# # Start the main loop
# cat.mainloop()


# import cv2
# import face_recognition as frcn
# import pickle
# import time
# import numpy as np
# import attendence as ac

# known_face_encodings = []
# try:
#     with open('Data/proccessing/known_face_encodings.pkl', 'rb') as file:
#         known_face_encodings = pickle.load(file)
#     # print('Known face encodings loaded from pickle file.')
# except FileNotFoundError:
#     print('Pickle file not found. Please run Program encoder to create known face encodings.')

# def handle_attendance(name):
#     ac.present(name)
#     print(f'{name} attended')

# def recognition():
#     cap=cv2.VideoCapture(0)
#     while True :
#         success, cam = cap.read()
#         imgS=cv2.cvtColor(cam,cv2.COLOR_BGR2RGB)
#         cam_img_loc=frcn.face_locations(imgS)  
#         cam_image_encodings=frcn.face_encodings(imgS,cam_img_loc)
#         cam_image_encodings = [np.array(enc) for enc in cam_image_encodings]

#         for encode_face,face_loc in zip(cam_image_encodings,cam_img_loc):
#             check_match=frcn.compare_faces(known_face_encodings,cam_image_encodings[0]) 
#             face_dis=frcn.face_distance(known_face_encodings,encode_face)
#             print(face_dis)

#             match_index=np.argmin(face_dis)

#             if check_match[match_index]:
#                 name=attendease_name[match_index].upper()
#                 y1,x2,y2,x1=face_loc
#                 cv2.rectangle(cam,(x1,y1),(x2,y2),(


# import cv2 
# import face_recognition as frcn
# import os 
# import numpy as np
# import pickle
# import keyboard
# import customtkinter as tk
# from PIL import Image, ImageTk
# import attendence as ac

# name = ""
# attendease_path = 'Data/Attandease'
# images = []
# attendease_name = []
# images_list = os.listdir(attendease_path)

# for photos in images_list:
#     current_image = cv2.imread(f'{attendease_path}/{photos}')
#     images.append(current_image)
#     attendease_name.append(os.path.splitext(photos)[0])

# known_face_encodings = []

# try:
#     with open('Data/proccessing/known_face_encodings.pkl', 'rb') as file:
#         known_face_encodings = pickle.load(file)
# except FileNotFoundError:
#     print('Pickle file not found. Please run Program encoder to create known face encodings.')

# def recognition():
#     global name

#     cap = cv2.VideoCapture(0)

#     def capture():
#         success, cam = cap.read()
#         if not success:
#             tpl.after(10, capture)
#             return

#         imgS = cv2.resize(cam, (0, 0), None, 0.25, 0.25)
#         imgS = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)
#         cam_img_loc = frcn.face_locations(imgS)
#         cam_image_encodings = frcn.face_encodings(imgS, cam_img_loc)
#         cam_image_encodings = [np.array(enc) for enc in cam_image_encodings]

#         for encode_face, face_loc in zip(cam_image_encodings, cam_img_loc):
#             check_match = frcn.compare_faces(known_face_encodings, cam_image_encodings[0])
#             face_dis = frcn.face_distance(known_face_encodings, encode_face)
#             print(face_dis)
#             match_index = np.argmin(face_dis)

#             if check_match[match_index]:
#                 name = attendease_name[match_index].upper()

#                 if keyboard.is_pressed('p'):
#                     present_taker(name)

#                 y1, x2, y2, x1 = face_loc
#                 cv2.rectangle(cam, (x1, y1), (x2, y2), (52, 32, 79), 3)
#                 cv2.putText(cam, name, (x1-6, y2+6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#                 update_label(cam)

#         # Continue capturing frames
#         tpl.after(10, capture)

#     def update_label(frame):
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img = Image.fromarray(frame_rgb)
#         imgtk = tk.CTkImage(img, size=(500, 400))
#         video_label.imgtk = imgtk
#         video_label.configure(image=imgtk)

#     def present_taker(name):
#         ac.present(name)
#         print(f'{name} attended')

#     tpl = tk.CTk()

#     tpl.video_frame = tk.CTkFrame(tpl, width=500, height=400, corner_radius=30, fg_color='#6ed489')
#     tpl.video_frame.place(relx=0.2, rely=0.4, anchor='center')

#     video_label = tk.CTkLabel(tpl.video_frame, text='', width=500, height=400, corner_radius=40, bg_color='gray')
#     video_label.pack(fill='both', padx=10, pady=10)

#     capture()
#     tpl.mainloop()

# if __name__ == '__main__':
#     recognition()


# import tkinter as tk

# def clear_and_show_text():
#     clear_text()
#     show_text()

# def clear_text():
#     entry.delete(0, 'end')
#     display.config(state='normal')
#     display.delete(1.0, 'end')
#     display.config(state='disabled')

# def show_text():
#     text = entry.get()
#     display.config(state='normal')
#     display.delete(1.0, 'end')
#     display.insert('end', text)
#     display.config(state='disabled')

# # Create the main tpl
# root = tk.Tk()
# root.title("Text Display")

# # Create an entry widget
# entry = tk.Entry(root)
# entry.pack()

# # Create a "Show Text" button
# show_button = tk.Button(root, text="Show Text", command=clear_and_show_text)
# show_button.pack()

# # Create a text widget for displaying text
# display = tk.Text(root, state='disabled', height=5, width=30)
# display.pack()

# root.mainloop()




# import customtkinter as tk

# root = tk.CTk()
# root.title("Chatbot GUI")
# root.geometry('700x500')
# root.resizable(False,False)

# def response():
#     gett=root_enter.get()
#     root_display.configure(state='normal')
#     root_display.delete(1.0,tk.END)
#     root_display.insert(0.1,gett)
#     root_enter.delete(0,tk.END)
#     root_display.configure(state='disabled')
#     root_enter.delete(0,tk.END)
# root_display=tk.CTkTextbox(root,height=20,font=tk.CTkFont(family='cursive',size=20,weight='bold'))
# root_display.place(relx=0.5,rely=0.3,anchor='center')
# root_enter=tk.CTkEntry(root)
# root_enter.place  (relx=0.5,rely=0.6,anchor='center')
# root_click=tk.CTkButton(root,command=response,text='SAVE ')
# root_click.place  (relx=0.5,rely=0.9,anchor='center')


# root.mainloop()



# import tkinter as tk
# from tkinter import filedialog
# import shutil
# import os

# def browse_file():
#     file_path = filedialog.askopenfilename()
#     selected_file_label.config(text=file_path)

# def copy_file():
#     src_file = selected_file_label.cget("text")
#     dst_folder = destination_entry.get()
    
#     if src_file and dst_folder:
#         try:
#             shutil.copy(src_file, os.path.join(dst_folder, os.path.basename(src_file)))
#             result_label.config(text="File copied successfully!")
#         except Exception as e:
#             result_label.config(text=f"Error: {str(e)}")
#     else:
#         result_label.config(text="Please select a file and specify a destination folder.")

# # Create the main tpl
# root = tk.Tk()
# root.title("File Copy App")

# # Create a label to display the selected file path
# selected_file_label = tk.Label(root, text="")
# selected_file_label.pack()

# # Create a button to open a file dialog
# browse_button = tk.Button(root, text="Browse", command=browse_file)
# browse_button.pack()

# # Create an entry field for specifying the destination folder
# destination_label = tk.Label(root, text="Destination Folder:")
# destination_label.pack()
# destination_entry = tk.Entry(root)
# destination_entry.pack()

# # Create a button to copy the selected file
# copy_button = tk.Button(root, text="Copy File", command=copy_file)
# copy_button.pack()

# # Create a label to display the copy result
# result_label = tk.Label(root, text="")
# result_label.pack()

# # Start the main loop
# root.mainloop()





# m=1

# for i in range(1,6):
#    m*=i
#    print(m)


# import tkinter as tk

# def show_notification(message):
#     notification_tpl = tk.Toplevel(root)
#     notification_tpl.title("Notification")
#     notification_label = tk.Label(notification_tpl, text=message, padx=10, pady=10)
#     notification_label.pack()
#     notification_tpl.after(3000, notification_tpl.destroy)  # Close after 3 seconds (3000 milliseconds)

# root = tk.Tk()
# root.title("Tkinter In-App Notifications")

# notification_button = tk.Button(root, text="Show Notification", command=lambda: show_notification("This is a notification message."))
# notification_button.pack()

# root.mainloop()
# from google.oauth2 import service_account
# from googleapiclient.discovery import build

# # Path to your service account key file (JSON)
# key_file_path = 'Data/processing/facial-attandance-system-a44206e6d609.json'

# # Initialize the credentials
# credentials = service_account.Credentials.from_service_account_file(
#     key_file_path, scopes=['https://www.googleapis.com/auth/drive']
# )

# # Authenticate with the Google Drive API
# drive_service = build('drive', 'v3', credentials=credentials)

# # List all spreadsheets in Google Drive
# results = drive_service.files().list(q="mimeType='application/vnd.google-apps.spreadsheet'").execute()

# # Print the list of spreadsheets
# for file in results.get('files', []):
#     print(f'Spreadsheet Title: {file["name"]}, Spreadsheet ID: {file["id"]}')

# import subprocess as ss
# command=['streamlit','run','show_attandance.py']

# ss.call(command)




# import tkinter as tk
# from tkinter import ttk
# from openpyxl import load_workbook

# # Create a Tkinter tpl
# tpl = tk.Tk()
# tpl.title("Excel Sheet in Tkinter")

# # Create a Treeview widget to display the Excel data
# tree = ttk.Treeview(tpl, columns=("Column 1", "Column 2", "Column 3"))
# tree.heading("#1", text="Column 1")
# tree.heading("#2", text="Column 2")
# tree.heading("#3", text="Column 3")
# tree.pack()

# # Load the Excel sheet
# file_path = "your_excel_file.xlsx"
# workbook = load_workbook('Data/Attandance_list/Present_list_2023-10-24.xlsx')
# sheet = workbook.active

# # Iterate through the Excel sheet and insert data into the Treeview
# for row in sheet.iter_rows(values_only=True):
#     tree.insert("", "end", values=row)

# # Run the Tkinter event loop
# tpl.mainloop()


# import tkinter as tk
# from tkinter import messagebox

# def show_notification():
#     notification = messagebox.showinfo("Notification", "This is a notification message.")
#     # Schedule the notification to automatically close after 3000 milliseconds (3 seconds)
#     root.after(3000, passs)
# def passs():
#     pass

# root = tk.Tk()
# root.geometry("300x100")

# button = tk.Button(root, text="Show Notification", command=show_notification)
# button.pack()

# root.mainloop()


# mes
# import tkinter as tk
# from tkinter import ttk

# def create_tab(tab_name):
#     # Create a new tab and frame
#     frame = ttk.Frame(notebook)
#     notebook.add(frame, text=tab_name)
    
#     # Add widgets to the frame (you can customize each tab)
#     label = tk.Label(frame, text=f"Content of {tab_name} tab")
#     label.pack(padx=10, pady=10)

# # Create the main tkinter window
# root = tk.Tk()
# root.title("Tabbed Application")

# # Create a notebook (tabbed interface)
# notebook = ttk.Notebook(root)
# notebook.pack(fill='both', expand=True)

# # Create multiple tabs with their respective frames
# tabs = ["Tab 1", "Tab 2", "Tab 3"]
# for tab_name in tabs:
#     create_tab(tab_name)

# Start the tkinter main loop
# root.mainloop()
# import tkinter as tk
# from tkinter import ttk

# def create_frame_content(tab_name):
#     frame = ttk.Frame(notebook)
#     if tab_name == "Tab 1":
#         label = tk.Label(frame, text="This is Tab 1")
#         label.pack(padx=10, pady=10)
#     elif tab_name == "Tab 2":
#         button = tk.Button(frame, text="Click me in Tab 2")
#         button.pack(padx=10, pady=10)
#     elif tab_name == "Tab 3":
#         entry = tk.Entry(frame)
#         entry.pack(padx=10, pady=10)
    
#     notebook.add(frame, text=tab_name)

# root = tk.Tk()
# root.title("Tabbed Application")

# notebook = ttk.Notebook(root)
# notebook.pack(fill='both', expand=True)

# tabs = ["Tab 1", "Tab 2", "Tab 3"]
# for tab_name in tabs:
#     create_frame_content(tab_name)

# root.mainloop()

# r='*'
# for i in range(0,5):
#     print(r)
#     r+='*'

# ads    
# import tkinter as tk
# from tkinter import ttk
# import webview

# root = tk.Tk()

# def initialize_webview():
#     webview.create_window("My WebView", "https://example.com")

# ttk.Button(root, text="Open WebView", command=initialize_webview).pack()

# root.mainloop()
# import cv2
# import numpy as np
# import os
# import face_recognition
# import pickle
# import time
# from tkinter import *
# from tkinter import ttk, filedialog
# from PIL import Image, ImageTk
# import _thread
# import ctypes
# import platform
# import pyttsx3
# import _ctypes
# import time
# import sys
# import win32com.client as wincl
# import subprocess
# import ctypes
# import tkinter as tk


# speech = pyttsx3.init()
# speech.setProperty('rate', 150)


# class Face:
#     def __init__(self):
#         self.faces_encoded = []
#         self.faces_names = []

#     def register_face(self, face_image_path, person_name):
#         # load image from path and convert it to rgb
#         face_image = face_recognition.load_image_file(face_image_path)
#         face_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)

#         # detect faces in the image
#         face_locations = face_recognition.face_locations(face_rgb)

#         # if face detected, encode it
#         if len(face_locations) > 0:
#             face_encoding = face_recognition.face_encodings(face_rgb, face_locations)[0]
#             self.faces_encoded.append(face_encoding)
#             self.faces_names.append(person_name)

#     def recognize_face(self, unknown_image_path):
#         unknown_image = face_recognition.load_image_file(unknown_image_path)
#         unknown_rgb = cv2.cvtColor(unknown_image, cv2.COLOR_BGR2RGB)

#         face_locations = face_recognition.face_locations(unknown_rgb)
#         face_encodings = face_recognition.face_encodings(unknown_rgb, face_locations)

#         match_found = False
#         name = "Unknown"

#         # check each face encoding in the list
#         for face_encoding in face_encodings:
#             matches = face_recognition.compare_faces(self.faces_encoded, face_encoding)

#             # if match found, update name and match_found flag
#             if True in matches:
#                 match_found = True
#                 name = self.faces_names[matches.index(True)]
#                 break

#         return match_found, name


# class GUI:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Face Recognition")
#         self.master.geometry('1000x700')
#         self.master.resizable(False, False)

#         self.cap = cv2.VideoCapture(0)
#         self.f = Face()

#         self.main_frame = tk.Frame(self.master)
#         self.main_frame.pack(fill=BOTH, expand=True)

#         self.video_frame = tk.Frame(self.main_frame, bg='gray')
#         self.video_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

#         self.canvas = tk.Canvas(self.video_frame, width=430, height=400)
#         self.canvas.pack()

#         self.register_frame = tk.Frame(self.main_frame)
#         self.register_frame.place(relx=0.5, rely=0.9, anchor=CENTER)

#         self.name_label = tk.Label(self.register_frame, text='Name: ')
#         self.name_label.pack(side=LEFT)

#         self.name_entry = tk.Entry(self.register_frame)
#         self.name_entry.pack(side=LEFT)

#         self.register_button = tk.Button(self.register_frame, text='Register', command=self.register_face)
#         self.register_button.pack(side=LEFT)

#         self.capture_frame = tk.Frame(self.main_frame)
#         self.capture_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

#         self.capture_button = tk.Button(self.capture_frame, text='Capture', command=self.capture_image)
#         self.capture_button.pack(side=LEFT)

#         self.recognize_button = tk.Button(self.capture_frame, text='Recognize', command=self.recognize_face)
#         self.recognize_button.pack(side=LEFT)

#         self.name_label = tk.Label(self.main_frame, text='')
#         self.name_label.pack(side=BOTTOM)

#         self.video_loop()

#     def register_face(self):
#         file_path = filedialog.askopenfilename()
#         name = self.name_entry.get()
#         if file_path and name:
#             self.f.register_face(file_path, name)

#     def capture_image(self):
#         _, frame = self.cap.read()
#         cv2.imwrite('temp.jpg', frame)

#     def recognize_face(self):
#         self.cap.release()
#         match_found, name = self.f.recognize_face('temp.jpg')
#         if match_found:
#             self.name_label.config(text=f'Hello, {name}')
#             speech.say(f'Hello, {name}')
#             speech.runAndWait()
#         else:
#             self.name_label.config(text=f'Unknown person')
#             speech.say(f'Unknown person')
#             speech.runAndWait()
#         self.cap = cv2.VideoCapture(0)

#     def video_loop(self):
#         _, frame = self.cap.read()
#         frame = cv2.flip(frame, 1)
#         cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
#         img = Image.fromarray(cv2image)
#         imgtk = ImageTk.PhotoImage(image=img)
#         self.canvas.create_image(0, 0, anchor=NW, image=imgtk)
#         self.window.after(30, self.video_loop)


# if __name__ == '__main__':
#     #speech = pyttsx3.init()
#     #speech.setProperty('rate', 150)

#     face_recognition=pickle.load()

#     window = Tk()
#     window.geometry('1000x700')
#     app = GUI(window)
#     window.mainloop()


# app = GUI(window)

# app.mainloop()

# import customtkinter as tk
# import tkwebview2 as tw
# a=tk.CTk()

# tw.tkwebview2.WebView2(a,500,500,'https://rathnursery.great-site.net')
# a.mainloop()
import clr
import sys
from tkinter import Tk
from tkwebview2.tkwebview2 import WebView2, have_runtime, install_runtime
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Threading')
from System.Windows.Forms import Control
from System.Threading import Thread,ApartmentState,ThreadStart    
if not have_runtime():#没有webview2 runtime
    install_runtime()
root=Tk()
root.title('pywebview for tkinter test')
root.geometry('1200x600+5+5')
frame=WebView2(root,500,500)
frame.pack(side='left')
frame.load_html('<h1>hi hi</h1>')
frame2=WebView2(root,500,500)
frame2.pack(side='left',padx=20,fill='both',expand=True)
frame2.load_url('https://smart-space.com.cn/')
root.mainloop()

