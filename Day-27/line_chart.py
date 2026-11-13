import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
marks = [60, 65, 70, 80, 90]

plt.plot(days, marks)

plt.xlabel("Days")
plt.ylabel("Marks")
plt.title("Marks Progress")

plt.show()