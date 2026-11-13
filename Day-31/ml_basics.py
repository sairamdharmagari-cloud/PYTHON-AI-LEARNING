import pandas as pd

data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Score": [35, 45, 55, 65, 75, 85]
}

df = pd.DataFrame(data)

print(df)

X = df[["Hours"]]
y = df["Score"]

'''Notice the double brackets:
df[["Hours"]]
because X should remain a DataFrame containing the feature column.'''