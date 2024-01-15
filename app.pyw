import customtkinter as tk
from PIL import Image,ImageTk
import subprocess
import encoder_refresh
import exporter
import os
import sys
base_path = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
app=tk.CTk()
app.geometry('1920x1080')
def set_default_size(app):
    # Get the screen dimensions
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    # Calculate the default tpl size (e.g., 60% of the screen width and height)
    default_width = int(screen_width )
    default_height = int(screen_height )
    # Set the default tpl size
    app.geometry(f"{default_width}x{default_height}")
app.configure(fg_color='white',fill='both')
def close_tpl2():
    app.withdraw()
    app.destroy()
app.protocol("WM_DELETE_tpl",close_tpl2)
phone_bg='white'
app.attandance_bar=tk.CTkFrame(app,width=700,height=1950,fg_color='#43338B')
app.attandance_bar.place(relx=0,rely=0.5,anchor='center')
app.phnframe=tk.CTkFrame(app.attandance_bar,corner_radius=42,height=495,width=250,fg_color=phone_bg,border_width=2,border_color='black')
app.phnframe.place(relx=0.75,rely=0.5,anchor='center')
app.phnframe.di=tk.CTkFrame(app.phnframe,fg_color='black',bg_color=phone_bg,width=84,height=20,corner_radius=18)
app.phnframe.di.place(relx=0.5,rely=0.06,anchor='center')
phimg=Image.open('Data/processing/222.jpg')
ph_img=tk.CTkImage(phimg)
app.browserframe=tk.CTkFrame(app.phnframe,height=300,width=205,fg_color='white')
app.browserframe.place(relx=0.5,rely=0.459,anchor='center')
def recognitionapp():
    subprocess.Popen(["python", "recognition.py"])
app.button=tk.CTkButton(app.phnframe,height=40,width=60,text='START',corner_radius=60,border_width=5.5,fg_color='#3AFFD0',border_color='#7D92FF',
                          bg_color=phone_bg,font=tk.CTkFont(size=13,weight='bold',family='Segoe UI Black'),
                          text_color='#7B3C45',hover_color='#00EAA2',command=recognitionapp)
app.button.place(relx=0.5,rely=0.85,anchor='center')
app_navbar_font=tk.CTkFont(size=20,weight='bold')
app.navbar=tk.CTkLabel(app,height=100,width=1070,text='',fg_color='transparent',corner_radius=20,font=app_navbar_font)
app.navbar.place(x=945,rely=0.1,anchor='center')
img1=Image.open('Data//processing/im.png')
img_thumb=tk.CTkImage(img1,size=(1082,615))
app.main_frame=tk.CTkFrame(app,height=615,width=1082,bg_color='red',fg_color='#AFB3C2')
app.main_frame.place(relx=0.61,rely=0.5,anchor='center')
app.main_label=tk.CTkLabel(app.main_frame,height=615,width=1082,image=img_thumb,text='')
app.main_label.grid(row=0,column=0)
button_border_color='black'
button_fg_color='#422996'
button_text_color='#ffb094'
button_bg_color='#AFB3C2'
button_hover_color='#6446c7'
def registrationapp():
    # app.withdraw()
    subprocess.Popen(["python", "registration.py"])
def refreshapp():
    encoder_refresh.encode_again()
def exportapp():
    exporter.export()
    exporter.opene()
def show_attandanceapp():
    subprocess.Popen(['streamlit','run','show_attandance.py','> /dev/null'])
registration_button=tk.CTkButton(app,text='New Registration',width=250,height=50,corner_radius=60,border_width=5.5,fg_color=button_fg_color,border_color=button_border_color,
                          bg_color='#AFB3C2',font=tk.CTkFont(size=20,weight='bold',family='Segoe UI Black'),
                          text_color=button_text_color,hover_color=button_hover_color,command=registrationapp)
registration_button.place(relx=0.81,rely=0.4,anchor='center')
refresh_button=tk.CTkButton(app,text='Refresh Face Data',width=250,height=50,corner_radius=60,border_width=5.5,fg_color=button_fg_color,border_color=button_border_color,
                          bg_color='#AFB3C2',font=tk.CTkFont(size=20,weight='bold',family='Segoe UI Black'),
                          text_color=button_text_color,hover_color=button_hover_color,command=refreshapp)
refresh_button.place(relx=0.81,rely=0.5,anchor='center')
show_attandance_button=tk.CTkButton(app,text='Show Attandance',width=250,height=50,corner_radius=60,border_width=5.5,fg_color=button_fg_color,border_color=button_border_color,
                          bg_color='#AFB3C2',font=tk.CTkFont(size=20,weight='bold',family='Segoe UI Black'),
                          text_color=button_text_color,hover_color=button_hover_color,command=show_attandanceapp)
show_attandance_button.place(relx=0.81,rely=0.6,anchor='center')
export_button=tk.CTkButton(app,text='Export Excel',width=250,height=50,corner_radius=60,border_width=5.5,fg_color=button_fg_color,border_color=button_border_color,
                          bg_color='#AFB3C2',font=tk.CTkFont(size=20,weight='bold',family='Segoe UI Black'),
                          text_color=button_text_color,hover_color=button_hover_color,command=exportapp)
export_button.place(relx=0.81,rely=0.7,anchor='center')
start_message='Welcome\nPress Start to open Attandance Taker'
# notify(app,start_message,7)
set_default_size(app)
# notify('Welcome','Press START to start taking Attandance',4)
app.mainloop()