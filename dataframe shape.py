import pandas as pd

data = {
    "Name": ["Amrutha", "Anu", "Siri", "Ravi"],
    "Marks": [85, 90, 75, 92],
    "Age": [20, 21, 19, 20]
}

df = pd.DataFrame(data)

print("Number of rows and columns:", df.shape)
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])