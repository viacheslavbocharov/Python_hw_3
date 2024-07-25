number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
action = input("Enter one of the following math actions( + , - , * , / ): ")
result = None

if action == "+":
    result = number1 + number2
elif action == "-":
    result = number1 - number2
elif action == "*":
    result = number1 * number2
elif action == "/":
    if number2 == 0:
        result = "You can't divide on zero"
    else:
        result = number1 / number2
else:
    result = "Undefined math action"

if isinstance(result, str):
    print(result)
else:
    print(str(number1) + " " + action + " " + str(number2) + " = " + str(result))

