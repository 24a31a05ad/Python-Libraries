import pandas as pd

data = {
    "Name": ["Amrutha", "Anu", "Siri"],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

df["Result"] = ["Pass", "Pass", "Pass"]

print(df)