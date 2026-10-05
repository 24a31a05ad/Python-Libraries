import pandas as pd

data = {
    "Name": ["Amrutha", "Anu", "Siri", "Ravi", "Teja"],
    "Marks": [85, 90, 75, 92, 88]
}

df = pd.DataFrame(data)

print(df["Marks"].describe())