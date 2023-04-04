import pandas as pd

answers = pd.read_excel(r'C:\Users\KIIT\Downloads\QUIZ-ANSWERS.xlsx' , sheet_name='Sheet1')
answers = answers.to_dict('records')
quizFrame = pd.read_excel(r'C:\Users\KIIT\Downloads\Quiz.xlsx', sheet_name='Form Responses 1')

displayFrame = pd.DataFrame(columns=['Q. No.', 'No. of Students Answered correctly',
                            'No. of Students Answered incorrectly', 'Difficulty Level(%)'])
quizFrame = quizFrame[quizFrame['Timestamp']
                    < pd.Timestamp(2023, 2, 14, 0, 0, 0)]

for ans in answers:
    correct = quizFrame[quizFrame[ans['Q. No.']] == ans['Answer']].shape[0]
    incorrect = quizFrame[quizFrame[ans['Q. No.']] != ans['Answer']].shape[0]
    displayFrame = pd.concat([displayFrame, pd.DataFrame({'Q. No.': [ans['Q. No.']], 'No. of Students Answered correctly': [correct],
                                                          'No. of Students Answered incorrectly': [incorrect], 'Difficulty Level(%)': [incorrect / (correct + incorrect) * 100]})], ignore_index=True)

displayFrame.sort_values('Difficulty Level(%)', ascending=False, inplace=True)
print(displayFrame)
