# Find the average mileage of each car making company.
import pandas as pd

df = pd.read_csv(r'C:\Users\KIIT\Downloads\Automobile_data.csv')

print('Average mileage of each car making company is:')
print(df.groupby('company')['average-mileage'].mean())
