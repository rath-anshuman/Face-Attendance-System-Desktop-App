import os
import sys
base_path = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
import datetime  as dt
current_time = dt.datetime.now().time()
hour=current_time.strftime('%H')
minute=current_time.strftime('%M')
current_time=(f'{hour}:{minute}')
current_date = dt.date.today()
current_day=current_date.weekday()
days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
current_day=days[current_day]
Sunday=   ['sunday_leave','sunday_leave','sunday_leave','sunday_leave','sunday_leave','sunday_leave']
Time=     [      '10.30-11.40'        ,        '11.40-12.40'       ,        '12.40-02.00'       ,'02.00-03.00',      '03.00-04.00'         ,     '04.00-05.00'          ]
sequence= [             0             ,              1             ,              2             ,      3      ,             4              ,             5              ]
Monday=   [      '    core    '       ,   'ML for Image Analysis'  ,   'ML for Image Analysis'  ,'Lunch Break',     'IOT Analytics'        ,     'IOT Analytics'        ]
Tuesday=  [      '    core    '       ,   'ML for Image Analysis'  ,    'Mathematics for ML'    ,'Lunch Break',     'IOT Analytics'        ,     'IOT Analytics'        ]
Wednesday=[      '    core    '       ,   'ML for Image Analysis'  ,    'Mathematics for ML'    ,'Lunch Break',      '    core    '        ,'ML for Predective Analysis']
Thursday= [      '    core    '       ,'ML for Predective Analysis',    'Mathematics for ML'    ,'Lunch Break',      '    core    '        ,      '    core    '        ]
Friday=   [      '    core    '       ,    'Mathematics for ML'    ,    'Mathematics for ML'    ,'Lunch Break',      '    core    '        ,      '    core    '        ]
Saturday= [      '    core    '       ,       '    core    '       ,    'Mathematics for ML'    ,'Lunch Break',      '    core    '        ,      '    core    '        ]
routine={
    'Monday':   Sunday,
    'Tuesday':  Tuesday,
    'Wednesday':Wednesday,
    'Thursday': Thursday,
    'Friday':   Friday,
    'Saturday': Saturday
}
def running_schedule(current_time):
    if '10:30' <= current_time <= '11:40':
        return 0
    elif '11:40' <= current_time <= '12:40':
        return 1
    elif '12:40' <= current_time <= '14:00':
        return 2
    elif '14:00' <= current_time <= '15:00':
        return 3
    elif '15:00' <= current_time <= '16:00':
        return 4
    elif '16:00' <= current_time <= '17:00':
        return 5
    else:
        return 'x'
running_index = running_schedule(current_time)
# print(running_index)
def subject_running():
    try:
        subject_running=routine[f'{current_day}'][running_index]
    except:
        subject_running='Invalid class time'
    return subject_running
if __name__=='__main__':
   print(routine)