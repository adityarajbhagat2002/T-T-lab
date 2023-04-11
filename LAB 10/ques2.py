# Print All Volkswagen Cars details and also sort them from highest to lowest price.
import pandas as pd

df = pd.read_csv(r'C:\Users\KIIT\Downloads\Automobile_data.csv')

print('All Volkswagen cars sorted from highest to lowest price are:')
print(df[df['company'] == 'volkswagen'].sort_values(by='price', ascending=False))


