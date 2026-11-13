import matplotlib.pyplot as plt

subjects = ["Physics", "Chemistry", "Maths"]
marks = [90, 85, 95]

plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%"
)

plt.title("Marks Distribution")

plt.show()