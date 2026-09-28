import pandas as pd

data = {
    "Name": ["Amrutha", "Anu", "Siri", "Ravi"],
    "Age": [20, 21, 20, 22],
    "Marks": [85, 90, 88, 92]
}

df = pd.DataFrame(data)

print("First Three Rows:")
print(df.iloc[0:3])