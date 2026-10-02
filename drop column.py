import pandas as pd

data = {
    "Name": ["Amrutha", "Anu", "Siri"],
    "Marks": [85, 90, 75],
    "Age": [20, 21, 20]
}

df = pd.DataFrame(data)

df = df.drop("Age", axis=1)

print(df)