name = input("Enter your name: ")

physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))
maths = int(input("Enter Maths marks: "))

total = physics + chemistry + maths
average = total / 3

print("\n----- RESULT -----")
print("Name:", name)
print("Physics:", physics)
print("Chemistry:", chemistry)
print("Maths:", maths)
print("Total:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 35:
    print("Grade: D")
else:
    print("Grade: Fail")