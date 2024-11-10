def calculator():
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        operator = input("Enter your operator (+, -, *, /): ")

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            result = num1 / num2
        else:
            return "Error: Invalid operator. Please use +, -, *, or /."

        # Print result rounded to 3 decimal places
        print(f"Your result is: {round(result, 3)}")

    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the calculator
calculator()
