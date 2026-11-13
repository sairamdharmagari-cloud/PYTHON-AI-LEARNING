marks = [90, 85, 78, 92, 88]

total = sum(marks)
average = total / len(marks)

print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", max(marks))
print("Lowest:", min(marks))

#
marks = []

for i in range(5):
    mark = int(input("Enter mark: "))
    marks.append(mark)

print("Marks:", marks)
print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))