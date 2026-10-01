import pandas as pd

data = {
    "Name": ["Amrutha", "Anu", "Siri"],
    "Marks": [85, 90, 75]
}

df = pd.DataFrame(data)

df["Bonus"] = df["Marks"] + 5

print(df)