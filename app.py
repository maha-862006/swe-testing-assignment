from calculator import Calculator

calc = Calculator()

print("Quick-Calc")

a = float(input("Enter first number: "))
operation = input("Enter operation (+ - * /): ")
b = float(input("Enter second number: "))

if operation == "+":
    print(calc.add(a, b))
elif operation == "-":
    print(calc.subtract(a, b))
elif operation == "*":
    print(calc.multiply(a, b))
elif operation == "/":
    print(calc.divide(a, b))
else:
    print("Invalid operation")