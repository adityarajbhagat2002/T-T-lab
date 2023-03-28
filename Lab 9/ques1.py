import pandas as pd

df_quizScore= pd.read_excel(r"C:\Users\KIIT\Downloads\Quiz.xlsx",sheet_name="Form Responses 1")
#print(df_quizScore)

df_attendance=pd.read_excel(r"C:\Users\KIIT\Downloads\Attendance.xlsx",sheet_name="CSE17-T&T Lab")
#print(df_attendance)

#print(df_quizScore[df_quizScore['Timestamp'] >= pd.Timestamp(2023, 2, 14, 0, 0, 0)]['Score'])
df_attendance['QUIZ-1  (SCORE/ ABS)'] = df_quizScore[df_quizScore['Timestamp'] < pd.Timestamp(2023, 2, 14, 0, 0, 0)]['Score']
df_attendance['QUIZ-2  (SCORE/ ABS)'] = df_quizScore[df_quizScore['Timestamp'] > pd.Timestamp(2023, 2, 14, 0, 0, 0)]['Score']
print(df_attendance['QUIZ-1  (SCORE/ ABS)'])
#print(df_attendance['QUIZ-2  (SCORE/ ABS)'])



