import pandas as pd

data = {
    "Name": ["Amrutha", "Anu", "Siri", "Ravi", "Teja"],
    "Marks": [85, 92, 75, 88, 95]
}

df = pd.DataFrame(data)

sorted_df = df.sort_values("Marks")

print(sorted_df)