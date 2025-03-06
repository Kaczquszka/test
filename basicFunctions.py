def calculator(a, b, sign):
    if sign == '+':
        print(a + b)
    elif sign == '-':
        print(a - b)
        print("you just subtracted two numbers")
        print(a+b+b)
    elif sign == '*':
        print(a * b)
    elif sign=='h':
        print("wtf")    
    else:
        if b == 0:
            print("pamiętaj cholero nie dziel przez zero")
            return 0
        else:
            print(a / b)


calculator(2, 3, '*')
calculator(2, 2, '+')
calculator(2, 0, '/')
