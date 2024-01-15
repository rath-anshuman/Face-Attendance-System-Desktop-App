import cv2 
import face_recognition as frcn
import os 
import numpy as np
import pickle
import keyboard
import time


# # Directory containing images of known individuals
attendease_path='Data/Attandease'

# known_face_encodings=[]
images=[]
attendease_name=[]


images_list=os.listdir(attendease_path)


for photos in images_list:
    current_image=cv2.imread(f'{attendease_path}\{photos}')
    images.append(current_image)
    attendease_name.append(os.path.splitext(photos)[0])



known_face_encodings = []
try:
    with open('Data/proccessing/known_face_encodings.pkl', 'rb') as file:
        known_face_encodings = pickle.load(file)
    # print('Known face encodings loaded from pickle file.')
except FileNotFoundError:
    print('Pickle file not found. Please run Program encoder to create known face encodings.')


def recognition():
    import attendence as ac
    cap=cv2.VideoCapture(0)
    while True :
        success, cam = cap.read()
        # imgS=cv2.resize(cam,(0,0),None,0.25,0.25)
        imgS=cv2.cvtColor(cam,cv2.COLOR_BGR2RGB)
        cam_img_loc=frcn.face_locations(imgS)   
        cam_image_encodings=frcn.face_encodings(imgS,cam_img_loc)
        cam_image_encodings = [np.array(enc) for enc in cam_image_encodings]

        for encode_face,face_loc in zip(cam_image_encodings,cam_img_loc):
            check_match=frcn.compare_faces(known_face_encodings,cam_image_encodings[0]) 
            face_dis=frcn.face_distance(known_face_encodings,encode_face)
            print(face_dis)

            match_index=np.argmin(face_dis)

            if check_match[match_index]:
                # global name
                name=attendease_name[match_index].upper()
                y1,x2,y2,x1=face_loc
                cv2.rectangle(cam,(x1,y1),(x2,y2),(52, 32, 79),3)
                # cv2.rectangle(cam,(x1,y2),(x2,y2-10),(52, 32, 79),cv2.FILLED)
                cv2.putText(cam,name,(x1-6,y2+6),cv2.Formatter_FMT_C,1,(255,255,255),2)
                


        cv2.imshow('camera',cam) 
        import attendence as ac
        
        if cv2.waitKey(100) & 0xFF == ord('p'):
            ac.present(name)
            print(f'{name} attended')
        if cv2.waitKey(100) &  0xFF == ord('q'):
            print('quiting...')
            time.sleep(3)
            break
    

if __name__=='__main__':
   
   
   recognition()