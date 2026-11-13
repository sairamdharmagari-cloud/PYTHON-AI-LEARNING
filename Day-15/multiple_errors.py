try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Second number cannot be zero.")