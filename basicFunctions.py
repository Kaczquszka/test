import math


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

# has to be corrected because i is at some point a float


def primeNumber(n):
    isPrime = True
    for i in range(math.sqrt(n)):
        if n % i == 0:
            isPrime = False
    print(isPrime)
  

primeNumber(4)
primeNumber(2)
