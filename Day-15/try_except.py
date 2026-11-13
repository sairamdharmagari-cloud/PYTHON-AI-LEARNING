#Without exception handling:

num = int(input("Enter a number: "))
print(10 / num)

#If the user enters 0, Python crashes with an error

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)

except:
    print("Something went wrong!")

   # Handle Specific Errors
#It's better to specify the error:

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")