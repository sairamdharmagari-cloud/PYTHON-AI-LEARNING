from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

messages = [
    "win free money",
    "claim your prize",
    "get free cash",
    "win a new phone",
    "meeting starts today",
    "send me the report",
    "project work is ready",
    "call me tomorrow",
    "free gift offer",
    "claim your reward",
    "office meeting tomorrow",
    "finish your assignment"
]

# 1 = Spam, 0 = Not Spam
labels = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0]

X_train,X_test,y_train,y_test=train_test_split(
    messages,
    labels,
    test_size=0.2,
    random_state=42,
    stratify=labels
)

model = make_pipeline(
    CountVectorizer(),
    MultinomialNB()
)

model.fit(X_train,y_train)

y_pred =model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
print("Accuracy:",round(accuracy*100,2),"%")

new_message = ["Congratulations! You won a free prize"]

prediction = model.predict(new_message)

if prediction[0]==1:
    print("Prediction: Spam")
else:
    print("Prediction: Not Spam")