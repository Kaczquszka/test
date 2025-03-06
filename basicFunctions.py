def calculator(a, b, sign):
    if sign == '+':
        print(a + b)
    elif sign == '-':
        print(a + b)
        print("you just subtracted two numbers")
    elif sign == '*':
        print(a * b)
    else:
        print(a / b)
        print("pamiętaj cholero nie dziel przez zero")


calculator(2, 3, '*')
calculator(2, 2, '+')
