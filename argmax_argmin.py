import numpy as np

arr = np.array([15, 8, 25, 12, 30])

max_index = np.argmax(arr)
min_index = np.argmin(arr)

print("Array:", arr)
print("Index of maximum value:", max_index)
print("Index of minimum value:", min_index)