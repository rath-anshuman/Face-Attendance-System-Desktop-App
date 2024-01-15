import subprocess as ss
import datetime as dt
import streamlit as sl
import pandas as pd
import os
import sys
current_user = os.getlogin()
base_path = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
current_date = dt.date.today()
current_time = dt.datetime.now().time()
hour=current_time.hour
minute=current_time.minute
current_time=(f'{hour}:{minute}')
current_day=current_date.weekday()
days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
current_day=days[current_day]
attandance_data=pd.read_excel(f'Data\Attandance_list\Present_list_{current_date}.xlsx')
# attandance_data=pd.read_excel(f'C:/Users/{current_user}/Downloads/Face detection attandance system/Present_list_2023-10-20.xlsx')
sl.dataframe(attandance_data)