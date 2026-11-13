import matplotlib.pyplot as plt

names = ["Sairam", "Rahul", "Arjun", "Kiran"]
marks = [90, 85, 78, 95]

plt.bar(names, marks)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()