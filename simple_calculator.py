def calculate_nums(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        try:
            if num2 == 0:
                raise Exception('Cannot divide by zero')
            else:
                return num1 / num2
        except Exception as e:
            return str(e)  # Return the error message as a string
    else:
        return "Invalid operator"

num1 = int(input('Enter a number: '))
op = input('Enter operator (+, -, *, /): ')
num2 = int(input('Enter a second number: '))
result = calculate_nums(num1, num2, op)
print(num1, op, num2, '=', result)
