# import customtkinter as tk

# def show_notification(root, message, time):
#     time *= 1000
#     notification_tpl = tk.CTkToplevel(root)
#     notification_tpl.lift(aboveThis=root)
#     # notification_tpl.resizable(False, False)
#     notification_tpl.title("Notification")

#     notification_label = tk.CTkLabel(notification_tpl, text=message, padx=10, pady=10)
#     notification_label.pack()

#     notification_tpl.after(time, notification_tpl.destroy) 

# from plyer import notification
# import time
# import plyer 

# plyer.notification


# from plyer import notification
# import time

# def show_notification():
#     notification.notify(title="Notification",message="This is a notification message.",timeout=3)

# if __name__ == "__main__":
#     show_notification()
#     # time.sleep(3) # Wait for the notification to close
# import os
# import sys


# base_path = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))

# from win10toast import ToastNotifier

# def show_notification(head,message,time):
#     toast = ToastNotifier()
#     toast.show_toast(head, message, time,icon_path=False)

# if __name__ == "__main__":
#     # show_notification()
#     pass