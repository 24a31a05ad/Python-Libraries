import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Are all elements greater than 5?", np.all(arr > 5))
print("Is any element greater than 45?", np.any(arr > 45))