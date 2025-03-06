def calculator(a, b, sign):
    if sign == '+':
        print(a + b)
    elif sign == '-':
        print(a - b)
    elif sign == '*':
        print(a * b)
    else:
        print(a / b)


calculator(2, 3, '*')
calculator(2,2,'+')