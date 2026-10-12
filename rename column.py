import pandas as pd

data = {
    "Name": ["Amrutha", "Anu", "Siri"],
    "Marks": [85, 90, 75]
}

df = pd.DataFrame(data)

df = df.rename(columns={"Marks": "Score"})

print(df)