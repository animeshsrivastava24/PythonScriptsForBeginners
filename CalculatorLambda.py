# Application makes a simple calculator with lambda function


# The function performs calculation
def calculate(entered_data):
    x_number = ''
    y_number = ''
    operator = None
    for char in entered_data:
        if char.isdigit():
            if operator is None:
                x_number += char
            else:
                y_number += char
        elif char in operations:
            operator = char
        elif char.isspace:
            pass
        else:
            raise Exception('invalid operator: ' + char)
    return operations[operator](int(x_number), int(y_number))


operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

print(calculate(input('Input what you want to calculate: ')))
