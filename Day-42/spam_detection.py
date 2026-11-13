from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# 1. Dataset
messages = [
    "win money now",
    "claim your free prize",
    "free offer win cash",
    "you won a lottery",
    "click here to claim reward",
    "exclusive offer just for you",
    "get free gift today",
    "win a brand new phone",
    "urgent claim your cash prize",
    "congratulations you won money",
    "meeting at office today",
    "please send the report",
    "let us discuss the project",
    "are you coming tomorrow",
    "the meeting starts at ten",
    "please call me later",
    "project deadline is next week",
    "your assignment is ready",
    "let us have lunch",
    "see you at the office"
]

# 1 = Spam, 0 = Not Spam
labels = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    messages,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels
)
# 3. Create pipeline
model=make_pipeline(
    CountVectorizer(),
    MultinomialNB()
)

# 4 .Train model
model.fit(X_train,y_train)

# 5. Predict test messages
y_pred = model.predict(X_test)

# 6. Evaluate
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy:",round(accuracy*100,2),"%")

print("Classification Report:")
print(classification_report(
    y_test,
    y_pred,
    zero_division=0
))

# 7. Test a new message
new_message = [
    "Congratulations win your free cash prize"
]

prediction = model.predict(new_message)


if prediction[0] ==1:
    print("\n New Message: Spam")
else:
    print("\n New Message: Not Spam")