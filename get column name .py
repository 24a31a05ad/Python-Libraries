import pandas as pd

data = {
    "Name": ["Amrutha", "Anu", "Siri"],
    "Marks": [85, 90, 75],
    "Age": [20, 21, 19]
}

df = pd.DataFrame(data)

print("Column Names:")
print(df.columns.tolist())