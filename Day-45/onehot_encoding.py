import pandas as pd

data={
    "Name":["Rahul","Anil","Sai","Ram"],
    "City":[
        "Hyd",
        "Mumbai",
        "Delhi",
        "Chennai"
    ]
}

df = pd.DataFrame(data)
print(df)


# 2. Apply One-Hot Encoding
encoded_df = pd.get_dummies(
    df,
    columns=["City"],
    dtype=int
)

print("\nOne-Hot Encoded Data:")
print(encoded_df)