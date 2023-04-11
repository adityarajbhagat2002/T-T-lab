# Find details of car with 4 number of cylinders with average mileage greater than 15
import pandas as pd

df = pd.read_csv(r'C:\Users\KIIT\Downloads\Automobile_data.csv')

print('Details of car with 4 number of cylinders with average mileage greater than 15 are:')
print(df[(df['num-of-cylinders'] == 'four') & (df['average-mileage'] > 15)])