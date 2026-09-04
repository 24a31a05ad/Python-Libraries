import numpy as np

arr = np.arange(1, 7)

new_arr = arr.reshape(2, 3)

print("Original Array:", arr)
print("Reshaped Array:")
print(new_arr)