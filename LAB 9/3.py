import pandas as pd

attendanceFrame = pd.read_excel(r'C:\Users\KIIT\Downloads\Attendance.xlsx', sheet_name='Sheet1')

print(attendanceFrame[(attendanceFrame['QUIZ-1  (SCORE/ ABS)'] == 'ABS') | (attendanceFrame['QUIZ-2  (SCORE/ ABS)'] == 'ABS')])