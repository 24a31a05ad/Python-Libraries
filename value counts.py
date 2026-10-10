import pandas as pd

data = {
    "Name": ["Amrutha", "Anu", "Siri", "Ravi", "Anu"],
    "City": ["Kakinada", "Hyderabad", "Kakinada", "Vijayawada", "Hyderabad"]
}

df = pd.DataFrame(data)

print(df["City"].value_counts())