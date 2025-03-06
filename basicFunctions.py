def calculator(a, b, sign):
    if sign == '+':
        print(a + b)
    elif sign == '-':
        print(a - b)
        print(a+b+b)
    elif sign == '*':
        print(a * b)
    else:
        print("lalallal")
        print(a / b)


calculator(2, 3, '*')
calculator(2, 2, '+')
