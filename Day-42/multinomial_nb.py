#This algorithm is especially useful for text classification.

#Let's classify messages as Spam or Not Spam using word counts.

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training messages
messages = [
    "win money now",
    "claim your free prize",
    "free offer win cash",
    "meeting at office today",
    "please send the report",
    "let us discuss the project",
    "win a free gift",
    "team meeting tomorrow"
]
# Labels: 1 = Spam, 0 = Not Spam
labels= [1,1,1,0,0,0,1,0]

#Convert text into numerical word count
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(messages)

#Create model
model = MultinomialNB()

#Train model
model.fit(X ,labels)

# Convert new message into word counts
new_message = ["win free money"]

new_message_vector= vectorizer.transform(new_message)

#Prediction

prediction= model.predict(new_message_vector)

if prediction[0] ==1:
    print("Spam Message")
else:
    print("Not Spam Message")