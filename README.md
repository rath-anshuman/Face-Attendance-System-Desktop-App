Face Recognition Attendance System
This repository holds the source code for a Face Detection Attendance System built using Python, OpenCV, and face_recognition libraries. It leverages computer vision technology to automate attendance recording, offering increased accuracy and efficiency compared to traditional methods.

Key Features:

Real-time Face Recognition: Utilizes OpenCV and face_recognition to capture video feed, identify faces, and compare them against a pre-existing database.
Automated Attendance Management: Records attendance based on recognized faces and updates a dynamic Excel workbook with date, time, and subject information.
User-Friendly Interface: Provides a web interface for accessing attendance data and managing user profiles.
Future Enhancements: Explore opportunities for integrating machine learning for improved recognition, mobile app development, and advanced data analytics.
Getting Started:

Clone the repository.
Install required libraries (reqiured are mention in requirement.md).
Change rotines and timing according to you in the script by editing 'routine.py' file.
Run the main script (app.pyw).
Register new faces for taking attendance by 'New Registration' button available in the interface. 
Take Attendance through the 'START' button by accesing 'start capture' and 'register attendance' function by given button.
Access the web interface through 'SHOW ATTENDANCE' button.
Export the excel format of that taken attendance of the current date by pressing 'Export Excel button'.



This project uses an Excel workbook as its database for simplicity. Future versions could implement more robust database solutions.
The system prioritizes user privacy and avoids storing sensitive information such as facial features.
Contributions:
We welcome contributions and suggestions from the community! Feel free to fork the repository and help us improve the Face Detection Attendance System.
