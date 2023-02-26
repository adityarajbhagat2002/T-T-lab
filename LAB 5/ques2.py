import numpy as np

arr=np.random.randint(5,21,size=10)

print(f'Original array ->{arr}')

arr=np.flip(arr)

print(f'Reversed array->{arr}')
