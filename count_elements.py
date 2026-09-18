import numpy as np

arr = np.array([10, 25, 30, 45, 50, 65])

count = np.count_nonzero(arr > 30)

print("Array:", arr)
print("Elements greater than 30:", count)