name = input("Enter your name: ")

physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))
maths = int(input("Enter Maths marks: "))

total = physics + chemistry + maths
avg = total / 3

print("Name:", name)
print("Physics:", physics)
print("Chemistry:", chemistry)
print("Maths:", maths)
print("Total:", total)
print("Average:", avg)