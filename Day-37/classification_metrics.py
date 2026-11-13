#Calculate all four metrics in one program

from sklearn.metrics import(
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

actual = [1, 0, 1, 1, 0, 0, 1, 0, 1, 0]

predicted = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

accuracy = accuracy_score(actual,predicted)
precision = precision_score(actual,predicted)
recall = recall_score(actual,predicted)
f1= f1_score(actual,predicted)

print("Accuracy:",round(accuracy*100,2),"%")
print("Precision:",round(precision,4))
print("Recall:",round(recall,4))
print("F1 Score:",round(f1,4))