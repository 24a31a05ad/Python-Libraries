import pandas as pd

data = {
    "Name": ["Amrutha", "Anu", "Siri", "Ravi", "Teja", "Kiran"],
    "Marks": [85, 90, 75, 92, 88, 79]
}

df = pd.DataFrame(data)

print(df.head(5))