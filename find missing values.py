import pandas as pd

data = {
    "Name": ["Amrutha", "Anu", "Siri", "Ravi"],
    "Marks": [85, None, 75, 92]
}

df = pd.DataFrame(data)

print(df.isnull())