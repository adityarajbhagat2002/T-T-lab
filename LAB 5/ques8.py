# Write a program to extract all the contiguous 3x3 blocks from a random 10x10 matrix.

import numpy as np
arr = np.random.randint(0, 5, (10, 10))
print("Original array:")
print(arr)
n = 3
i = 1 + (arr.shape[0]-3)
j = 1 + (arr.shape[1]-3)
result = np.lib.stride_tricks.as_strided(arr, shape=(i, j, n, n), strides=arr.strides + arr.strides)
print("\nContiguous 3x3 blocks:")
print(result)