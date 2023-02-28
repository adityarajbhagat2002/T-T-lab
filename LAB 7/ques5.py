import numpy as np
arr=np.array([[34,43,73],
            [82,22,12],
            [53,94,66]])
amin_value = np.amin(arr, axis=1)
print('Printing amin Of Axis 1 ')
print(amin_value)
amax_value = np.amax(arr, axis=0)
print('Printing amax Of Axis 0 ')
print(amax_value)
