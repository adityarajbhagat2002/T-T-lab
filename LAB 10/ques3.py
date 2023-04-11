# Count total cars per company and their average price.
import pandas as pd

df = pd.read_csv(r'C:\Users\KIIT\Downloads\Automobile_data.csv')

print('Total cars per company and their average price are:')
print(df.groupby('company')['price'].agg(['count', 'mean']))
