import pandas as pd

data = {
    "Name": ["Amrutha", "Anu", "Siri"],
    "Age": [20, 21, 20],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print(df)