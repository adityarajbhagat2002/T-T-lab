import pandas as pd

attendanceFrame = pd.read_excel(r'C:\Users\KIIT\Downloads\Attendance.xlsx', sheet_name='CSE17-T&T Lab')
quizFrame = pd.read_excel(r'C:\Users\KIIT\Downloads\Quiz.xlsx', sheet_name='Form Responses 1')

for index, row in attendanceFrame.iterrows():
    curQuizFrame = quizFrame[row['ROLL NO.'] == quizFrame['ROLL']]
    quiz1Array = curQuizFrame[curQuizFrame['Timestamp'] < pd.Timestamp(2023, 2, 14, 0, 0, 0)]['Score'].values
    quiz2Array = curQuizFrame[curQuizFrame['Timestamp'] >= pd.Timestamp(2023, 2, 14, 0, 0, 0)]['Score'].values
    attendanceFrame.loc[index, 'QUIZ-1  (SCORE/ ABS)'] = quiz1Array[0] if len(quiz1Array) else 'ABS'
    attendanceFrame.loc[index, 'QUIZ-2  (SCORE/ ABS)'] = quiz2Array[0] if len(quiz2Array) else 'ABS'

attendanceFrame.to_excel(r'C:\Users\KIIT\Downloads\Attendance.xlsx')
