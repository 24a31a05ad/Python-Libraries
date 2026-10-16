import pandas as pd

data = {
    "Name": ["Amrutha", "Anu", "Siri", "Ravi"],
    "Marks": [85, 90, 75, 92]
}

df = pd.DataFrame(data)

df = df.drop(1)
df = df.reset_index(drop=True)

print(df)