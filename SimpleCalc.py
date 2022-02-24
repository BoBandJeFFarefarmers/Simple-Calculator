numberOne = int(input('Type a number: '))
operation = input('Type in an operation (+, *, -, /): ')
numberTwo = int(input('Type another number: '))

if operation == "+":
    print(numberOne + numberTwo)
elif operation == "*":
    print(numberOne * numberTwo)
elif operation == "-":
    print(numberOne - numberTwo)
elif operation == "/":
    print(numberOne / numberTwo)