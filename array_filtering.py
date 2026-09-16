import numpy as np

arr = np.array([10, 25, 30, 45, 50, 65])

result = arr[arr > 30]

print("Original Array:", arr)
print("Elements greater than 30:", result)