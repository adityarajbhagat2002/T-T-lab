import pandas as pd

df = pd.read_csv(r'C:\Users\KIIT\Downloads\Automobile_data.csv')

print('First five rows are:')
print(df.head(5))

print('Last five rows are:')
print(df.tail(5))
