def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))

#Create a function that calculates the average of three marks:

def calculate_average(a, b, c):
    return (a + b + c) / 3

physics = int(input("Physics: "))
chemistry = int(input("Chemistry: "))
maths = int(input("Maths: "))

average = calculate_average(physics, chemistry, maths)
print("Average:", average)

#This is a great exercise because you're combining functions + input + calculations.