import pandas as pd

data = {
    "Name": ["Amrutha", "Anu", "Siri", "Ravi"],
    "Marks": [85, None, 75, 92]
}

df = pd.DataFrame(data)

df = df.dropna()

print(df)