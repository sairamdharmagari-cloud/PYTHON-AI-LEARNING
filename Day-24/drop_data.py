import pandas as pd

data = {
    "Name": ["Sairam", "Rahul", "Arjun", "Kiran"],
    "Age": [20, None, 21, 22],
    "Marks": [90, 85, None, 95]
}

df = pd.DataFrame(data)

clean_df = df.dropna()

print(clean_df)

#dropna() removes rows containing missing values.

#In real ML projects, you don't blindly delete missing data. You first understand why it's missing and choose an appropriate strategy.

print(df.duplicated())
#count duplicates
print(df.duplicated().sum())
#remove duplicates
df = df.drop_duplicates()