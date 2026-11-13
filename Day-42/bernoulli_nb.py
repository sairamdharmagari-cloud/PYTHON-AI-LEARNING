from sklearn.naive_bayes import BernoulliNB

# Features: Free, Win, Offer
X = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 0],
    [0, 0, 0],
    [0, 0, 1],
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0]
]

# 1 = Spam, 0 = Not Spam
y = [1, 1, 1, 0, 0, 0, 1, 0]

# Create model
model = BernoulliNB()

# Train
model.fit(X, y)

# New email:
# Free=1, Win=1, Offer=0
new_email = [[1, 1, 0]]

# Predict
prediction = model.predict(new_email)

if prediction[0] == 1:
    print("Spam")
else:
    print("Not Spam")