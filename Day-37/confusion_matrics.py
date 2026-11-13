#Let's understand how to generate a confusion matrix using Python.

from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
import matplotlib.pyplot as plt

#actual results
actual = [1,0,1,1,0,0,1,0,1,0]

#model prediction
predicted= [1,0,1,0,0,1,1,0,1,0]


#create cm
cm= confusion_matrix(actual,predicted)

print("Confusion Matrix:")
print(cm)

#visualize

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Not Spam","Spam"]
)

display.plot()
plt.title("Classification Confusion Matrix")
plt.show()