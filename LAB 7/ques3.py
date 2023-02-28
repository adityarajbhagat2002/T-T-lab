import numpy as np

a=np.array(['PYTHON' , 'PHP' , 'JS' , 'EXAMPLES' , 'HTML '],dtype=str)

print("Original array : ")
print(a)

c=np.char.find(a,'P')

print(c)
