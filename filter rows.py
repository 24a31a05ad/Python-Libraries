import pandas as pd

data = {
    "Name": ["Amrutha", "Anu", "Siri", "Ravi"],
    "Marks": [85, 90, 65, 92]
}

df = pd.DataFrame(data)

result = df[df["Marks"] >= 80]

print(result)