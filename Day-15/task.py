try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)
    print("Division:", num1 / num2)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Calculator finished.")

#try      → Code that might cause an error
#except   → What to do if an error occurs
#finally  → Code that always runs