import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Score": [35, 45, 55, 65, 75, 85, 90, 95, 98, 100]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training data:")
print(X_train)

print("\nTesting data:")
print(X_test)

'''What happened?
Original data
     ↓
train_test_split()
     ↓
┌───────────────┬──────────────┐
│ Training 80%  │ Testing 20%  │
└───────────────┴──────────────┘

random_state=42 makes the random split reproducible, so you can get the same split when you run the program again.'''